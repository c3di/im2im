# im2im: Automatically Converting In-Memory Image Representations using A Knowledge Graph Approach

**NOTE**: In the anonymous version, when clicking on links (such as those in the README), you may experience longer loading times on the anonymized GitHub site. We recommend navigating to the file manually and then clicking to open it directly

**NOTE**: For the purposes of double-blind review, we have kept the repository private and temporarily removed the package from PyPI. We apologize for any inconvenience and will republish the package once the review process is complete.

---

[![PyPI - Version](https://img.shields.io/pypi/v/im2im.svg)](https://pypi.org/project/im2im/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/im2im)](https://pypi.org/project/im2im/)
[![Downloads](https://static.pepy.tech/badge/im2im)](https://pepy.tech/project/im2im)
[![Tests](https://github.com/c3di/im2im/actions/workflows/python%20tests%20with%20coverage.yml/badge.svg)](https://github.com/c3di/im2im/actions/workflows/python%20tests%20with%20coverage.yml)
[![codecov](https://codecov.io/github/c3di/im2im/graph/badge.svg?token=BWBXANX8W7)](https://codecov.io/github/c3di/im2im)

The `im2im` package provides an automated approach for converting in-memory image representations across a variety of image processing libraries, including `scikit-image`, `opencv-python`, `scipy`, `PIL`, `Matplotlib.plt.imshow`, `PyTorch`, `Kornia` and `Tensorflow`. It handles the nuances inherent to each library's image representation, such as data formats (numpy arrays, PIL images, torch tensors, and so on), color channel (RGB or grayscale), channel order (channel first or last or none), device (CPU/GPU), and pixel intensity ranges.

**We aim to identify the conversion code that minimizes information loss and requires the fewest conversion steps, prioritizing CPU execution while applying a configurable penalty for GPU operations. Both the search function and GPU penalty can be adjusted to suit different scenarios.**

Im2im was developed for the use in Visual Programming Language (VPLs) for image processing to completely removes the conversions steps required to manually manage image transformations, drastically improving accessibility, specifically for non-expert users. It also addresses the tension between low-level implementation details necessary for compatibility and the high-level image processing operations that VPLs aim to provide. However, the library is a conventional Python package, and as such, it can also be used by directly invoking its functions from any Python image processing program to automate image conversion steps. Considering the relatively low memory footprint and computational overhead of the system, using the library to simplify conventional Python programming is an interesting option as well. 


## Installation

**NOTE**: For the purposes of double-blind review, we have kept the repository private and temporarily removed the package from PyPI. 
We recommend downloading the package from the "dist" folder and installing it using the following command:
```python
pip install /path_to/im2im-0.0.5-py3-none-any.whl
```

~~Install the package via pip:~~

```bash
pip install im2im
```


## Usage

```python
import numpy as np
from im2im import Image, im2im

# Assume an image that is a numpy.ndarray with shape (20, 20, 3) in uint8 format
to_be_converted = np.random.randint(0, 256, (20, 20, 3), dtype=np.uint8)

# Convert the image using the input preset "numpy.rgb_uint8" for the source image and "torch.gpu" for the target image.
converted: Image = im2im(Image(to_be_converted, "numpy.rgb_uint8"), "torch.gpu")
# Access the converted image data via 'converted.raw_image', which is now a torch tensor with shape (1, 3, 20, 20),
# in float32 format, normalized to the range [0, 1], and transferred to the GPU.

# the underlying conversion uses the following code:
# from PIL import Image
# from torchvision.transforms import functional as F
# image = Image.fromarray(source_image)
# image = F.to_tensor(image)
# image = image.unsqueeze(0)
# target_image = image.cuda()'

# We aim to identify the conversion code that minimizes information loss and requires the fewest conversion steps, prioritizing CPU execution while applying a configurable penalty for GPU operations. Both the search function and GPU penalty can be adjusted to suit different scenarios.**
```

For other APIs like `im2im_code`, please refer to [public APIs](https://github.com/c3di/im2im/blob/main/src/im2im/api.py). 

For integration to visual programming language, please refer to [Comparative Analysis](https://github.com/c3di/im2im/blob/main/comparative_analysis).

## Evaluation

**Comparative Analysis**
We developed two VPLs: one base VPL that directly integrates functions from multiple sources and the same VPL enhanced by our im2im library. The source code are available in [Comparative Analysis](https://github.com/c3di/im2im/blob/main/comparative_analysis). For detailed comparisons, please refer to the following studies: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1E0Sgrb2CrUkoXVv9bcUWvnbLNJ5i-DF4?usp=sharing), [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ILMiCqwrJ-zRHzDp0e3IL7fOcvamrGYS?usp=sharing) and [third study](https://github.com/c3di/im2im/blob/main/comparative_analysis/3/Implementation_Comparison.pdf).

**Accuracy**
All conversion code snippets are thoroughly verified through [execution checks](https://github.com/c3di/im2im/blob/main/tests/test_conversion_code_in_kg.py) to ensure their correctness.

**Performance Benchmark**
Please refer to [benchmark](https://github.com/c3di/im2im/blob/main/benchmark) folder.

## Contribution

We welcome all contributions to this project! If you have suggestions, feature requests, or want to contribute in any other way, please feel free to open an issue or submit a pull request. For detailed instructions on developing, building, and publishing this package, please refer to the [README_DEV](https://github.com/c3di/im2im/blob/main/README_Dev.md).

## Cite

Todo

## License

This project is licensed under the MIT License. See the LICENSE file for details.
