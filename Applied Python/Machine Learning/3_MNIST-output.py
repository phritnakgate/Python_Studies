import pylab
import matplotlib.pyplot as plt
from sklearn import datasets
digit = datasets.load_digits()
print(digit.target[0])
'''
แสดงผล MNIST โดยใช้ pylab
pylab.imshow(digit.images[0], cmap=pylab.cm.gray_r)
pylab.show()
'''

#แสดงผล MNIST โดยใช้ matplotlib
plt.imshow(digit.images[0], cmap=plt.cm.gray_r)
plt.show()

