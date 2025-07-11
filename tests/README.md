# Tests

**For development, we recommend using Option 1, but for testing the current functionality, Option 2 is more suitable.**



## Option 1: Run the unit tests locally

###  CPU-ONLY Environment

With your Python virtual environment active, install the tests environment
```bash
pip install -r path/to/requirements_cpu.txt
```
In the console, natigate to the root folder of project. Run the unit tests in `tests` folder 
```bash
pytest tests/ --maxfail=1
```
**NOTE: Unit tests required GPU will be skipped  in a CPU-only environment.**


### GPU-ONLY Environment
**Make sure [NVIDIA® GPU drivers](https://www.nvidia.com/drivers), [CUDA® Toolkit 12.3](https://developer.nvidia.com/cuda-toolkit-archive), [cuDNN SDK 8.9.7](https://developer.nvidia.com/cudnn) are installed** for running tensorflow on GPU.
More detailed, please refer to [TensorFlow Installation Guide](https://www.tensorflow.org/install/pip).



With your Python virtual environment active, choose the `requirements_gpu.txt`, 

```bash
pip install -r path/to/requirements_gpu.txt
```

Run the unit tests in `tests` folder
```bash
pytest tests/ --maxfail=1
```

####  QA

Verify the GPU support for Tensorflow in the console:

```bash
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

If empty of devices are returned, check if the environment was specified:

[python 3.x - Cannot dlopen some GPU libraries. Skipping registering GPU devices - Stack Overflow](https://stackoverflow.com/questions/60208936/cannot-dlopen-some-gpu-libraries-skipping-registering-gpu-devices).



## Option 2:  Run the unit tests using docker

Follow the official instructions to set up Docker Engine [Install using the `apt` repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) on ubuntu. Not need to install Docker Desktop.

###  CPU-ONLY Environment

```bash
sudo docker run feichen999/im2im_unit_tests_cpu
```

Docker will pull the image from Docker hub and run locally. **NOTE: Unit tests required GPU will be skipped  in a CPU-only environment.**


### GPU Environment

```bash
sudo docker run --rm --gpus all feichen999/im2im_unit_tests_gpu
```

All unit tests passed.
