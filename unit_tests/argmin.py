import unittest
import numpy as np
import tensorflow as tf
import os

class Test(unittest.TestCase):

    def test_argmin_float32(self):
        success = True
        for _ in range(10):
            # sample input
            batch_size, d1, d2 = map(int, np.random.randint(low=2, high=100, size=3))
            test_input = np.zeros((batch_size, d1, d2), dtype='float32')
            test_input[:] = np.random.randn(*test_input.shape)
            test_axis = np.random.randint(3)

            # evaluate the numpy version
            test_result = np.argmin(test_input,axis = test_axis)

            # evaluate the tensorflow version
            #with tf.Session() as sess:
            tf_input = tf.constant(test_input, dtype=tf.float32)
            tf_axis = tf.constant(test_axis, dtype=tf.int32)
            tf_result = tf.argmin(tf_input, axis = tf_axis)
            #tf_result = sess.run(tf_result)
            
            # check that outputs are similar
            success = success and np.allclose(test_result, tf_result)
        self.assertEqual(success, True)
        print("\n dtype = FLOAT32 , Test Executed! \n")

    def test_argmin_float64(self):
        success = True
        for _ in range(10):
            # sample input
            batch_size, d1, d2 = map(int, np.random.randint(low=2, high=100, size=3))
            test_input = np.zeros((batch_size, d1, d2), dtype='float64')
            test_input[:] = np.random.randn(*test_input.shape)
            #test_input = np.random.random([batch_size, d1, d2])
            test_axis = np.random.randint(3)

            # evaluate the numpy version
            test_result = np.argmin(test_input,axis = test_axis)

            # evaluate the tensorflow version
            #with tf.Session() as sess:
            tf_input = tf.constant(test_input, dtype=tf.float64)
            tf_axis = tf.constant(test_axis, dtype=tf.int32)
            tf_result = tf.argmin(tf_input, axis = tf_axis)
            #tf_result = sess.run(tf_result)
            
            # check that outputs are similar
            success = success and np.allclose(test_result, tf_result)

        self.assertEqual(success, True)
        print("\n dtype = FLOAT64 , Test Executed! \n")


    def test_argmin_int64(self):
        success = True
        for _ in range(10):
            # sample input
            batch_size, d1, d2 = map(int, np.random.randint(low=2, high=100, size=3))
            test_input = np.random.randint(5, size=(batch_size,d1,d2) , dtype= np.int64)
            test_axis = np.random.randint(3)

            # evaluate the numpy version
            test_result = np.argmin(test_input,axis = test_axis)

            # evaluate the tensorflow version
            #with tf.Session() as sess:
            tf_input = tf.constant(test_input, dtype=tf.int64)
            tf_axis = tf.constant(test_axis, dtype=tf.int32)
            tf_result = tf.argmin(tf_input, axis = tf_axis)
            #tf_result = sess.run(tf_result)
            
            # check that outputs are similar
            success = success and np.allclose(test_result, tf_result)

        self.assertEqual(success, True)
        print("\n dtype = INt64 , Test Executed! \n")


if __name__ == '__main__':
    print('============================= START TESTS =============================')
    unittest.main()