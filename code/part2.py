##############
# basic python
##############

##########################
# how to read this chapter
##########################
1 + 1

##########
# comments
##########

# print the result of 1 + 1
print(1 + 1)

###########
# variables
###########

three_pt_made = 4

three_pt_made
3*three_pt_made

three_pt_made = three_pt_made + 1

three_pt_made

####################
# types of variables
####################

over_under = 216  # int
fg_percentage = 0.48  # float

starting_c = 'Karl-Anthony Towns'
starting_pg = "D'Angelo Russel"

type(starting_c)

type(over_under)

starters = f'{starting_c}, {starting_pg}, etc.'
starters

# string methods
'from downtown!'.upper()

'Ron Artest'.replace('Artest', 'World Peace')

####################################
# How to figure things out in Python
####################################
'lebron james'.capitalize()

'  lebron james'
'lebron james'

#######
# bools
#######
team1_pts = 110
team2_pts = 120

# and these are all bools:
team1_won = team1_pts > team2_pts
team2_won = team1_pts < team2_pts
teams_tied = team1_pts == team2_pts
teams_did_not_tie = team1_pts != team2_pts

type(team1_won)
teams_did_not_tie

# error because test for equality is ==, not =
# teams_tied = (team1_pts = team2_pts)  # commented out since it throws an error

shootout = (team1_pts > 130) and (team2_pts > 130)
at_least_one_good_team = (team1_pts > 120) or (team2_pts > 120)
you_guys_are_bad = not ((team1_pts > 100) or (team2_pts > 100))
meh = not (shootout or at_least_one_good_team or you_guys_are_bad)

###############
# if statements
###############
if team1_won:
  message = "Nice job team 1!"
elif team2_won:
  message = "Way to go team 2!!"
else:
  message = "must have tied!"

message
