"""
Boltzmann Machine
Connectionist Computing Assignment 
Student name: Hugo King-Hall

"""
import random
import math

example_1 = [[-1, -1, -1, -1, -1, 1], [-1, -1, 1, -1, -1, -1], [1, -1, -1, -1, -1, -1]]
input_1 = [[-1, -1, -1, -1, 1, 1], [-1, -1, -1, -1, -1, -1],[ 1, 1, 1, 1, -1, -1]]

example_2 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, 1],[-1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
input_2 = [[-1, -1, 1, -1, 1, -1, -1, -1, -1, 1],[-1, 1, -1, 1, 1, -1, 1, 1, 1, 1]]

class Boltzmann ():

	def __init__(self, neurons, _input, examples, learning_rate, samples, max_flips):
		self.neurons = neurons
		self.examples = examples
		self.input = _input

		self.net = []	# list to store network values
		self.weights = {} # hash to store weights for neurons
		self.dw = {}	# hash to store update for weights

		self.setup()	# init weights to random values		

		self.eta = learning_rate
		self.samples = samples
		self.max_flips = max_flips

	# setup the lists for network, weights and dw
	def setup(self):
		for i in range (self.neurons):
			self.weights[i] = [] # init with key mapping to a list
			self.dw[i] = []
			self.net.append(0)
			for x in range (self.neurons):
				self.weights[i].append(0.2*(random.random()-0.5))
				self.dw[i].append(0.0)

	# use the weights to set the network
	def activation(self, j):
		z = 0
		for i in range(self.neurons):
			if i != j:
				z += self.weights[j][i] * self.net[i]

		return z

	# implementation of learning
	def learning(self):
		for i in range (len(self.examples)):
			for j in range (self.neurons):
				for k in range(self.neurons):
					self.dw[j][k] = self.eta*self.examples[i][j]*self.examples[i][k]
		
		self.dreaming()
	
	# implementation of dreaming
	def dreaming(self):
		for s in range (self.samples):
			for j in range (self.neurons):
				if (random.random() < 0.5):
					self.net[j] = -1
				else:
					self.net[j] = 1
			for q in range (self.max_flips):
				for j in range(self.neurons):
					z = self.activation(j)
					T = 0.1*(self.max_flips-q)/self.max_flips
					try:
						expression = 1/(1+math.exp(-2*z/T))
						rand = random.random()
						if expression > rand:
							#print expression > rand
							self.net[j] = 1
						else:
							self.net[j] = -1
					except OverflowError: # this is a bit bad here. expression could be high but precise
							print "OVERFLOW"
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

machine = Boltzmann(neurons, input_1, example_1, 0.01, 500, 100) # if flips is too high there is an overflow error
# this means the number is too much for a double

output_file = open("weights.txt", "w")
s = ""
for i in range (500):
	machine.learning()

for i in range (5):
	print "Run %i" %i
	for j in range (len(machine.examples)):
		machine.net = machine.input[j]
		machine.dreaming()
		print "Example is %s | Network is %s" %(str(machine.examples[j]), str(machine.net))
		s += "\nRun ============= %i %s" %(i, str(machine.weights))

output_file.write(s)
