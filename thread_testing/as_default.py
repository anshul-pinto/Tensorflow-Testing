import tensorflow as tf
import sys

print("\n\n============== THREAD TESTING ===========\n\n")
print("Test Suite : {}".format(sys.argv[1]))
print("Test Case : {}".format(sys.argv[2]))
# 1. Using Graph.as_default():
g = tf.Graph()
with g.as_default():
  c = tf.constant(5.0)
  assert c.graph is g

# 2. Constructing and making default:
with tf.Graph().as_default() as g:
  c = tf.constant(5.0)
  assert c.graph is g

print("\n PASS: All local variables within context manager refer to same default graph")


print("\n\n PASS : Default graphs are identical \n\n".format(g.finalized))
print("="*40)
