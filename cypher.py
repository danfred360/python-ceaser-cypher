'''
Author: Daniel Frederick
Date: November 6, 2018
'''


class Helper:
    def __init__(self):
        self.alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", "."]

    # read file fname and return an array of str for each line
    def readFile(self, fname):
        f = open(fname)
        ans = []
        while True:
            x = f.readline()
            print(x)
            if x == '/n':
                break
            ans.append(x)
        f.close()
        print('Succesfully read file {}.'.format(fname))
        return ans

    # outputs a file fname with contents arr, returns boolean
    def outputFile(self, fname, arr):
        f = open(fname)
        for i in arr:
            f.write(i)
        print('Succesfully outputed file {}.'.format(fname))

    # shifts input str key spaces
    def shift(self, str, key):
        arr = list(str)
        ans = ''
        for i in arr:
            char = alp[alp.index(i) + key]
            ans += char
        return ans

    # returns players inout for shift
    def getKey(self):
        while True:
            k = input('Enter desired shift --> ')
            if k.isInt():
                break
        return k

    def getOFName(self):
        return input('Enter desired output file name --> ')


class Encrypt(Helper):
    def __init__(self, fname):
        print('Reading contents of {}.'.format(fname))
        fcontents = self.readFile(fname)
        key = self.getKey()
        ofname = self.getOFName()
        ncontents = []
        print('Encrypting file {}.'.format(fname))
        for i in fcontents:
            ncontents.append(self.shift(i, key))
        self.outputFile(ofname, ncontents)
        print('File {} outputed.'.format(ofname))


class Decrypt(Helper):
    def __init__(self, fname):
        fcontents = self.readFile(fname)
        key = -(self.getKey())
        ncontents = self.shift(fcontents, key)


temp = Encrypt('input.txt')
