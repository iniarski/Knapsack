import pack
import filemaker
import time

def printSize(grd, grdTime, gen, genTime, size):
    print('For', size, 'x', size, ' matrix', sep='')
    print('The greedy algorith took:', grdTime, "s wit resut of ", grd)
    print('The genetic algorith took:', genTime, "s wit resut of ", gen)
    increse = ((gen / grd) - 1) * 100
    print(increse, '% increse')

def main():

    greedyTimes = []
    greedy = []
    geneticTimes = []
    genetic = []


    fm = filemaker.FileMaker(0)
    size = 30

    for i in range(5):
        start = time.time()
        fm.changeSize(size)
        fm.makeFile()
        test = pack.Backpack(fm.filename)
        genetic.append(test.genetic())
        geneticTimes.append(time.time() - start)
        start = time.time()
        greedy.append(test.greedy())
        greedyTimes.append(time.time() - start)

        printSize(greedy[i], greedyTimes[i], genetic[i], geneticTimes[i], size)

        size *= 2

if __name__ == '__main__':
    main()