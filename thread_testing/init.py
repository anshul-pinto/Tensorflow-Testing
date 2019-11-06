import tensorflow as tf
import sys

print("\n\n============== THREAD TESTING ===========\n\n")
print("Test Suite : {}".format(sys.argv[1]))
print("Test Case : {}".format(sys.argv[2]))
g = tf.Graph()
print("\n\nfinalized = {}\t ===> Graph has been initialized - PASS\n\n".format(g.finalized))
print("="*40)
