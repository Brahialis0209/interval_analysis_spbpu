import dataManager as dm
import numpy as np


class LinearSolutionManager:
    def LinearSolution(self, fileName : str):
        tau = list()
        w = list()
        with open(fileName) as file:
            tau = [float(t) for t in file.readline().split()]
            for line in file.readlines():
                w.append(float(line))
        return tau, w
