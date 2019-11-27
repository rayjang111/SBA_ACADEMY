import tensorflow as tf
import pandas as pd
import numpy as np
with open('data.txt') as file:
    reader=iter(file.readlines())
    header=next(reader)
    header=header.split(' ')
    header.remove('\n')
    print(header)
    lines=[]
    for line in reader:
        line=line.split(' ')
        if '\n' in line:
            line.remove('\n')
        lines.append(line)
    df=pd.DataFrame(data=lines,columns=header)
    df=df.astype(np.float64)
y_true=df['price']
y_mean=df['price'].mean()
y_std=df['price'].std()
df=(df-df.mean())/df.std()
def return_y(y):
    return y*y_std+y_mean
X_train=np.array(df.drop('price',1),dtype=np.float32)
print(X_train.shape)
print(X_train.dtype)
y_train=np.array(df['price'],dtype=np.float32).reshape(-1,1)
y_train=np.vstack(y_train)
print(y_train.shape)
print(y_train.dtype)
W=tf.Variable(tf.random_normal([4,1]),name='weight')
b=tf.Variable(tf.random_normal([1,1]),name='bias')
hypothesis=tf.matmul(X_train,W)+b 
cost=tf.reduce_mean(tf.square(hypothesis-y_train))
optimizer=tf.train.AdamOptimizer(learning_rate=0.01) ###빨라지고 싶으면 learning_rate을 더크게
train=optimizer.minimize(cost)
X=tf.placeholder(tf.float32,shape=[None,4])
Y=tf.placeholder(tf.float32,shape=[None,1])
init=tf.global_variables_initializer()
with tf.Session() as sess:
        sess.run(init)
        for step in range(3001): ###반복회수 30000번 
            cost_val,W_val,b_val,_=sess.run([cost,W,b,train],feed_dict={X:X_train,Y:y_train}) ###실행되어야 하는걸 계속 구해야한다.
            if step%300==0:
                print(step,"번 훈련시켰을때 에러",end=" ")
                print(cost_val)
y_hat=return_y(X_train.dot(W_val)+b_val)
y_hat=np.hstack(y_hat)
dic={"훈련을 통해 구한 예측값":y_hat,"실제값":y_true}
print(pd.DataFrame(dic))

        
