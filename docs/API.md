# `im2im` API Documentation

This module provides functionality for converting in-memory image representations using a metadata-guided approach. It includes:

* A `Metadata` structure to describe the image data.

- A unified `Image` class for wrapping image data with metadata.
- The `im2im` function for metadata-aware image conversion.
- Utilities for extending and customizing the knowledge graph for image conversions.

------
## TypedDict: `Metadata`
```python
class Metadata(TypedDict):
    data_representation: str
    color_channel: str
    channel_order: Literal['channel last', 'channel first', 'none']
    minibatch_input: bool
    image_data_type: Literal[
        'uint8', 'uint16', 'uint32', 'uint64',
        'float32', 'float64', 'double',
        'int8', 'int16', 'int32', 'int64',
        'float32(0to1)', 'float32(-1to1)',
        'float64(0to1)', 'float64(-1to1)',
        'double(0to1)', 'double(-1to1)'
    ]
    device: str
```
Describes the metadata of an image representation used for compatibility checking and transformation.

### Fields
- `data_representation`: Name of the data structure (e.g., 'torch.tensor', 'numpy.ndarray').

- `color_channel`: Channel information (e.g., 'rgb', 'gray', 'multi-spectral').

- `channel_order`: 'channel last' | 'channel first' | 'none' — spatial layout of channels.

- `minibatch_input`: Whether the image is part of a batch (True) or single instance (False).

- `image_data_type`: Pixel type, including normalized variants.

- `device`: Execution device (e.g., 'cpu', 'cuda', 'cuda:0').

## Class: `Image`

```python
Image(raw_image, config: Union[Metadata, str])
```

Wraps a raw image with a metadata configuration describing its structure and storage.

### Parameters

- `raw_image`: Any
   The in-memory image (e.g., NumPy array, PyTorch tensor).
- `config`: `Metadata | str`
   If a string, should be a preset (e.g., `"torch.tensor.hw.rgb.float32.cpu"`).
   If a `Metadata` object, it must be complete.

### Raises

- `Exception`: If metadata is incomplete.

------

## Function: `im2im`

```python
im2im(source_image: Image, target: Union[Metadata, str], allow_lossy_fallback=True) -> Image
```

Converts an image from one metadata format to another.

### Parameters

- `source_image`: `Image`
   The input image to be converted.
- `target`: `Metadata | str`
   Target metadata or preset identifier.
- `allow_lossy_fallback`: `bool` (default: `True`)
   Whether to allow fallback conversions that may lose information.

### Returns

- `Image`: A new image in the target format.

### Example

```python
import numpy as np
from im2im import Image, im2im

# Example input: an image that is a numpy.ndarray with shape (20, 20, 3) in uint8 format
to_be_converted = Image(np.random.randint(0, 256, (20, 20, 3), dtype=np.uint8), "numpy.rgb_uint8")
# Convert to the target image with metadata preset "torch.gpu".
converted: Image = im2im(to_be_converted, "torch.gpu")
```

------

## Function: `im2im_code`

```python
im2im_code(source_var_name: str, source_metadata: Metadata, target_var_name: str, target_metadata: Metadata,
           allow_lossy_fallback=True) -> List[str]
```

Generates Python code to convert from source metadata to target metadata.

### Parameters

- `source_var_name`: `str`
   Variable name of the source image.
- `source_metadata`: `Metadata`
   Metadata of the source image.
- `target_var_name`: `str`
   Variable name for the target image.
- `target_metadata`: `Metadata`
   Metadata of the target image.
- `allow_lossy_fallback`: `bool` (default: `True`)
   Allow lossy conversions if no lossless path exists.

### Returns

- `List[str]`: A list of Python code lines for the conversion.

------

## Function: `new_cost_function_on_edge`

```python
new_cost_function_on_edge(cost_function: Callable)
```

Sets a custom cost function for evaluating conversion paths.

### Parameters

- `cost_function`: Callable
   A function taking `(source_metadata, target_metadata, edge_attributes)` and returning a cost tuple.

------

## Function: `new_heuristic_function`

```python
new_heuristic_function(function: Callable)
```

Sets a custom heuristic function for pathfinding in the knowledge graph.

------

## Function: `get_possible_metadata`

```python
get_possible_metadata(preset: str) -> PossibleMetadata
```

Returns possible metadata values inferred from a preset string.

------

## Function: `add_lib_metadata`

```python
add_lib_metadata(lib: str, metadata: Metadata4Library)
```

Adds metadata information for a library to the preset table.

------

## Function: `add_meta_values_for_image`

```python
add_meta_values_for_image(new_metadata: MetadataValues)
```

Adds new metadata values to the knowledge graph (e.g., new data types or layouts).

------

## Function: `add_edge_factory_cluster`

```python
add_edge_factory_cluster(factory_cluster: FactoriesCluster)
```

Registers a new cluster of conversion routines (edges) in the knowledge graph.

------

## Function: `add_conversion_for_metadata_pairs`

```python
add_conversion_for_metadata_pairs(
    pairs: Union[List[ConversionForMetadataPair], ConversionForMetadataPair]
)
```

Adds explicit conversion implementations between metadata pairs.

