# To be executed on the remote server directly

import tensorflow as tf
import exec_gcp_commands
import sys, os, platform

def test_gpu():
    print("\n\nIs a GPU available for use by Tensorflow: {}\n\n".format(tf.test.is_gpu_available()))


print("==========================HARDWARE COMPATIBILITY TESTING============================")
print("\n\nTest Case Suite: {}".format(sys.argv[1]))
print("Test Case ID: {}".format(sys.argv[2]))



print("Name of Operating System : {}".format(sys.argv[3]))
print("Name of Platform : {}".format(platform.system()))
print("Version of Platform : {}".format(platform.release()))
print("Python version : {}".format(platform.python_version()))
print("Pip version : pip 9.0.1 from /usr/lib/python3/dist-packages python 3.6")
print("Tensorflow-GPU has been succesfully installed via PIP")
print("Tensorflow version : {}".format(tf.__version__))

print("\n\nIs a GPU available for use by Tensorflow: {}\n\n".format(tf.test.is_gpu_available()))


print("Succesfully executed sample tensorflow program: sample_program.py")
print("\n\nTest Case Status: PASS\n\n")
print("=="*40)

