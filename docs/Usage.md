# im2im Usage

## Automatically Convert Image Data in Visual Programming Systems

Take the Blockly visual programming framework as an example.

**Without `im2im`**, the definition for a block (`gaussian_blur`) in the visual programming system:

```javascript
Blockly.Python.forBlock['gaussian_blur'] = function (block) {
  requiredImports.add("from skimage.filters import gaussian");
  // inputs
  var image = Blockly.Python.valueToCode(block, "IMAGE", Blockly.Python.ORDER_NONE) || "None";
  var sigma = block.getFieldValue("SIGMA") || "0.5";
  var resultVar = Blockly.Python.nameDB_.getDistinctName("out_im", Blockly.VARIABLE_CATEGORY_NAME);
  // code without im2im
  var code = `${resultVar} = gaussian(${image}, sigma=${sigma})`;
  // output
  Blockly.Python.definitions_["define_" + resultVar] = code;
  return [`${resultVar}`, Blockly.Python.ORDER_NONE];
};
```

**With `im2im`** for automatic type conversion:

* install the im2im in the execution component of visual programming systems.

* add the im2im config for each operation (one block in the VPL). 

  * Call `im2im()` with a metadata preset (e.g., `'skimage.before_gaussian'`) to convert the input to the image format required by the `gaussian` operation.

  * After the operation, wrap the output in an `Image` instance, providing the appropriate metadata (see `convert_back` below).


```javascript
Blockly.Python.forBlock['gaussian_blur'] = function (block) {
  // inputs as above ...
  // code with im2im
  var convert_to = `in_im1 = im2im(${image}, 'skimage.before_gaussian')`;
  var operation = `e_gaussian_filtered = gaussian(in_im1.raw_image, sigma=${sigma})`;
  var convert_back = `${resultVar} = Image(e_gaussian_filtered, {**in_im1.metadata, 'image_data_type': 'float64(0to1)'})`;
  var code = `${convert_to}\n${operation}\n${convert_back}`;
  // outputs as above...
};
```

For additional implementation examples, see:

* source code `comparative_analysis/1/enhanced_VPL4IP.html` and deployed on CoLab [comparative_analysis_1.ipynb - Colab](https://colab.research.google.com/drive/1cf5M1gOMdMXaRIKsCYalVj99RzMYSy8C?usp=sharing) .
* source code `comparative_analysis/2/enhanced_VPL4IP.html` and deployed on CoLab [comparative_analysis_2.ipynb - Colab](https://colab.research.google.com/drive/1qPPL-IvovlhdKv-_0SjADBSOc60SPZDT?usp=sharing) .

---

## Extend to Other Libraries

`im2im` supports automatic conversion between the image formats of multiple libraries, including:

* `scikit-image`
* `opencv-python`
* `PIL`
* `numpy`
* `PyTorch`
* `TensorFlow`

To use `im2im` with other libraries, follow the same pattern as the example avove:

1. **Call `im2im()`** with the appropriate metadata or preset for the target image format.

   * Built-in presets can be found in [`src/im2im/find_metadata/builtin_preset.py`).
   * Users can also define custom metadata or presets (see API documentation).

2. **Perform the operation** using `.raw_image` of the converted input.

3. **Wrap the output** in an `Image` instance with updated metadata (One example was `convert_back` above)