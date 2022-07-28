from random import randint
import os

class FileMaker:
    def __init__(self, size):
        self.size = size
        self.filename = "packages" + str(size) + ".txt"
        self.fileExists = os.path.exists(self.filename)

    # All the files have stritly defined form
    # 1st line : Data for sizexsize matrix
    # 2nd line : id,width,heigth,value
    # following lines have the values specified in the second line in said order
    # for example line 20
    # 18,4,7,2

    # the Backpack class from pack.py works with .txt files in that form

    def makeFile(self):
        if not self.fileExists:
            with open(self.filename, 'w') as file:
                file.write('Data for ' + str(self.size) + 'x' + str(self.size) + 'matrix\n')
                file.write('id,width,height,value\n')

                packCount = int(self.size * self.size / 20 + randint(-20, 20))

                for i in range(packCount):
                    line = str(i + 1) + ',' + str(randint(1, 10)) + ',' + str(randint(1, 10)) + ',' + str(randint(1, 10)) +'\n'
                    file.write(line)

            file.close()
            self.fileExists = True

    def removeFile(self):
        if self.fileExists:
            os.remove(self.filename)
            self.fileExists = False

    def changeSize(self, size):
        if self.fileExists:
            self.removeFile()

        self.size = size
        self.filename = "packages" + str(size) + ".txt"
        self.fileExists = os.path.exists(self.filename)

    def remakeFile(self):
        if self.fileExists:
            self.removeFile()

        self.makeFile()