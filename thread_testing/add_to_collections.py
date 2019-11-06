import tensorflow as tf
import sys


print("\n\n============== THREAD TESTING ===========\n\n")
print("Test Suite : {}".format(sys.argv[1]))
print("Test Case : {}".format(sys.argv[2]))
g = tf.Graph()
g.add_to_collection("aa", 1)
val = 1
name = "aa"
# print(g.aa)

print("\n\n Value: {} has been added to Graph-g with name: {}\n\n".format(val, name))
print("="*40)
