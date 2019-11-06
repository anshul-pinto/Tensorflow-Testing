import tensorflow as tf

tf.compat.v1.disable_eager_execution()

import sys

print("\n\n============== THREAD TESTING ===========\n\n")
print("Test Suite : {}".format(sys.argv[1]))
print("Test Case : {}".format(sys.argv[2]))



g = tf.Graph()
a = 2
b = 3
c = tf.add(a, b, name='Add')
print(c)

g.clear_collection("aa")

g.create_op()

print("\n\nPASS: Collection-AA has been successfully cleared!\n")
print("="*40)
