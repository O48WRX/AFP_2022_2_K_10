import random
import numpy as np


def sigmoid_grindset(z):
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    return sigmoid_grindset(z) * (1 - sigmoid_grindset(z))


def deactivation_sigmoid(z):
    return z * (1.0-z)


class Network:
    # A size definiálja a neurális hálózat méretét
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        # Randomizált bias és súlyokat adunk meg
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def cost_derivative(self, output_activations, y):
        return output_activations - y

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid_grindset(np.dot(w, a) + b)
        return a

    # Sztochasztikus gradiens süllyedés algoritmusa
    def stochastic_gradient_descent(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        training_data = list(training_data)
        samples = len(training_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k + mini_batch_size]  # k-tól k + a paraméter hosszú adathalmmazon dolgozik
                            for k in range(0, samples, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)  # Updateli a mini-batchet az ETA(Estimated Time Of Arrival)-el
            if test_data:
                print(f"Epoch {j}: {self.evaluate(test_data)} / {n_test} "
                      f"Ejtett hibák: {n_test - self.evaluate(test_data)}")
                print(f"Pontosság: {(self.evaluate(test_data) / n_test) * 100}%")
            else:
                print(f"Epoch {j} complete")

    def backwards_propagation(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        # feedforward
        activation = x
        activations = [x]  # aktivált értékeket tárol layererről layerre
        zs = []  # Z vektorokat tárol layerről layerre
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid_grindset(z)
            activations.append(activation)

        # backward pass
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for _layer in range(2, self.num_layers):
            z = zs[-_layer]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-_layer + 1].transpose(), delta) * sp
            nabla_b[-_layer] = delta
            nabla_w[-_layer] = np.dot(delta, activations[-_layer - 1].transpose())
        return nabla_b, nabla_w

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backwards_propagation(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w - (eta / len(mini_batch)) * nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (eta / len(mini_batch)) * nb
                       for b, nb in zip(self.biases, nabla_b)]

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(y[x]) for (x, y) in test_results)
