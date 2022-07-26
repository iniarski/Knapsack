import pack
import time


def main():
    # time complexity with regard to size
    greedyTimes = []
    greedy = []
    geneticTimes = []
    genetic = []


    test = pack.Backpack('packages100.txt')

    #for i in range(10):
    #    start = time.time()
    #    greedy.append(test.greedy())
    #    greedyTimes.append(time.time() - start)

    #    start = time.time()
    #    genetic.append(test.genetic())
    #    geneticTimes.append(time.time() - start)

    #    print("Greedy")
    #    print(greedy)
    #    print(greedyTimes)

    #    print("Genetic")
    #    print(genetic)
    #    print(geneticTimes)

    pops = 2

    for i in range(6):
        test.pop = pops
        start = time.time()

        genetic.append(test.genetic())
        geneticTimes.append(time.time() - start)

        pops *= 2

        print(genetic)
        print(geneticTimes)

if __name__ == '__main__':
    main()