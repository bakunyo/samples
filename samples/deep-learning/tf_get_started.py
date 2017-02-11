import tensorflow as tf
import numpy as np
import matplotlib.pylab as plt

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# 関数を定義
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# 2乗和誤差で損失関数を定義
loss = tf.reduce_mean(tf.square(y - y_data))
# 学習率0.5で調整していく
optimizer = tf.train.GradientDescentOptimizer(0.5)
# 損失関数を最小化する
train = optimizer.minimize(loss)

# 始める前に、tfグローバル変数を初期化する必要があるらしい
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

x_ary = np.empty(201)
w_ary = np.empty(201)
b_ary = np.empty(201)

# Fit the line
for step in range(201):
  sess.run(train)
  x_ary[step] = step
  w_ary[step] = sess.run(W)
  b_ary[step] = sess.run(b)
  if step % 20 == 0:
    print(step, sess.run(W), sess.run(b))

plt.xlabel("x")
plt.plot(x_ary, w_ary)
plt.plot(x_ary, b_ary)
plt.show()

