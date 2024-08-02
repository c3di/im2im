from .preset_to_metadata import Metadata4Library, Metadata, PresetToMetadataTable, get_preset_table
from .builtin_preset import *


def find_target_metadata(source_metadata, target_preset_path) -> Metadata:
    """
    Find the metadata of the target preset path by merging the source metadata with the fixed metadata of the target preset.
    """
    lib, preset = target_preset_path.split(".")
    fixed_metadata = get_preset_table().get_metadata(lib, preset)
    final_metadata = source_metadata.copy()
    final_metadata.update(fixed_metadata)
    return final_metadata
