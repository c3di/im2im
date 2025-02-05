from pathlib import Path
from datetime import datetime
import sys
import os
import argparse
import timeit
import textwrap
import itertools
import csv

parent_directory = Path.cwd().parent
sys.path.insert(0, str(parent_directory))
src_directory = os.path.join(parent_directory, "src")
sys.path.insert(0, src_directory)

from im2im import im2im_code, im2im, Image, _code_generator
from im2im.knowledge_graph_construction.metedata import encode_metadata, decode_metadata, metadata_values
from tests.image_util import random_test_image_and_expected


def use_single_function_appproach(source_image, source, target, repeat_count=5):
    globals_ = {
        'source_image': source_image,
    }

    code = im2im_code("im_in", source, "im_out", target)
    if code is None:
        return None
    
    imports, main_body = code
    
    callable_code = f"""def tmp_convert(im_in):
{textwrap.indent(main_body.strip(), "    ")}
    return im_out"""
    
    full_code = f"tmp_convert(source_image)"
    time = timeit.timeit(stmt=full_code, setup=f'{imports}\n{callable_code}', number=repeat_count, globals=globals_)
    return time / repeat_count


def use_im2im(source_image, source, target, repeat_count=5):
    globals_ = {
        'im2im': im2im,
        'Image': Image,
        'source_image': source_image,
        'source': source,
        'target': target
    }

    time = timeit.timeit(stmt="im2im(Image(source_image, source), target)", number=repeat_count, globals=globals_)
    return time / repeat_count


def measure_time(pair, res, repeat_count=1):
    source, target = pair
    if not isinstance(res, tuple):
        res = (res, res)
    source_image, _ = random_test_image_and_expected(source, target, res)
    t1 = use_single_function_appproach(source_image, source, target, repeat_count)
    if t1 is None:
        return None
    t2 = use_im2im(source_image, source, target, repeat_count)
    return [encode_metadata(source), encode_metadata(target), round(t1 * 1000, 3), round(t2 * 1000, 3), round(t2 / t1, 2) if t1 != 0 else 0]


def measure_times(pairs, res, repeat_count):    
    cost_time = []
    exception = []
    counter = 1
    total = len(pairs)
    for pair in pairs:
        print(f'{counter}/{total} measure {pair}')
        counter = counter + 1
        t = measure_time(pair, res, repeat_count)
        if t is None:
            continue
        if t[4] < 1:
            exception.append(t)
        else:
            cost_time.append(t)
    return cost_time, exception


def conversion_pairs():
    all_valid_metadata = []
    keys = metadata_values.keys()
    combinations = itertools.product(*(metadata_values[key] for key in keys))
    for combination in combinations:
        metadata = dict(zip(keys, combination))
        if metadata in _code_generator.knowledge_graph.nodes:
            all_valid_metadata.append(metadata)
    nodes_count = len(all_valid_metadata)
    print(f'{nodes_count} total Nodes')

    pairs = []
    for source in all_valid_metadata:
        for target in all_valid_metadata:
            if source != target:
                pairs.append((source, target))
    print(f'{len(pairs)} total Pairs')
    return pairs


def write_to_file(cost_time, file_name):
    header = ','.join(["From", "To", "Single Function Approach (ms)", "Step-by-Step Approach (im2im) (ms)", "Ratio (t2/t1)"])
    content = [header] + [','.join(map(str, t)) for t in cost_time if t is not None]
    with open(file_name, "w") as file:
        file.writelines([line + "\n" for line in content])
    print(f"Successfully written to {file_name}")


def read_paris_from_file(file_path):
    """
    Reads a CSV file and returns a list of tuples containing values 
    from the first and second columns.
    
    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        list of tuple: A list of tuples with values from the first 
        and second columns.
    """
    result = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader, None)
        for row in reader:
            result.append((decode_metadata(row[0]), decode_metadata(row[1])))
    return result


def run(res, repeat, file_path):
    start_time = datetime.now()
    pairs = conversion_pairs() if file_path is None else read_paris_from_file(file_path)

    cost_time, exception = measure_times(pairs, res, repeat)

    for _ in range(5):
        if not exception:
            break
        exception_pair = [(decode_metadata(p[0]), decode_metadata(p[1])) for p in exception]
        valid_on_exception, exception = measure_times(exception_pair, res, repeat)
        cost_time = cost_time + valid_on_exception
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    write_to_file(cost_time, f"{res}_{timestamp}.csv")
    if len(exception) > 0:
        write_to_file(exception, f"{res}_exception_{timestamp}.csv")

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"{res}: Elapsed Time: {int(hours):02}:{int(minutes):02}:{seconds:.2f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--res", type=int, required=True, help="Resolution parameter.")
    parser.add_argument("--repeat", type=int, default=1, help="Number of repetitions for timing on each type conversion.")
    parser.add_argument("--file_path", type=str, help="If the file_path is provided, only the source-target metedata in the file will be measured.")
    args = parser.parse_args()
    
    run(args.res, args.repeat, args.file_path)