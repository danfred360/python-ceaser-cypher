'''
Author: Daniel Frederick
Date: October 18, 2018
'''

import re

class Ceaser:
    def __init__(self):
        self.alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", "."]

    #encrypts a txt file
    class encrypt:
        def __init__(self):
            self.iname = input('Please enter input file to encrypt --> ')
            self.oname = input('Please enter output file for encrypted message --> ')
            self.h = Ceaser().helper()

        #runs all necessary code to encrypt file
        def run(self):
            inArr = self.h.readFile(self.iname)
            self.numArr = self.h.convertStrArrToNumArr(inArr)
            self.process(input('Enter desired shift --> '))

        def process(self, shift):
            ans = []
            for i in self.numArr:
                temp = []
                for j in i:
                    temp.append(int(j) + int(shift))
                ans.append(temp)
            x = self.h.convertNumArrToStrArr(ans)
            print(x)
            return x

    #decrypts a txt file
    class decrypt:
        def __init__(self):
            pass

    #helper methods live here
    class helper:
        def __init__(self):
            pass

        #returns an array of lines from inputed txt file
        def readFile(self, i):
            f = open(i + '.txt', 'r')
            ans = []
            for i in range(0, self.countLines(i)):
                temp = f.readline()
                temp = temp[:len(temp)-3]
                ans.append(temp)
            f.close()
            return ans

        #returns number of lines in a txt file
        def countLines(self, i):
            with open(i + '.txt') as f:
                for i, l in enumerate(f):
                    pass
            f.close()
            return i#+ 1

        #converts an array of characters to numbers
        def convertCharArrToNumArr(self, charArr):
            ans = []
            for i in charArr:
                ans.append(self.findLastIndex(main.alp, i))
            return ans

        def convertNumArrToCharArr(self, numArr):
            ans = []
            for i in numArr:
                ans.append(main.alp[int(i)])
            return ans

        def convertStrArrToCharArr(self, strArr):
            ans = []
            for i in strArr:
                ans.append(list(i))
            return ans

        def convertCharArrToStrArr(self, charArr):
            ans = []
            for i in charArr:
                ans.append(list(i))
            return ans

        #returns last index of x if it's presents, and -1 if it isn't
        def findLastIndex(self, arr, x):
            index = -1
            for i in range(0, len(arr)):
                if arr[i] == x:
                    index = i
            return index
main = Ceaser()

temp = Ceaser().encrypt()
temp.run()
            
