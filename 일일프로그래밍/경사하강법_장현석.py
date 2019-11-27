from numpy import *
import random
def standRegres(xArr,yArr):
    xMat=mat(xArr); yMat=mat(yArr).T
    xTx=xMat.T*xMat
    if linalg.det(xTx)==0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws=xTx.I*(xMat.T*yMat)
    return ws
def gradient_Regres(xArr,yArr,learning_rate=0.01):
    a=random.gauss(0,1)
    b=random.gauss(0,1)
    while True:
        for i in range(len(yArr)):
            data=xArr[i]
            y_hat=data[0]*b+data[1]*a
            y=yArr[i]
            loss=(y-y_hat)*(y-y_hat)
            gradient_b=2*(y-y_hat)*(-data[0])
            gradient_a=2*(y-y_hat)*(-data[1])
            a-=gradient_a*learning_rate
            b-=gradient_b*learning_rate
        if loss<0.0001:
            return b,a
            break
xArr=[[1,0],[1,1],[1,2],[1,3],[1,4]] ###y=7+2x 식에서 샘플을 가져옴
yArr=[7,9,11,13,15]
print('OLS를 통한 추정값',standRegres(xArr,yArr))
print("Gradient descent algorithm을 통한 추정값:",gradient_Regres(xArr,yArr))
