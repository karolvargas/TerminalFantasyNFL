import nflgame

print("Welcome to Fantasy Checker!\n You have the option to look up this weeks top performers in either rushing, passing, receiving, or kicking. \n")
games = nflgame.games(2017)
print len(games)
stats = input("What stats would you like to see? (rushing, receiving, passing, kicking) ")




#if stats == 'rushing':
