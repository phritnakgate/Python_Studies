from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

#ถ้าไม่กำหนด test size : test 25 และ train 75
x_train,x_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
#ระบุขนาด testset trainset ให้เพิ่ม test_size เช่น test_size=0.2 เป็นต้น