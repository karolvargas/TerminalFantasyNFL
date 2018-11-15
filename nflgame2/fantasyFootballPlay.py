import nflgame



def welcome():

    print("Welcome to Python NFL Consistency Checker! ")
    stats = raw_input('Are you looking for offense or defense?(must be lowercase) ')
    print(type(stats))
    stats = str(stats)
    #stats = stats.strip()
    o = str("offense")
    d = str("defense")
    if stats == o:
        offense()
    elif stats == d:
        print("defense!")
    else:
        print("Um lets try that again...")
        welcome()

def offense():
    statis = raw_input('Enter the word: passing, rushing, or receiving. To see those stats: and the year you would like to see.(must be lowercase) ')
    p = str("passing")
    r = str("rushing")
    rc = str("receiving")
    if statis == p:
        passing(statis)
    elif statis == r:
        rushing(statis)
    elif statis == rc:
        receiving(statis)
    else:
        print("Error!!! That input did not work! Try again: ")
        offense()

def passing(statis):
    usr_year, week = map(int, input("What year and week  would you like to view? (ex. 2018 8): ").split())
    if week > 17:
        print("Theres only 17 weeks man! Lets try this again: ")
        passing(statis, year)
    elif week <= 0:
        print("Are you done messing around bro... Again")
        passing(statis, year)
    limit = raw_input("Enter the amount of people you would like to see for top stats for week ",week," of ",usr_year,". I.E. TOP 5, 10, 15, 20: ")
    limit = [int(limit)]
    games = nflgame.games(usr_year, week=week)
    players = nflgame.combine_game_stats(games)
    for p in players.passing().sort('passing_yds').limit(limit):
        msg = '%s %d carries for %d yards and %d TDs'
        print msg % (p, p.passing_att, p.passing_yds, p.passing_tds)


welcome()


"""
def defense(): 
    statis, year = in       



games = nflgame.games(2017, week=7)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(10):
    msg = '%s %d carries for %d yards and %d TDs'
    print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)"""
