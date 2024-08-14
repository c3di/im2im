# im2im: Automatically Converting In-Memory Image Representations using A Knowledge Graph Approach

[![PyPI - Version](https://img.shields.io/pypi/v/im2im.svg)](https://pypi.org/project/im2im/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/im2im)](https://pypi.org/project/im2im/)
[![Downloads](https://static.pepy.tech/badge/im2im)](https://pepy.tech/project/im2im)
[![Documentation](https://img.shields.io/badge/Doc-tutorial-blue)](https://github.com/c3di/im2im/blob/main/tutorial.ipynb)
[![Tests](https://github.com/c3di/im2im/actions/workflows/python%20tests%20with%20coverage.yml/badge.svg)](https://github.com/c3di/im2im/actions/workflows/python%20tests%20with%20coverage.yml)
[![codecov](https://codecov.io/github/c3di/im2im/graph/badge.svg?token=BWBXANX8W7)](https://codecov.io/github/c3di/im2im)

The `im2im` package provides an automated approach for converting in-memory image representations across a variety of image processing libraries, including `scikit-image`, `opencv-python`, `scipy`, `PIL`, `Matplotlib.plt.imshow`, `PyTorch`, `Kornia` and `Tensorflow`. It handles the nuances inherent to each library's image representation, such as data formats (numpy arrays, PIL images, torch tensors, and so on), color channel (RGB or grayscale), channel order (channel first or last or none), device (CPU/GPU), and pixel intensity ranges.

Im2im was developed for the use in Visual Programming Language for image processing (VPL4IPs) to completely removes the conversions steps required to manually manage image transformations, drastically improving accessibility, specifically for non-expert users. It also addresses the tension between low-level implementation details necessary for compatibility and the high-level image processing operations that VPL4IPs aim to provide. However, the library is a conventional Python package, and as such, it can also be used by directly invoking its functions from any Python image processing program to automate image conversion steps. Considering the relatively low memory footprint and computational overhead of the system, using the library to simplify conventional Python programming is an interesting option as well. 


## Installation

Install the package via pip:
```bash
pip install im2im
```


## Usage

```python
import numpy as np
from im2im import Image, im2im

# Assume an image that is a numpy.ndarray with shape (20, 20, 3) in uint8 format
image = np.random.randint(0, 256, (20, 20, 3), dtype=np.uint8)
# Initialize the image with the corresponding metadata preset for numpy RGB uint8 format
from_im = Image(image, "numpy.rgb_uint8")
# Convert the image to a torch tensor with shape (1, 3, 20, 20), in float32 format,
# normalized to the range [0, 1], and transferred to the GPU
to_im = im2im(from_im, "torch.gpu")
# Access the converted image data via to_im.raw_image
```

For other APIs like `im2im_code`, please refer to [public APIs](https://github.com/c3di/im2im/blob/main/src/im2im/api.py).

## Evaluation

**Comparative Analysis**
The effectiveness and benefits for VPL4IPs are validated through Comparative Analysis](https://github.com/c3di/im2im/blob/main/comparative_analysis).

**Accuracy**
All conversion code snippets are thoroughly verified through [execution checks](https://github.com/c3di/im2im/blob/main/tests/test_conversion_code_in_kg.py) to ensure their correctness.

**Performance Profiling**
Performance is analyzed using the cProfile module, with detailed results available in the [profiling notebooks](https://github.com/c3di/im2im/blob/main/profile).

## Contribution

We welcome all contributions to this project! If you have suggestions, feature requests, or want to contribute in any other way, please feel free to open an issue or submit a pull request. For detailed instructions on developing, building, and publishing this package, please refer to the [README_DEV](https://github.com/c3di/im2im/blob/main/README_Dev.md).

## Cite

Todo

## License

This project is licensed under the MIT License. See the LICENSE file for details.
