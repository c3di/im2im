from typing import Union, List

from .preset_to_metadata import Metadata4Library, PresetToMetadataTable, get_preset_table, PossibleMetadata
from .builtin_preset import *
from ..knowledge_graph_construction import is_metadata_complete, Metadata


def get_default_metadata(possible_metadata: PossibleMetadata) -> Metadata:
    default_metadata = {}
    for key, value in possible_metadata.items():
        if isinstance(value, list):
            default_metadata[key] = value[0]
        else:
            default_metadata[key] = value
    return default_metadata


def find_closest_match(possible_metadata: PossibleMetadata, target):
    matched_metadata = {}
    for key, value in target.items():
        allowed_value = possible_metadata.get(key)
        if isinstance(allowed_value, list):
            if value in allowed_value:
                matched_metadata[key] = value
        else:
            matched_metadata[key] = allowed_value
    return matched_metadata


def find_target_metadata(source_metadata, target_preset_path) -> Metadata:
    """
    Return the metadata of the target preset path by finding the closest match with the source metadata.
    """
    all_possible: Union[PossibleMetadata, List[PossibleMetadata]] = get_preset_table().get_possible_metadata(target_preset_path)
    if not isinstance(all_possible, list):
        all_possible = [all_possible]

    for possible_metadata in all_possible:
        closest_match = find_closest_match(possible_metadata, source_metadata)
        if is_metadata_complete(closest_match):
            return closest_match

    return get_default_metadata(all_possible[0])
