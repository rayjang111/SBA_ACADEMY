# Lab 6 Softmax Classifier
import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility
import pandas as pd
import tensorflow as tf
df=pd.read_csv('data-04-zoo.csv')
df_value=df[18:].values
df_columns=df.iloc[:,0][:18]
df_columns=[i.split()[2] for i in df_columns][1:]
df=pd.DataFrame(df_value,columns=df_columns)
x_data=df.values[:,:-1]
y_data=df.values[:,-1]
y_data=pd.get_dummies(y_data).values


X = tf.placeholder("float", [None, 16])
Y = tf.placeholder("float", [None, 7])
nb_classes = 7

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# Cross entropy cost/loss
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
acc = tf.reduce_mean((tf.cast(tf.equal(tf.argmax(hypothesis,1), tf.argmax(Y,1)), dtype=tf.float32)))
# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run([optimizer], feed_dict={X: x_data, Y: y_data})
        a1,a2=sess.run([cost,acc], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step,"번째 ","loss 는 ",a1,"정확도는: ",a2)
