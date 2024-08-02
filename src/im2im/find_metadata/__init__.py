from .preset_to_metadata import Metadata4Library, Metadata, PresetToMetadataTable, get_preset_table


def find_target_metadata(source_metadata, target_preset_path) -> Metadata:
    lib, func = target_preset_path.split(".")
    fixed_metadata = get_preset_table().get_metadata(lib, func)
    return source_metadata.copy().update(fixed_metadata)
