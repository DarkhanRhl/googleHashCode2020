import sys

def isInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def isFloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


class Parsing:
    def __init__(self, filepath):
        self.openFile(filepath)
        self.libraries = []
        self.parse()

    def openFile(self, filepath):
        fd = open(filepath)
        self.rawData = fd.read()

    def parse(self):
        lines = self.rawData.split("\n")
        lines = [string for string in lines if string != ""]
        [self.booksNumber, self.librariesNumber, self.daysNumber] = list(map(int, lines[0].split(" ")))
        self.booksScore = list(map(int, lines[1].split(" ")))
        lines = lines[2:]
        for index in range(0, len(lines), 2):
            libraryInfo = lines[index].split(" ")
            self.libraries.append({
                "booksNumber": int(libraryInfo[0]),
                "signUpDays": int(libraryInfo[1]),
                "shipCapacity": int(libraryInfo[2]),
                "books": list(map(int, lines[index + 1].split(" "))),
                "score": 0,
                "index": int(index / 2)
            })

    def getParsing(self):
        return [self.booksNumber, self.librariesNumber, self.daysNumber, self.booksScore, self.libraries]