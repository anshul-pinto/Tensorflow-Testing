import unittest
import numpy as np
import tensorflow as tf
import os

class Test(unittest.TestCase):

    def test_atan_float32(self):
        success = True
        for _ in range(10):
            # sample input
            batch_size, d1, d2 = map(int, np.random.randint(low=2, high=100, size=3))
            test_input = np.zeros((batch_size, d1, d2), dtype='float32')
            test_input[:] = np.random.randn(*test_input.shape)

            # evaluate the numpy version
            temp_result = np.tan(test_input)
            test_result = np.arctanh(temp_result)

            # evaluate the tensorflow version
            #with tf.Session() as sess:
            tf_input = tf.constant(temp_result, dtype=tf.float32)
            tf_result = tf.atanh(tf_input)
            #tf_result = sess.run(tf_result)
            
            # check that outputs are similar
            success = success and np.allclose(test_result, tf_result)
        self.assertEqual(success, True)
        print("\n dtype = FLOAT32 , Test Executed! \n")

if __name__ == '__main__':
    print('============================= START TESTS =============================')
    unittest.main()