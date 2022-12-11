import dataManager as dm
import OctaveSolver as ocsol
import Ploater as pltr
import csv
class Solution:

    def __init__(self, filePR1 , filePR2 , fileLR1 , fileLR2 , startCSVOffset , eps , isShow , isSave , savePath):
        self.offset = startCSVOffset
        self.filePR1 = filePR1
        self.filePR2 = filePR2
        self.fileLR1 = fileLR1
        self.fileLR2 = fileLR2
        self.eps = eps
        self.isShow = isShow
        self.isSave = isSave
        self.savePath = savePath
        return

    def loadData(self):
        dataManager= dm.DataManager()
        self.data = dataManager.loadData(self.filePR1, self.offset)
        self.data2 = dataManager.loadData(self.filePR2, self.offset)
        return

    def findOctaves(self):
        octaveSolver = ocsol.LinearSolutionManager()
        self.tau, self.w = octaveSolver.LinearSolution(self.fileLR1)
        self.etalonTau, self.etalonW = octaveSolver.LinearSolution(self.fileLR2)
        return

    def plot(self):
        plotter = pltr.Plotter(self.isShow, self.isSave, self.savePath)
        plotter.plotInputDatas(self.data, self.data2)
        plotter.plotHystW(self.w, self.etalonW)
        plotter.plotIntervals(self.data, self.data2, self.eps)
        plotter.plotLinearRegression(self.data, self.tau, self.w, self.data2, self.etalonTau, self.etalonW, self.eps)
        plotter.plotFixedHyst_Intervals(self.data, self.tau, self.w, self.data2, self.etalonTau, self.etalonW, self.eps)
        plotter.plotJK(self.data, self.tau, self.w, self.data2, self.etalonTau, self.etalonW, self.eps)
        
        return


