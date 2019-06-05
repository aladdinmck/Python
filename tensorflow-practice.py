# I've created this in order 
# to learn tensorflow briefly

# Python script using TensorFlow
# for multiplying two arrays 

# import 'tensorflow'
import tensorflow as tf

# initialize two constants
x1 = tf.constant([1, 2, 3, 4])
x2 = tf.constant([5, 6, 7, 8])

# multiply 
result = tf.multiply(x1, x2)

# initialize the session
sess = tf.Session()

# print the result
print(sess.run(result))

# close the session
sess.close()
