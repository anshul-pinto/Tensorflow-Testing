import tensorflow as tf
import sys
import threading

def graph(thread_id, graph_obj):
    print("Thread-{}\t Test Suite : {}".format(thread_id, sys.argv[1]))
    print("Thread-{}\tTest Case : {}".format(thread_id, sys.argv[2]))

    g = tf.Graph()
    g.add_to_collection("aa", 1)
    val = 1
    name = "aa"
    # print(g.aa)

    print("\n\n Value: {} has been added to Graph-g with name: {}\n\n".format(val, name))



if __name__ == "__main__": 
    # creating thread 
    print("\n\n============== THREAD TESTING ===========\n\n")
    g = tf.Graph()

    t1 = threading.Thread(target=graph, args=(1, g,)) 
    t2 = threading.Thread(target=graph, args=(2, g,)) 
  
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


