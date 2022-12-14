import math
import scipy.optimize as opt
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, isShow, isSave : bool, savePath : str):
        self.isSave = isSave
        self.isShow = isShow
        self.savePath = savePath
        return

    def plotInputDatas(self, data, data2):

        data_n = [i + 1 for i in range(len(data))]
        plt.plot(data_n, [d[0]  for  d in data], 'C0', label='Ch1_500nm_2mm.csv')
        plt.legend()
        plt.title('Experiment data')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'input_PR1.png')
        plt.show()
        plt.figure()

        plt.plot(data_n, [ed[0] for ed in data2], 'C1', label='Ch2_500nm_2mm.csv')
        plt.legend()
        plt.title('Experiment data')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'input_PR2.png')
        plt.show()
        plt.figure()

        plt.plot(data_n, [data[i][0] for i in range(len(data))], label='Ch1_500nm_2mm.csv')
        plt.plot(data_n, [data2[i][0] for i in range(len(data2))], label='Ch2_500nm_2mm.csv')
        plt.legend()
        plt.title('Experiment data ch1 and ch2')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'input_1_2.png')
        plt.show()
        plt.figure()
        return

    def plotIntervals(self, data , data2, eps ):
        intervals = [[d[0] - eps, d[0] + eps] for d in data]
        eIntervals = [[d[0] - eps, d[0] + eps] for d in data2]

        for i in range(len(intervals)):
            if i == 0:
                plt.vlines(i + 1, intervals[i][0], intervals[i][1], 'C0', lw=1, label = "$I_1$")
            else:
                plt.vlines(i + 1, intervals[i][0], intervals[i][1], 'C0', lw=1)

        plt.legend()
        plt.title('Ch1 data intervals')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'intervals_PR1.png')
        plt.show()
        plt.figure()

        for i in range(len(eIntervals)):
            if i == 0:
                plt.vlines(i + 1, eIntervals[i][0], eIntervals[i][1], 'C1', lw=1, label = "$I_2$")
            else:
                plt.vlines(i + 1, eIntervals[i][0], eIntervals[i][1], 'C1', lw=1)

        plt.legend()
        plt.title('Ch2 data intervals')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'intervals_PR2.png')
        plt.show()
        plt.figure()
        return

    def plotLinearRegression(self, data , tau, w, eData, eTau, eW, eps : float):

        intervals = [[data[i][0] - eps * w[i], data[i][0] + eps * w[i]] for i in range(len(data))]
        eIntervals = [[eData[i][0] - eps * eW[i], eData[i][0] + eps * eW[i]] for i in range(len(eData))]
        for i in range(len(intervals)):
            if i == 0:
                plt.vlines(i + 1, intervals[i][0], intervals[i][1], 'C0', lw=1, label = "$I_1$")
            else:
                plt.vlines(i + 1, intervals[i][0], intervals[i][1], 'C0', lw=1)

        plt.plot([1, len(intervals)], [1 * tau[1] + tau[0], len(intervals) * tau[1] + tau[0]], color='green', label = "$Lin_1$")
        plt.legend()
        plt.title('Ch1 data intervals')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'lr_1.png')
        plt.show()
        plt.figure()

        for i in range(len(eIntervals)):
            if i == 0:
                plt.vlines(i + 1, eIntervals[i][0], eIntervals[i][1], 'C1', lw=1, label = "$I_2$")                
            else:
                plt.vlines(i + 1, eIntervals[i][0], eIntervals[i][1], 'C1', lw=1)
        
        plt.plot([1, len(eIntervals)], [1 * eTau[1] + eTau[0], len(eIntervals) * eTau[1] + eTau[0]], color='green', label = "$Lin_1$")
        plt.legend()
        plt.title('Ch2 data intervals')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'lr_2.png')
        plt.show()
        plt.figure()
        return

    def plotHystW(self, w , eW):

        plt.hist(w, bins=10, label="$w_1$", color='C0')
        plt.legend()
        plt.title('$w_1$ histogram')
        plt.savefig(self.savePath + 'whyst_PR1.png')
        plt.show()
        plt.figure()

        plt.hist(eW, bins=10, label="$w_2$", color='C1')
        plt.legend()
        plt.title('$w_2$ histogram')
        plt.savefig(self.savePath + 'whyst_PR2.png')
        plt.show()
        plt.figure()
        return

    def plotFixedHyst_Intervals(self, data , tau, w , eData , eTau , eW , eps):

        intervals = [[data[i][0] - eps * w[i], data[i][0] + eps * w[i]] for i in range(len(data))]
        eIntervals = [[eData[i][0] - eps * eW[i], eData[i][0] + eps * eW[i]] for i in range(len(eData))]

        dataFixed = [[intervals[i][0] - tau[1] * (i + 1), intervals[i][1]  - tau[1] * (i + 1)] for i in range(len(data))]
        eDataFixed = [[eIntervals[i][0] - eTau[1] * (i + 1), eIntervals[i][1]  - eTau[1] * (i + 1)] for i in range(len(data))]
        # plotFixedHyst
        self.plot_interval_hist(dataFixed, "C0", "$I_1^c$")
        plt.legend()
        plt.title('$I_1^c$ histogram')
        plt.savefig(self.savePath + 'fhyst_PR1.png')
        plt.show()
        plt.figure()

        self.plot_interval_hist(eDataFixed, "C1", "$I_2^c$")
        plt.legend()
        plt.title('$I_2^c$ histogram')
        plt.savefig(self.savePath + 'fhyst_PR2.png')
        plt.show()
        plt.figure()

        for i in range(len(dataFixed)):
            plt.vlines(i + 1, dataFixed[i][0], dataFixed[i][1], 'C0', lw=1)

        plt.plot([1, len(dataFixed)], [tau[0], tau[0]], color='green', label = "$Lin_1$")
        plt.legend()
        plt.title('Data without linear drifting')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'fixed_PR1.png')
        plt.show()
        plt.figure()

        for i in range(len(eDataFixed)):
            plt.vlines(i + 1, eDataFixed[i][0], eDataFixed[i][1], 'C1', lw=1)

        plt.plot([1, len(eIntervals)], [eTau[0], eTau[0]], color='green', label = "$Lin_1$")
        plt.legend()
        plt.title('Data without linear drifting')
        plt.xlabel('n')
        plt.ylabel('mV')
        plt.savefig(self.savePath + 'fixed_PR2.png')
        plt.show()
        plt.figure()
        return

    def plot_interval_hist(self, x : list, color='b', label1=""):
        min_value = x[0][0]
        max_value = x[-1][1]
        step = 0.0001
        bins = [min_value + step * i for i in range(math.ceil((max_value - min_value) / step))]
        hist = [(t[1] + t[0]) / 2 for t in x]
        cur_value = 0

        plt.hist(hist, color = color, label = label1)
        return

    def plotJK(self, data, tau, w, eData, eTau, eW, eps):

        intervals = [[data[i][0] - eps * w[i], data[i][0] + eps * w[i]] for i in range(len(data))]
        eIntervals = [[eData[i][0] - eps * eW[i], eData[i][0] + eps * eW[i]] for i in range(len(eData))]

        dataFixed = [[intervals[i][0] - tau[1] * (i + 1), intervals[i][1] - tau[1] * (i + 1)] for i in
                         range(len(data))]
        eDataFixed = [[eIntervals[i][0] - eTau[1] * (i + 1), eIntervals[i][1] - eTau[1] * (i + 1)] for i in
                          range(len(data))]
        intervalR = [0.00003 * i + 1 for i in range(10000)]
        jaccars = []

        def countJakkar(R):
            dataNew = [[dataFixed[i][0] * R, dataFixed[i][1] * R] for i in range(len(dataFixed))]
            allData = dataNew + eDataFixed
            min_inc = list(allData[0])
            max_inc = list(allData[0])
            for interval in allData:
                min_inc[0] = max(min_inc[0], interval[0])
                min_inc[1] = min(min_inc[1], interval[1])
                max_inc[0] = min(max_inc[0], interval[0])
                max_inc[1] = max(max_inc[1], interval[1])
            JK = (min_inc[1] - min_inc[0]) / (max_inc[1] - max_inc[0])
            return JK

        for r in intervalR:
            jaccars.append(countJakkar(r))

        optimal_x = opt.fmin(lambda x: -countJakkar(x), 1.0481598517985304)
        print(optimal_x[0])
        print(countJakkar(optimal_x[0]))

        max1 = opt.root(countJakkar, 1.038)
        min1 = opt.root(countJakkar, 1.05)
        print(min1.x, max1.x)

        plt.plot(intervalR, jaccars, label="Jaccard", zorder=1)
        plt.scatter(optimal_x[0], countJakkar(optimal_x[0]), label="optimal point at R=" + str(optimal_x[0]))
        plt.scatter(min1.x, countJakkar(min1.x), label="$min_R$=" + str(min1.x[0]), color="r", zorder=2)
        plt.scatter(max1.x, countJakkar(max1.x), label="$max_R$=" + str(max1.x[0]), color="r", zorder=2)
        plt.legend()
        plt.grid()
        plt.xlabel('$R_{21}$')
        plt.ylabel('Jaccard')
        plt.title('Jaccard vs R')
        plt.savefig(self.savePath + 'jakkar.png')
        plt.show()
        plt.figure()

        dataNew = [[dataFixed[i][0] * optimal_x[0], dataFixed[i][1] * optimal_x[0]] for i in range(len(dataFixed))]
        allData = dataNew + eDataFixed
        self.plot_interval_hist(allData, "C0", "Combined with optimal R")
        plt.legend()
        plt.title('Histogram of combined data with optimal R21')
        plt.savefig(self.savePath + 'jakkar_combined_hist.png')
        plt.show()
        plt.figure()
        return



