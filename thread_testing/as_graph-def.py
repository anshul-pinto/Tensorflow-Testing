import tensorflow as tf
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

proto = g.as_graph_def(add_shapes=True)
print("\n\nPASS: Datatype of return value of as_graph_def() : {}".format(type(proto)))

print("="*40)
