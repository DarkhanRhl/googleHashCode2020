import math
import copy

class Core:
    def __init__(self, booksNumber, librariesNumber, daysNumber, booksScore, librairies):
        self.booksNumber = booksNumber #Number
        self.librariesNumber = librariesNumber #Number
        self.daysNumber = daysNumber #Number
        self.booksScore = booksScore #List of Number
        self.librairies = librairies #List of Object

        for library in self.librairies:
            library["books"] = self.getBooksSortedByScore(library["books"])

        self.days = 0
        self.end = False
        self.banned = []

        self.loop()

    def getBooksSortedByScore(self, books):
        booksScore = [self.booksScore[index] for index in books]
        response = [x for _,x in sorted(zip(booksScore, books))]
        response.reverse()
        return response

    def removeBannedBooks(self, books):
        newBooks = []
        for book in books:
            try:
                self.banned.index(book)
            except ValueError:
                newBooks.append(book)
        return newBooks

    def setScore(self, library):
        library["books"] = self.removeBannedBooks(library["books"])

        daysAvailable = (self.daysNumber - self.days) - library["signUpDays"]
        if daysAvailable <= 0:
            return 
        numberBooksGettable = min(library["booksNumber"], daysAvailable * library["shipCapacity"])
        daysTaken = library["signUpDays"] + math.ceil(numberBooksGettable / library["shipCapacity"])
        
        scores = [self.booksScore[index] for index in library["books"]]
        score = sum(scores[:numberBooksGettable]) / daysTaken
        library["score"] = score

    def getHighestScoreLibrary(self, libraries):
        highestScore = -1
        highestLibrary = {}
        for library in libraries:
            if highestScore == -1 or library['score'] > highestScore:
                highestScore = library['score']
                highestLibrary = library
        return highestLibrary
    
    def addBanedBooks(self, highestLibrary):
        self.banned += highestLibrary["books"]

    def loop(self):
        libraries = copy.copy(self.librairies)
        libraryNb = 0
        usedLibraries = []
        while self.days < int(self.daysNumber):
            for library in libraries:
                self.setScore(library)
            highestLibrary = self.getHighestScoreLibrary(libraries)
            try:
                self.days += int(highestLibrary['signUpDays'])
            except:
                break
            libraryNb += 1
            usedLibraries.append(highestLibrary)
            self.addBanedBooks(highestLibrary)
            libraries.remove(highestLibrary)
        print(libraryNb)
        for library in usedLibraries:
            index = 0
            print(library['index'], len(library['books']))
            for book in library['books']:
                print(book, end='')
                if index == len(library['books']) - 1:
                    print()
                else:
                    print(' ', end='')
                index += 1
