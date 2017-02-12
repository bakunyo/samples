# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time

import numpy as np
import tensorflow as tf
import matplotlib.pylab as plt

import cifar10_model as model
from cifar10_reader import Cifar10Reader

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer('epoch', 30, "訓練するEpoch数")
tf.app.flags.DEFINE_string('data_dir', './data/', "訓練データのディレクトリ")
tf.app.flags.DEFINE_string('checkpoint_dir', './checkpoints/',
                          "チェックポイントを保存するディレクトリ")

filenames = [
  os.path.join(
    FLAGS.data_dir,'data_batch_%d.bin' % i) for i in range(1, 6)
  ]

def _loss(logits, label):
  labels = tf.cast(label, tf.int64)
  cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
    logits, labels, name='cross_entropy_per_example')
  cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
  return cross_entropy_mean


def _train(total_loss, global_step):
  opt = tf.train.GradientDescentOptimizer(learning_rate=0.001)
  grads = opt.compute_gradients(total_loss)
  train_op = opt.apply_gradients(grads, global_step=global_step)
  tf.summary.scalar("loss", total_loss)

  return train_op

filenames = [
  os.path.join(
    FLAGS.data_dir,'data_batch_%d.bin' % i) for i in range(1, 6)
  ]


def main(argv=None):
  global_step = tf.Variable(0, trainable=False)
  
  train_placeholder = tf.placeholder(tf.float32,
                                     shape=[32, 32, 3],
                                     name='input_image')
  label_placeholder = tf.placeholder(tf.int32, shape=[1], name='label')
  
  # (width, height, depth) -> (batch, width, height, depth)
  image_node = tf.expand_dims(train_placeholder, 0)
  
  logits = model.inference(image_node)
  total_loss = _loss(logits, label_placeholder)

  train_op = _train(total_loss, global_step)

  summary = tf.summary.merge_all()

  with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    total_duration = 0

    writer = tf.summary.FileWriter('./tensorflow_log', sess.graph)
    summary_i = 0
    
    for epoch in range(1, FLAGS.epoch + 1):
      start_time = time.time()
      
      for file_index in range(5):
        print('Epoch %d: %s' % (epoch, filenames[file_index]))
        reader = Cifar10Reader(filenames[file_index])

        for index in range(10000):
          if index % 100 == 0:
            accurancy = 0.0
            accurate_count = 0
            accurate_tried_count = 0

          image = reader.read(index)
          
          _, loss_value, logits_value = sess.run(
            [train_op, total_loss, logits],
            feed_dict={
              train_placeholder: image.byte_array,
              label_placeholder: image.label
            })

          accurate_tried_count += 1
          result = np.argmax(logits_value, 1)
          if ("%d" % image.label) == ("%d" % result):
            accurate_count += 1

          assert not np.isnan(loss_value), \
            'Model diverged with loss = NaN'

          if index % 100 == 99:
            print('[%d]: %r' % (image.label, logits_value))
            print('Inference: %r' % result)
            accurancy = accurate_count / accurate_tried_count
            print('Accurancy: %f' % accurancy)
            summary_i += 1
            summary_str = sess.run(summary,
                feed_dict={
                train_placeholder: image.byte_array,
                label_placeholder: image.label
              })

            writer.add_summary(summary_str, summary_i)
            writer.flush()

        reader.close()

      duration = time.time() - start_time
      total_duration += duration
    
    print('Total duration = %d sec' % total_duration)

if __name__ == '__main__':
  tf.app.run()
