import tensorflow as tf

#model the network
x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.mul(x1,x2)

# #run the session
# with tf.Session() as sess:
# 	output = sess.run(result)
# 	print(output)
 

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
  with tf.device("/gpu:1"):
    print(sess.run([product]))