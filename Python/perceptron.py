import numpy as np
# import matplotlib.pyplot as plt
import argparse


class Perceptron:

    def __init__(self, dataset: np.array, eta: float, threshold: float = 1e-3):
        self.dataset = dataset

        self.eta = eta
        self.threshold = threshold
        self.weights = np.random.uniform(-0.5, 0.5, self.dataset.shape[1])

        self.train()

    def f(self, net: np.float):
        if (net >= 0.5):
            return 1
        return 0

    def train(self):

        E2 = self.threshold + 1

        while(E2 > self.threshold):
            for index, value in enumerate(self.dataset):
                row = np.append(value[:-1], 1)
                net = np.sum(row * self.weights)  # Product
                y_obtained = self.f(net)

                E = (value[-1] - y_obtained)  # E = y - ŷ

                E2 += E**2

                dE2 = E * (-row)  # Descending gradient

                self.weights -= self.eta * dE2  # w(t+1) = w(t) - eta * dE²/dw

            E2 /= len(self.dataset)
            print("Error: %.2f" % E)

    def test(self, x: list):
        # x1w1 + x2w2 + theta
        return self.f(np.sum(np.append(x, 1) * self.weights))

    def plot(self, data: list):
        pass


# LOCIG AND EXAMPLE
parser = argparse.ArgumentParser()
parser.add_argument('operation', type=str)
parser.add_argument('test', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()

if(args.operation == "and"):
    input_file = open("./and.txt")
elif(args.operation == "or"):
    input_file = open("./or.txt")

data = np.loadtxt(input_file)

p = Perceptron(data, 0.1)

print(p.test(args.test))
