#!/usr/bin/env python

print ("Please enter the number of neurons")

user_input = raw_input('--> ') # gets input from the user
neuron_values = []

neurons = int(user_input) # parses the input to an int

for i in range (0, neurons):
	print i
	neuron_values.append(0)

print "done"

for i in range (len(neuron_values)):
	print neuron_values[i]


