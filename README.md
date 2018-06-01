## PokerSquares

# Introduction

This was my first ever coding project. In November of 2017, I picked up a book on python, and ver very quickly learned the basics of the language. Within 1 week, I started working on this project and two weeks after that, I completed it.

# Disclaimer

Because this was my first ever coding project, you will very quickly notice that the code is a piece of shit. No class structure, ambiguous variable namings, non PEP8 standards, etc. I could in theory go back and refactor everything, make it look pretty, but I am not finding the motivation to dig through all this stuff, and would rather start a new project than still work on this one (to see a better example of my python coding skills, I suggest you check out the app folder of (filigree)[https://github.com/MichalBurgunder/Filigree].

# Rules of the Game

When you start the game, you will have a five by five grid of places where you can place cards. For each turn, you will flip a card and will be asked to place it in an empty spot in the grid. There will 25 cards flipped in total. The goal of the game is to accumulate as many points as you can (you can see the point distributions in the options, inside the game).
The amount of points is dependent on how rare of a poker combination you have in a row, or a column. So for example, you might have KH, KS, KC, 5H and 6H in a single row, which might give you 25 points (a good score), but you also have to conside the arrangement you get when looking at the columns, so you might get a combination that looks like KH, QD, 9S, TS, JC, which would consitute a straight (15 points).
The scores are calculated as you play, but only the final score matters. 

Have fun! <3
