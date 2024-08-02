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
        return final_metadata.update(self.preset_with_override_metadata[preset])


class PresetToMetadataTable:
    def __init__(self):
        self.presets: Dict[str, Metadata4Library] = {}

    def add_lib_metadata(self, lib: str, metadata: Metadata4Library):
        self.presets[lib] = metadata

    # def add_metadata_in_lib(self, lib: str, preset: str, metadata: Metadata):
    #     if lib not in self.presets:
    #         raise Exception(f"Library '{lib}' not found in presets")
    #     self.presets[lib].add_preset_with_override_metadata(preset, metadata)

    def get_metadata(self, lib: str, preset: str | None) -> Metadata:
        if lib not in self.presets:
            raise Exception(f"No metadata available for {lib}")
        return self.presets[lib].get_metadata(preset)


preset_table = PresetToMetadataTable()


def get_preset_table():
    return preset_table
