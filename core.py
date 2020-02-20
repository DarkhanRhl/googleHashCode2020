import math
import copy

class Core:
    def __init__(self, booksNumber, librariesNumber, daysNumber, booksScore, librairies):
        self.booksNumber = booksNumber #Number
        self.librariesNumber = librariesNumber #Number
        self.daysNumber = daysNumber #Number
        self.booksScore = booksScore #List of Number
        self.librairies = librairies #List of Object

        self.actualDay = 0
        self.end = False

        self.loop()

    def getBooksSortedByScore(self, books):
        booksScore = [self.booksScore[index] for index in books]
        response = [x for _,x in sorted(zip(booksScore, books))]
        response.reverse()
        return response

    def setScore(self, library):
        sortedBooks = self.getBooksSortedByScore(library["books"])
        daysAvailable = (self.daysNumber - self.actualDay) - library["signUpDays"]
        if daysAvailable <= 0:
            return 
        numberBooksGettable = min(library["booksNumber"], daysAvailable * library["shipCapacity"])
        daysTaken = library["signUpDays"] + math.ceil(numberBooksGettable / library["shipCapacity"])
        
        scores = [self.booksScore[index] for index in sortedBooks]
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
    
    def loop(self):
        libraries = copy.copy(self.librairies)
        days = 0
        libraryNb = 0
        usedLibraries = []
        while days < int(self.daysNumber):
            for library in libraries:
                self.setScore(library)
            highestLibrary = self.getHighestScoreLibrary(libraries)
            try:
                days += int(highestLibrary['signUpDays'])
            except:
                break
            libraryNb += 1
            usedLibraries.append(highestLibrary)
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
