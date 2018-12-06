import nflgame
from nflgame import games



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
        defense()
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

#def create_list():
#    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
#    usr_year = int(usr_first.split(" ")[0])
#    week = str(usr_first.split(" ")[1])
#    timeList = [usr_year, week]
#    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
#    limit = int(limit_in)
#    timeList.append(limit)

#    return timeList


def passing(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = int(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(usr_year)
    print(week)
    g = games(int(usr_year), int(week))
    players = nflgame.combine_game_stats(g)
    for p in players.passing().sort('passing_yds').limit(int(limit_in)):
        msg = '%s %d completions for %d yards and %d TDs'
        print msg % (p, p.passing_att, p.passing_yds, p.passing_tds)



def rushing(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = int(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    g = games(int(usr_year), int(week))
    players = nflgame.combine_game_stats(g)
    for p in players.rushing().sort('rushing_yds').limit(int(limit_in)):
       msg = '%s %d carries for %d yards and %d TDs'
       print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)



def receiving(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = str(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    g = games(int(usr_year), int(week))
    players = nflgame.combine_game_stats(g)
    for p in players.receiving().sort('receiving_yds').limit(int(limit_in)):
       msg = '%s %d catches for %d yards and %d TDs'
       print msg % (p, p.receiving_rec, p.receiving_yds, p.receiving_tds)



##Defense portion
def defense():
    statis = raw_input('Enter the word: interceptions, tackles, sacks. To see those stats: and the year you would like to see.(must be lowercase) ')
    int = str("interceptions")
    tak = str("tackles")
    saks = str("sacks")
    pbu = str("PBU")
    if statis == int:
        interceptions(statis)
    elif statis == tak:
        tackles(statis)
    elif statis == saks:
        sacks(statis)
    else:
        print("Error!!! That input did not work! Try again: ")
        defense()

def interceptions(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = str(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    g = games(int(usr_year), int(week))
    players = nflgame.combine_game_stats(g)
    for p in players.defense().sort('defense_int').limit(int(limit_in)):
       msg = '%s %d interceptions for %d yards and %d TDs'
       print msg % (p, p.defense_int, p.defense_int_yds, p.defense_int_tds)

def tackles(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = str(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    g = games(int(usr_year), int(week))
    players = nflgame.combine_game_stats(g)
    for p in players.defense().sort('defense_tkl').limit(int(limit_in)):
       msg = '%s %d tackles with %d assisted tackles, %d sacks, %d TFLs, and %d fumbles'
       print msg % (p, p.defense_tkl, p.defense_ast, p.defense_sk, p.defense_tkl_loss, p.defense_ffum)


def sacks(statis):
    usr_first = raw_input("What year and week  would you like to view? (ex. 2018 8): ")
    usr_year = int(usr_first.split(" ")[0])
    week = str(usr_first.split(" ")[1])
    timeList = [usr_year, week]
    limit_in = raw_input("Enter the amount of people you would like to see for top stats for this week of this year. I.E. TOP 5, 10, 15, 20: ")
    limit = int(limit_in)
    timeList.append(limit)
    print(timeList)
    g = games(int(usr_year), int(week))
    players = nflgame.combine_game_stats(g)
    for p in players.defense().sort('defense_sk').limit(int(limit_in)):
       msg = '%s %d sacks with %d sack yds, and %d QB hits'
       print msg % (p, p.defense_sk, p.defense_sk_yds, p.defense_qbhit)



welcome()
