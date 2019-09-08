import sys
import Math as u
import random as rnd
from Utils import cmDebug as cm

values = []
outcomes = []

#outcomes = [0, 1, 1]


weights = list()


def Configure():
    global values
    global outcomes

    valuesFile = open('values.txt', 'r')
    for line in valuesFile.readlines():
        outcomes.append(int(line[3]))
        val = []
        for char in line:
            if (char == '1' or char =='0'):
                val.append(int(char))
        values.append(val)
    
    try:
        length = len(values[0])
    except TypeError:
        length = len(values)
    for _ in range(0, length):
        weights.append(2 * rnd.random() - 1)

def Add(value):
    
    valuesFile = open('values.txt', 'r')
    for line in valuesFile.readlines():
        if value == line:
            Main()
    
    writeFile = open('values.txt', 'a')
    writeFile.write('\n{}'.format(value))
    values.append([int(value[0]), int(value[1]), int(value[2]), int(value[3]), int(value[4])])

#########   PROGRAM    ################

def Main():

    if (input("Do you wanna test the neural network? ")) == 'y':
        Test()
    

    if input("Do you wanna add another binary number to the values? ") == 'y':
        Add ( input ("Insert {} digit binary number: ".format (len(values[0])) ) )
        Main()


    times = int(input("How many times? "))
    for _ in range (0, times):
        NeuralNetwork()
    NeuralNetwork(Print = 'dev')
    print()


    if input("Again? ") == 'y':
        Main()

def Test():
    _input = input("Insert {} digit binary number: ".format(len(values[0])))
    if _input != '': 
        vals = [[int(_input[0]), int(_input[1]), int(_input[2]), int(_input[3]), int(_input[4])]]
        NeuralNetwork(x = vals, y = [0], Print = 'test', Train = False)

        Test()
    else:
        Main()

def NeuralNetwork(x = values, y = outcomes, Print = '', Train = True):

    global weights
    
    outcome = u.dot(x, weights)
    outcome = u.nonlin(outcome)
    
    if Print == 'test':
        if outcome[0] > .5:
            cm ("My guess is 1", 'green')
        else:
            cm ("My guess is 0", 'green')

    if Print == 'dev':
        cm ('The weights are: {}'.format(weights), 'dev')
        cm ('Expected outcomes: {}'.format(y), 'dev')
        cm ('Actual outcomes: {}'.format(outcome), 'dev')
    
    err = u.add(y, u.mult(outcome, -1))

    #Backpropagation
    dw = u.multMatrix(err, u.nonlin(outcome, True))
    if Train:
        weights = u.add (weights, u.dot(x, dw, t1 = True))





######################################################################################################


if __name__ == '__main__':
    Configure()
    Main()