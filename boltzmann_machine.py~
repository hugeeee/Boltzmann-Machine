"""
Boltzmann Machine
Connectionist Computing Assignment 
Student name: Hugo King-Hall

"""

import random
import math

input_1 = [[-1, -1, -1, -1, -1, 1], [-1, -1, 1, -1, -1, -1], [1, -1, -1, -1, -1, -1]]
input_2 = [[-1, -1, -1, -1, 1, 1], [-1, -1, -1, -1, -1, -1],[ 1, 1, 1, 1, -1, -1]]
input_3 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, 1],[-1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
input_4 = [[-1, -1, 1, -1, 1, -1, -1, -1, -1, 1],[-1, 1, -1, 1, 1, -1, 1, 1, 1, 1]]

class Boltzmann ():

	def __init__(self, neurons, examples, learning_rate, samples, max_flips):
		self.neurons = neurons
		self.examples = examples

		self.net = []	# list to store network values
		self.weights = {} # hash to store weights for neurons
		self.dw = {}	# hash to store update for weights

		self.setup()	# init weights to random values

		self.P = len(self.examples)
		self.eta = learning_rate
		self.samples = samples
		self.max_flips = max_flips

	# use the weights to set the network
	def activation(self, j):
		z = 0
		for i in range(self.neurons):
			if i != j:
				z += self.weights[j][i] * self.net[i]

		return z

	# setup the lists for network, weights and dw
	def setup(self):
		for i in range (self.neurons):
			self.weights[i] = [] # init with key mapping to a list
			self.dw[i] = []
			for x in range (self.neurons):
				self.weights[i].append(0.2*(random.random()-0.5))
				self.dw[i].append(0.0)
				self.net.append(0)

	# implementation of learning
	def learning(self):
		for i in range (self.P):
			for j in range (self.neurons):
				for k in range(self.neurons):
					self.dw[j][k] = self.eta*self.examples[i][j]*self.examples[i][k]

	# implementation of dreaming
	def dreaming(self):
		for i in range (self.samples):
			for j in range (self.neurons):
				if (random.random() < 0.5):
					self.net[j] = -1
				else:
					self.net[j] = 1
			for k in range (self.max_flips):
				for j in range(self.neurons):
					z = self.activation(j)
					T = 0.1*(self.max_flips - k)/ self.max_flips
					if (1 / (1 + math.exp(-2*z/T)) < random.random()):
						self.net[j] = 1
					else:
						self.net[j] = -1
			for j in range (self.neurons):
				for k in range (self.neurons):
					self.dw[j][k] -= self.eta * self.neurons* self.net[j] *self.net[k] / self.samples

# end of class

######################################################
#############	This is the main
####################################################

print ("Please enter the number of neurons")

user_input = raw_input('--> ') # gets input from the user
neurons = int(user_input) # parses the input to an int

machine = Boltzmann(neurons, input_1, 0.01, 500, 100) # if ticks is too high there is an overflow error
# this means the number is too much for a double

for i in range (5000):
	machine.learning()

for i in range (machine.P):
	for j in range (machine.neurons):
		machine.net = machine.examples[i]
		machine.dreaming()

print "Input"
print input_1
print "Network:"
print machine.net
