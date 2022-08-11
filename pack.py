import math
import random


class Backpack:
    def __init__(self, file):

        with open(file) as f:
            lines = f.readlines()

        title = lines[0]

        xMark = title.find('x')
        numLen = 1
        while title[xMark+numLen] in '1234567890':
            numLen += 1

        self.size = int(title[xMark + 1 : xMark + numLen])

        lines = lines[2:]

        self.packNum = len(lines)
        self.packs = [None] * self.packNum

        for i in range(self.packNum):
            lines[i] = lines[i].split(',')
            self.packs[i] = (int(lines[i][1]), int(lines[i][2]), int(lines[i][3][:-1]))

        # parameters
        self.noPrint = True
        # number of instances per generation
        self.pop = 16
        # number of generations
        self.gen = 8

    def greedy(self):

        # the greedy algorith tries to fit the most valued package

        board = self.size * [None]
        for i in range(self.size):
            board[i] = self.size * [-1]

        packages = [* range(self.packNum)]
        obj = self.packNum * [0]
        sum = 0

        for i in range(self.packNum):
            obj[i] = self.packs[i][2] / (self.packs[i][0] * self.packs[i][1])

        while bool(obj):
            notin = True
            skip = 0

            ind = obj.index(max(obj))

            if self.packs[ind][0] > self.packs[ind][1]:
                bigg = self.packs[ind][0]
                smal = self.packs[ind][1]
            else:
                smal = self.packs[ind][0]
                bigg = self.packs[ind][1]

            skip = 0

            for i in range(self.size - smal):
                if notin:
                    for j in range(self.size - smal):

                        if skip == 0 and notin:
                            empty = True
                            for k in range(i, i + smal):
                                for l in range(j + smal, j, -1):
                                    if board[k][l] != -1:
                                        empty = False
                                        skip = l - j
                                        break
                                if not empty:
                                    break
                            if empty:
                                if self.size - i > bigg:
                                    for k in range(i + smal, i + bigg):
                                        for l in range(j, j + smal):
                                            if board[k][l] != - 1:
                                                empty = False
                                                break
                                        if not empty:
                                            break
                                    if empty:
                                        for k in range(i, i + bigg):
                                            for l in range(j, j + smal):
                                                board[k][l] = ind

                                        sum += self.packs[ind][2]
                                        notin = False
                                    empty = True
                                if notin and self.size - j > bigg:
                                    for k in range(i, i + smal):
                                        for l in range(j + smal, j + bigg):
                                            if board[k][l] != -1:
                                                empty = False
                                                break
                                        if not empty:
                                            break

                                    if empty:
                                        for k in range(i, i + smal):
                                            for l in range(j, j + bigg):
                                                board[k][l] = ind

                                        sum += self.packs[ind][2]
                                        notin = False

                        else:
                            skip -= 1
                else:
                    break

            obj.pop(ind)
            packages.pop(ind)

        if not self.noPrint:
            for i in range(self.size):
                for j in board[i]:
                    if j != -1:
                        print(j % 10, end='')
                    else:
                        print(-1, end='')
                print()

        return sum

    def randomize(self, value):
        sigmoid = math.erf(random.random() - 0.5) / 8
        return value * sigmoid + value

    def genetic(self):

        # the genetic alogrith make a list of preferences
        # every generation new speciments will have sligthly changed preferences
        # after every generation has a chance to solve the problem the bottom performing half will be terminated
        # while the top performing half will have offsprings, again with sligthly changed preferences

        default = self.packNum * [0]

        for i in range(self.packNum):
            default[i] = self.packs[i][2] / (self.packs[i][0] * self.packs[i][1])

        population = []

        for i in range(self.pop):
            obj = self.packNum * [0]
            for j in range(self.packNum):
                obj[j] = self.randomize(default[j])
            population.append(obj)

        best = 0
        bestBoard = 0

        for g in range(self.gen):
            results = []
            saved = []

            for p in range(self.pop):

                sum = 0
                board = self.size * [None]
                packages = [* range(self.packNum)]
                obj = population[p].copy()

                for i in range(self.size):
                    board[i] = self.size * [-1]

                while bool(obj):
                    notin = True
                    skip = 0

                    ind = obj.index(max(obj))

                    if self.packs[ind][0] > self.packs[ind][1]:
                        bigg = self.packs[ind][0]
                        smal = self.packs[ind][1]
                    else:
                        smal = self.packs[ind][0]
                        bigg = self.packs[ind][1]

                    skip = 0

                    for i in range(self.size - smal):
                        if notin:
                            for j in range(self.size - smal):

                                if skip == 0 and notin:
                                    empty = True
                                    for k in range(i, i + smal):
                                        for l in range(j + smal, j , -1):
                                            if board[k][l] != -1:
                                                empty = False
                                                skip = l - j
                                                break
                                        if not empty:
                                            break
                                    if empty:
                                        if self.size - i > bigg:
                                            for k in range(i + smal, i + bigg):
                                                for l in range(j, j + smal):
                                                    if board[k][l] != - 1:
                                                        empty = False
                                                        break
                                                if not empty:
                                                    break
                                            if empty:
                                                for k in range(i, i + bigg):
                                                    for l in range(j, j + smal):
                                                        board[k][l] = ind

                                                sum += self.packs[ind][2]
                                                notin = False
                                            empty = True
                                        if notin and self.size - j > bigg:
                                            for k in range(i, i + smal):
                                                for l in range(j + smal, j + bigg):
                                                    if board[k][l] != -1:
                                                        empty = False
                                                        break
                                                if not empty:
                                                    break

                                            if empty:
                                                for k in range(i, i + smal):
                                                    for l in range(j, j + bigg):
                                                        board[k][l] = ind

                                                sum += self.packs[ind][2]
                                                notin = False

                                else:
                                    skip -= 1
                        else:
                            break

                    packages.pop(ind)
                    obj.pop(ind) 

                    
                    # if the package did not fit remove all the packages with greater or equal size
                    if notin:
                        for i in range(len(packages) - 1, -1, -1):
                            p = packages[i]
                            if self.packs[p][0] >= smal and self.packs[p][1] >= smal:
                                if self.packs[p][0] >= bigg or self.packs[p][1] >= bigg:
                                    packages.pop(i)
                                    obj.pop(i) 

                results.append(sum)
                if not self.noPrint:
                    saved.append(board)

            if max(results) > best:
                best = max(results)
                if not self.noPrint:
                    bestBoard = saved[results.index(max(results))]

            if g != self.gen - 1:
                for i in range(self.pop // 2):
                    popIndex = results.index(min(results))
                    results.pop(popIndex)
                    population.pop(popIndex)

                for i in range(self.pop // 2):
                    newObj = self.packNum * [0]
                    for j in range(self.packNum):
                        newObj[j] = self.randomize(population[i][j])

                    population.append(newObj)

        if not self.noPrint:
            for i in range(self.size):
                for j in bestBoard[i]:
                    if j != -1:
                        print(j % 10, end='')
                    else:
                        print(' ', end='')
                print()

        return best