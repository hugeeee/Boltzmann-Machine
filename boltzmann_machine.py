#!/usr/bin/env python

import random

input_1 = [[-1, -1, -1, -1, -1, 1], [-1, -1, 1, -1, -1, -1], [1, -1, -1, -1, -1, -1]]
input_2 = [[-1, -1, -1, -1, 1, 1], [-1, -1, -1, -1, -1, -1],[ 1, 1, 1, 1, -1, -1]]
input_3 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, 1],[-1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
input_4 = [[-1, -1, 1, -1, 1, -1, -1, -1, -1, 1],[-1, 1, -1, 1, 1, -1, 1, 1, 1, 1]]

class Boltzmann ():

	def __init__(self, neurons, examples, learning_rate):
		self.neurons = neurons
		self.examples = examples
		self.net = []
		self.weights = {} # hash to store weights for neurons
		self.dw = {}
		self.setup_weights()	# init weights to random values
		self.P = len(self.examples)
		self.eta = learning_rate

	def activation(j):
		z = 0
		for i in range(neurons):
			if i != j:
				z += self.weights[j][i] * self.net[i]

		return z

	def setup_weights(self):
		for i in range (self.neurons):
			self.weights[i] = [] # init with key mapping to a list
			self.dw[i] = []
			for x in range (self.neurons):
				self.weights[i].append(0.2*(random.random()-0.5))
				self.dw[i].append(0.0)

	def learning():
		for i in (self.P):
			for j in (self.neurons):
				for k in (self.neurons):
					dw[j][k] = self.eta*self.examples[i][j]*self.examples[i][k]


print ("Please enter the number of neurons")

user_input = raw_input('--> ') # gets input from the user
neurons = int(user_input) # parses the input to an int

machine = Boltzmann(neurons, input_1, 0.01)

print "done"

print machine.weights
