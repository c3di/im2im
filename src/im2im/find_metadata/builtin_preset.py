from .preset_to_metadata import Metadata4Library, get_preset_table

preset_table = get_preset_table()

opencv_lib = Metadata4Library(
    {"data_representation": "numpy.ndarray", "color_channel": "bgr", "channel_order": "channel last",
     "minibatch_input": False, "image_data_type": "uint8", "device": "cpu"}, )
opencv_lib.add_preset_with_override_metadata("gray", {"color_channel": "gray", "channel_order": "none"})
preset_table.add_lib_metadata("opencv", opencv_lib)

skimage_lib = Metadata4Library(
    {"data_representation": "numpy.ndarray", "color_channel": "rgb", "channel_order": "channel last",
     "minibatch_input": False, "device": "cpu"})
skimage_lib.add_preset_with_override_metadata("gray", {"color_channel": "gray", "channel_order": "none"})
preset_table.add_lib_metadata("skimage", skimage_lib)

pil_lib = Metadata4Library(
    {"data_representation": "PIL.Image", "color_channel": "rgb", "channel_order": "channel last",
     "minibatch_input": False, "device": "cpu"})
pil_lib.add_preset_with_override_metadata("gray", {"color_channel": "gray", "channel_order": "none"})
preset_table.add_lib_metadata("pil", pil_lib)

numpy_lib = Metadata4Library(
    {"data_representation": "numpy.ndarray", "color_channel": "rgb", "channel_order": "channel last",
     "minibatch_input": False, "device": "cpu"})
numpy_lib.add_preset_with_override_metadata("gray", {"color_channel": "gray", "channel_order": "none"})
numpy_lib.add_preset_with_override_metadata("rgb_uint8", {"image_data_type": "uint8"})
preset_table.add_lib_metadata("numpy", numpy_lib)

torch_lib = Metadata4Library(
    {"data_representation": "torch.tensor", "color_channel": "rgb", "channel_order": "channel first",
     "minibatch_input": True, "image_data_type": "float32(0to1)", "device": "cpu"})
torch_lib.add_preset_with_override_metadata("rgb_gpu", {"color_channel": "rgb", "device": "gpu"})
torch_lib.add_preset_with_override_metadata("gray", {"color_channel": "gray"})
torch_lib.add_preset_with_override_metadata("gray_gpu", {"color_channel": "gray", "device": "gpu"})
preset_table.add_lib_metadata("torch", torch_lib)
