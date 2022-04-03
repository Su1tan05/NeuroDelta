from kinematics import SimulatedDeltaBot
from NeuralNetwork import NeuralNetwork
import numpy as np
import csv

with open('angles.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



neural_network = NeuralNetwork()

training_set_inputs = np.array(angles)
training_set_outputs = X.T
neural_network.train(training_set_inputs, training_set_outputs, 1000)


print ("\nNew synaptic weights (layer 1) after training: ")
print (neural_network.synaptic_weights1)
print ("\nNew synaptic weights (layer 2) after training: ")
print (neural_network.synaptic_weights2)
print ("\nNew synaptic weights (layer 3) after training: ")
print (neural_network.synaptic_weights3)
# test with new input
print ("\nConsidering new situation [1,0,0] -> ?")
print (neural_network.forward_pass(array([1,0,0])))