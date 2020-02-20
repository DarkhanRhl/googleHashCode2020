import math

class Core:
    def __init__(self, booksNumber, librariesNumber, daysNumber, booksScore, librairies):
        self.booksNumber = booksNumber #Number
        self.librariesNumber = librariesNumber #Number
        self.daysNumber = daysNumber #Number
        self.booksScore = booksScore #List of Number
        self.librairies = librairies #List of Object

        self.actualDay = 0
        self.end = False

        self.gameLoop()

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

    def gameLoop(self):
        while not self.end:
            for library in self.librairies:
                self.setScore(library)
            self.actualDay += 1
            if self.actualDay == self.daysNumber:
                self.end = True
