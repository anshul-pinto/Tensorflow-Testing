import numpy as np 
import matplotlib.pyplot as plt 
import os
import time
import tensorflow as tf

array_sizes = [100,1000,4000,8000]

#numpy implementation 
numpy_per = []
tf_per = []

for array in array_sizes:
	test_matrix = np.random.random((array,array))

	start = time.time()
	test_result = np.log(test_matrix)
	end = time.time()

	numpy_per.append(end - start)

	tf_input = tf.constant(test_matrix, dtype=tf.float64)

	tf_start = time.time()
	tf_result = tf.compat.v1.log(tf_input)
	tf_end = time.time()

	tf_per.append(tf_end- tf_start)

for i in range(len(array_sizes)):
	print('Size:',array_sizes[i],' numpy performance:', "%.5f" % numpy_per[i],' tensorflow performance:',"%.5f" % tf_per[i])
	#print('tensorflow performance :', tf_per)
plt.figure(figsize = (5,5))
plt.plot(array_sizes,numpy_per,color = 'green', label = 'numpy')
plt.plot(array_sizes, tf_per, color = 'blue', label = 'tensorflow')
plt.title('Tensorflow vs Numpy : Log')
plt.savefig('Log.png')