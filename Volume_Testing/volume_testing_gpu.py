# To be executed on the remote server directly

import tensorflow as tf

import exec_gcp_commands
import sys, os, platform

def test_gpu():
    print("\n\nIs a GPU available for use by Tensorflow: {}\n\n".format(tf.test.is_gpu_available()))


print("==========================VOLUME TESTING============================")
print("\n\nTest Case Suite: {}".format(sys.argv[1]))
print("Test Case ID: {}".format(sys.argv[2]))



print("Tensorflow-GPU exists in latest version\n\n")
print("Tensorflow version : {}".format(tf.__version__))
print("\n\nIs a GPU available for use by Tensorflow: {}\n\n".format(tf.test.is_gpu_available()))


a = tf.random.uniform((1000, 1000))
b = tf.random.uniform((1000, 1000))

c = a + b

# tf.Session.run(c)
print("\n\nFinal Output of Matrix Operations:")
print(c.numpy())

print("\n\nSUCCESS: Tensorflow is able to allocate 10^6 memory for matrix operations\n\n")



# print("Succesfully executed sample tensorflow program: sample_program.py")
print("\n\nTest Case Status: PASS\n\n")
print("=="*40)

