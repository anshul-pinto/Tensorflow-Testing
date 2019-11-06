import tensorflow as tf
tf.compat.v1.disable_eager_execution()

import sys
import threading

def graph(thread_id):
    print("Thread-{}\t Test Suite : {}".format(thread_id, sys.argv[1]))
    print("Thread-{}\tTest Case : {}".format(thread_id, sys.argv[2]))
    g = tf.Graph()
    a = 2
    b = 3
    c = tf.add(a, b, name='Add')
    print(c)

    proto = g.as_graph_element(c,
        allow_tensor=True,
        allow_operation=True)
    print("\n\nPASS: Datatype of return value of as_graph_def() : {}\t : {}".format(type(proto), proto))

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


