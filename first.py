BATCH_SIZE = 100
EPOCHS = 100 #number of training epochs
MAX_FILE_SIZE = 3200
lstm_size = 1000


import tensorflow as tf
import os
import sys
from tensorflow.models.rnn import rnn_cell

print("I'm running! Yay!")

## read in the data
fileNamesList = ["data/"+s for s in os.listdir("data/")]
fileNameQueue = tf.train.string_input_producer(fileNamesList, name = "oFileQueue")

reader = tf.WholeFileReader(name = "oReader")
key, value = reader.read(fileNameQueue)

example_decoded = tf.decode_raw(value, tf.uint8, name="oASCIIParser")

# example_split = tf.FIFOQueue(3200, [tf.uint8], name="oSequenceMaker")
# example_split.enqueue(tf.split(0,tf.size(example_decoded)[0],example_decoded))

# print("here")

# with tf.Session() as sess:
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#
#     for i in range(100):
#         example, key = sess.run([example_batch,key_batch])
#         print(example, key)
#
#     coord.request_stop()
#     coord.join(threads)

## set up the network
#execfile("/usr/local/lib/python2.7/site-packages/tensorflow/models/rnn/rnn-cell.py")


print(example_decoded.get_shape().as_list()[1])
#shape is not defined yet, and it needs
lstm = rnn_cell.BasicLSTMCell(lstm_size)
state = tf.zeros([1, lstm.state_size])
output, state = lstm(example_decoded, state)
print(output)

## train
