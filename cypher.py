'''
Author: Daniel Frederick
Date: November 6, 2018
'''


class Helper:
    def __init__(self):
        self.alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", 'G', 'H', 'I', 'K',
 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z'," ", ",", "."]

    # read file fname and return an array of str for each line
    def readFile(self, fname):
        f = open(fname, 'r')
        ans = []
        '''
        while True:
            x = f.readline()
            print(x)
            if x == '\n':
                break
            ans.append(x)
        '''
        for i in range(0, self.countLines(fname)):
            ans.append(f.readline())
        f.close()
        print('Succesfully read file {}.'.format(fname))
        return ans

    # returns number of lines in a txt file fname
    def countLines(self, fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        f.close()
        return i + 1

    # outputs a file fname with contents arr, returns boolean
    def outputFile(self, fname, arr):
        f = open(fname, 'w')
        for i in arr:
            f.write(i)
        print('Succesfully outputed file {}.'.format(fname))

    # shifts input str key spaces
    def shift(self, str, key):
        arr = list(str)
        ans = ''
        for i in arr:
            if i == '\n':
                ans += i
                continue
            num = self.alp.index(i) + key
            if num >= len(self.alp):
                num = num - len(self.alp)
            char = self.alp[num]
            ans += char
        return ans

    # returns players inout for shift
    def getKey(self):
        while True:
            try:
                k = int(input('Enter desired shift --> '))
                break
            except:
                print('Please enter an integer')

        return k

    def getOFName(self):
        return input('Enter desired output file name --> ') + '.txt'

    def getFName(self):
        return input('Enter desired input file name --> ') + '.txt'


class Encrypt(Helper):
    def __init__(self):
        self.alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", 'G', 'H', 'I', 'K',
 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z'," ", ",", "."]
        fname = self.getFName()
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
    def __init__(self):
        self.alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", 'G', 'H', 'I', 'K',
 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z'," ", ",", "."]
        fname = self.getFName()
        print('Reading contents of {}.'.format(fname))
        fcontents = self.readFile(fname)
        key = -(self.getKey())
        ofname = self.getOFName()
        ncontents = []
        print('Decrypting file {}.'.format(fname))
        for i in fcontents:
            ncontents.append(self.shift(i, key))
        self.outputFile(ofname, ncontents)
        print('File {} outputed.'.format(ofname))


temp = Encrypt()
temp1 = Decrypt()
