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

#def tuple_creator(usr_year, week):
 #   usr_year1 = usr_year
  #  week1 = week

#    yearLi

#    return tuple1




def passing(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = str(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    games = nflgame.games(timeList[0], week=timeList[1])
    players = nflgame.combine_game_stats(games)
    for p in players.passing().sort('passing_yds').limit(20):
        msg = '%s %d carries for %d yards and %d TDs'
        print msg % (p, p.passing_att, p.passing_yds, p.passing_tds)
    return usr_year


def rushing(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = str(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    games = nflgame.games(timeList[0], week=timeList[1])
    players = nflgame.combine_game_stats(games)
    for p in players.rushing().sort('rushing_yds').limit(timeList[2]):
       msg = '%s %d carries for %d yards and %d TDs'
       print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)
    return usr_year


def receiving(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = str(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    games = nflgame.games(timeList[0], week=timeList[1])
    players = nflgame.combine_game_stats(games)
    for p in players.receiving().sort('receiving_yds').limit(timeList[2]):
       msg = '%s %d catches for %d yards and %d TDs'
       print msg % (p, p.receiving_att, p.receiving_yds, p.receiving_tds)
    return usr_year


welcome()


"""
def defense():
    statis, year = in



games = nflgame.games(2017, week=7)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(10):
    msg = '%s %d carries for %d yards and %d TDs'
    print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)"""
