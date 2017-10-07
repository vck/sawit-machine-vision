# neural nets here

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits

from time import time

digit = load_digits()

x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target, test_size=0.3)

for i in range(10, 1000):
   print("training model with {} hidden layers...".format(i))
   clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(i))
   n0 = time()
   clf.fit(x_train, y_train)
   print("accuracy: {}%".format(round(clf.score(x_test, y_test), 2)*100))
   print("model trained in {} seconds".format(round(time() - n0), 2))
