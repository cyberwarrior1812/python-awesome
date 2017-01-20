#!python3
import pybrain
from pybrain.tools.shortcuts import buildNetwork

aspects = {'age' : 1,'height' : 2, 'weight' : 30 }

#net = buildNetwork(aspects['age'], aspects['height'], aspects['weight'])
net = buildNetwork(2,3,1)
print net.activate([3,1])

