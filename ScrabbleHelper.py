import codecs
import random
import string

# utworzenie początkowej planszy do gry
board = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 't', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'a', '-', '-', '-', '-'],
         ['-', '-', '-', '-', 's', 'u', 'r', 'o', 'w', 'i', 'c', 'a', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'z', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'k', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'a', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

# wydrukowanie planszy początkowej
for row in board:
    for cell in row:
        print(cell, end=" ")
    print()

# wczytanie listy wyrazów z pliku
dictionary = codecs.open('slowa.txt', encoding='utf-8')

# wylosowanie 7 liter
letters = []
for i in range(7):
    letters.append(random.choice(string.ascii_letters.lower()))

print('\nWylosowane litery:')
print(letters)

lettersOnDeck = []
for row in board:
    for cell in row:
        if cell not in lettersOnDeck and cell != '-':
            lettersOnDeck.append(cell)

print('\nLitery na planszy:')
print(lettersOnDeck)

foundWords = []

print("\nPrzetwarzanie, proszę czekać...")
for word in dictionary:

    flag = 0
    candidateWord = ''

    for char in word:
        if char in lettersOnDeck:
            flag = 1
            candidateWord = word.replace(char, '', 1)
            break
        else:
            continue

    bufferLetters = letters[:]
    candidateWord = candidateWord.replace('\r\n', '')

    for char in candidateWord:

        if char not in bufferLetters:
            flag = 0
            break
        else:
            bufferLetters.remove(char)
            continue

    if flag == 1:
        foundWords.append(word)
    else:
        continue


SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

bestScore = 0
bestWord = ''

for word in foundWords:
    total = 0
    word = word.replace('\r\n', '')

    for char in word:
        total += SCORES[char]

    if total > bestScore:
        bestScore = total
        bestWord = word

print("Znalezione słowo o największej liczbie punktów: " + word + ", liczba punktów: " + str(bestScore))

for char in word:
    if char in lettersOnDeck:
        rootLetter = char

for rowIndex, row in enumerate(board):
    for cellIndex, cell in enumerate(row):
        if cell == rootLetter:
            print("Pozycja litery " + rootLetter + " => (" + str(rowIndex) + "," + str(cellIndex) + ")")
            break
