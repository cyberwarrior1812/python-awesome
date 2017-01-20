#!python3
import pybrain
from pybrain.tools.shortcuts import buildNetwork

aspects = {'age' : 2, 'height' : 3, 'weight' : 1 }

net = buildNetwork(aspects['age'], aspects['height'], aspects['weight'])
#net = buildNetwork(2,3,1)
print net.activate([2,3]) # This gives random answers every time the program is run. Why?

