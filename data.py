from numpy import genfromtxt


images_ = genfromtxt('data_test.csv', delimiter=',')
standards_ = images_[0:3]
