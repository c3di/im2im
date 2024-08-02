from typing import Dict

from ..knowledge_graph_construction import Metadata


class Metadata4Library:
    metadata: Metadata = None
    preset_with_override_metadata: Dict[str, Metadata] = {}

    def __init__(self, metadata):
        self.metadata = metadata

    def add_preset_with_override_metadata(self, preset, metadata):
        self.preset_with_override_metadata[preset] = metadata

    def get_metadata(self, preset):
        if preset not in self.preset_with_override_metadata:
            return self.metadata
        final_metadata = self.metadata.copy()
        final_metadata.update(self.preset_with_override_metadata[preset])
        return final_metadata


class PresetToMetadataTable:
    def __init__(self):
        self.presets: Dict[str, Metadata4Library] = {}

    def add_lib_metadata(self, lib: str, metadata: Metadata4Library):
        self.presets[lib] = metadata

    def get_metadata(self, path) -> Metadata:
        if "." in path:
            lib, path = path.split(".")
        else:
            lib = path
            path = None
        if lib not in self.presets:
            raise Exception(f"No metadata available for {lib}")
        return self.presets[lib].get_metadata(path)


preset_table = PresetToMetadataTable()


def get_preset_table():
    return preset_table
