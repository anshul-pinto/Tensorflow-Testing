import tensorflow as tf
import sys
import threading

print("\n\n============== THREAD TESTING ===========\n\n")
print("Test Suite : {}".format(sys.argv[1]))
print("Test Case : {}".format(sys.argv[2]))


def graph(thread_id):
    print("Thread-{}\t Test Suite : {}".format(thread_id, sys.argv[1]))
    print("Thread-{}\tTest Case : {}".format(thread_id, sys.argv[2]))

    g = tf.Graph()
    a = 2
    b = 3
    c = tf.add(a, b, name='Add')
    print(c)

    proto = g.as_graph_def(add_shapes=True)
    print("\n\nPASS: Datatype of return value of as_graph_def() : {}".format(type(proto)))

    print("="*40)

if __name__ == "__main__": 
    # creating thread 
    print("\n\n============== THREAD TESTING ===========\n\n")

    t1 = threading.Thread(target=graph, args=(1,)) 
    t2 = threading.Thread(target=graph, args=(2,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Both threads are identical!") 
    print("="*40)

