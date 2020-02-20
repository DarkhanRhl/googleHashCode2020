#!/usr/bin/env python3
import sys
import parsing
import core

parsing = parsing.Parsing(sys.argv[1])
[booksNumber, librariesNumber, daysNumber, booksScore, librairies] = parsing.getParsing()

core.Core(booksNumber, librariesNumber, daysNumber, booksScore, librairies)

# print("Number of books: " + booksNumber)
# print("Number of librairies: " + librariesNumber)
# print("Number of days: " + daysNumber)
# print("books score: ", end="")
# print(booksScore)
# print("\n\n----LIBRAIRIES----")

# for library in librairies:
#     print("library number of book: " + library["booksNumber"])
#     print("library signup duration: " + library["signUpDays"])
#     print("library ship capacity: " + library["shipCapacity"])
#     print("library books: ", end="")
#     print(library["books"])
#     print("\n")