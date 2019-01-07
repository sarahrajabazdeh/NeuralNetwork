import numpy as np
class NN:

    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):

        return 1/(1+np.exp(-x))

    def sigmoid_dev(self, x):

        return 1*(1-x)

    def think(self,input):
        input=input.astype(float)
        output=self.sigmoid(np.dot(input, self.synaptic_weights))
        return output

    def training(self, training_input, training_output, training_iter):
        for iteration in range(training_iter):

            # siphon the training data via  the neuron
            output = self.think(training_inputs)

            # error rate for back-propagation
            error = training_outputs - output

            #  weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_dev(output))

            self.synaptic_weights += adjustments

if __name__ == '__main__':
    neuralnetwork=NN()
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])
    training_outputs = np.array([[0, 1, 1, 0]]).T
    neuralnetwork.training(training_inputs, training_outputs, 15000)
    
    print("Ending Weights After Training: ")
    print(neuralnetwork.synaptic_weights)

    user_input_one = str(input("User Input One: "))
    user_input_two = str(input("User Input Two: "))
    user_input_three = str(input("User Input Three: "))

    print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
    print("New Output data: ")
    print(neuralnetwork.think(np.array([user_input_one, user_input_two, user_input_three])))
    print(" it just worked)!")



