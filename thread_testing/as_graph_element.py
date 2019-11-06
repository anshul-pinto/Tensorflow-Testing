import tensorflow as tf

tf.compat.v1.disable_eager_execution()

import sys

print("\n\n============== THREAD TESTING ===========\n\n")
print("Test Suite : {}".format(sys.argv[1]))
print("Test Case : {}".format(sys.argv[2]))
g = tf.Graph()



g = tf.Graph()
a = 2
b = 3
c = tf.add(a, b, name='Add')
print(c)

proto = g.as_graph_element(c,
    allow_tensor=True,
    allow_operation=True)
print("\n\nPASS: Datatype of return value of as_graph_def() : {}\t : {}".format(type(proto), proto))

print("="*40)
