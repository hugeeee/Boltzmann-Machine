#!/usr/bin/env python

import random

binary = [0, 1]

input_1 = [[-1, -1, -1, -1, -1, 1], [-1, -1, 1, -1, -1, -1], [1, -1, -1, -1, -1, -1]]

examples = 0

def num_examples(_input):
	for i in _input:
		examples += len(i)

def activation(value):
	z = 0
	for i in range(neurons):
		if i != value:
			z += weights[value][i] * net[i]

	return z

print ("Please enter the number of neurons")

user_input = raw_input('--> ') # gets input from the user
net = []
weights = {} # hash to store weights for neurons
dw = {}

x = random.uniform(-1, 1)
round(x, 2)

neurons = int(user_input) # parses the input to an int

for i in range (neurons):
	net.append(0)
#	weights[i] = random.choice(binary)
	weights[i] = [] # init with key mapping to a list
	dw[i] = []
	for x in range (neurons):
		weights[i].append(random.choice(binary))


print "done"

