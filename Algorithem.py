import random
import bs4 as bs
import requests
import pickle


'''t1_opp =
t2_opp =
t1_ppg =
t2_ppg =
t1_seed =
t2_seed =
rnd ='''




# total = ()

def get_seed_prob(seed, rnd):

    seed_row = seed - 1
    rnd_col = rnd

    seed_prob_rnd = [(1, .993, .853, .691, .412, .243, .154, .618),
                     (2, .941, .625, .456, .206, .096, .037, .147),
                     (3, .846, .515, .250, .118, .074, .029, .118),
                     (4, .794, .471, .154, .096, .022, .007, .029),
                     (5, .654, .338, .059, .044, .022, .001, .001),
                     (6, .632, .309, .103, .022, .015, .007, .029),
                     (7, .618, .199, .074, .022, .007, .007, .029),
                     (8, .500, .096, .059, .037, .022, .007, .029),
                     (9, .500, .051, .029, .007, .001, .001, .001),
                     (10, .382, .169, .059, .007, .001, .001, .001),
                     (11, .368, .162, .059, .029, .001, .001, .001),
                     (12, .346, .147, .007, .001, .001, .001, .001),
                     (13, .206, .044, .001, .001, .001, .001, .001),
                     (14, .154, .015, .001, .001, .001, .001, .001),
                     (15, .059, .007, .001, .001, .001, .001, .001),
                     (16, .007, .001, .000, .000, .000, .000, .000)]



    seed_row_list = seed_prob_rnd[seed_row]

    overall_prob = seed_row_list[-1]

    win_prob = seed_row_list[rnd_col]

    print(win_prob)

    return win_prob, overall_prob

def get_teams(seed, region):

    east_teams = ['Duke', 'Michigan State', 'LSU', 'Virginia Tech', 'Mississippi State', 'Maryland', 'Louisville',
                  'VCU', 'UCF', 'Minnesota', TBH, 'Liberty', 'Saint Louis', 'Yale', 'Bradley', TBH]
    west_teams = ['Gonzaga', 'Michigan', 'Texas Tech', 'Florida State', 'Marquette', 'Buffalo', 'Nevada',
                  'Syracuse', 'Baylor', 'Florida', TBH, 'Murray State', 'Vermont', 'N Kentucky', 'Montana', TBH]
    south_teams = ['Virginia', 'Tennessee', 'Purdue', 'Kansas State', 'Wisconsin', 'Villanova', 'Cincinnati',
                      'Ole Miss', 'Oklahoma', 'Iowa', "Saint Mary's", 'Oregon', 'UC Irvine', 'Old Dominion', 'Colgate',
                      'Gardner-Webb']
    midwest_teams = ['North Carolina', 'Kentucky', 'Huston', 'Kansas', 'Auburn', 'Iowa State', 'Woffford',
                      'Utah State', 'Washington', 'Seton Hall', 'Ohio State', 'New Mexico State', 'Northeastern',
                      'Georgia State', 'Abil Christian', 'Iona']

    seed_list = seed - 1

    if region == 'e':
        team = east_teams[seed_list]
    elif region == 'w':
        team = west_teams[seed_list]
    elif region == 's':
        team = south_teams[seed_list]
    elif region == 'mw':
        team = midwest_teams[seed_list]


    return team

def team_info(team_name):
    east_teams = ['Duke', 'Michigan State', 'LSU', 'Virginia Tech', 'Mississippi State', 'Maryland', 'Louisville',
                  'VCU', 'UCF', 'Minnesota', TBH, 'Liberty', 'Saint Louis', 'Yale', 'Bradley', TBH]
    west_teams = ['Gonzaga', 'Michigan', 'Texas Tech', 'Florida State', 'Marquette', 'Buffalo', 'Nevada',
                  'Syracuse', 'Baylor', 'Florida', TBH, 'Murray State', 'Vermont', 'N Kentucky', 'Montana', TBH]
    south_teams = ['Virginia', 'Tennessee', 'Purdue', 'Kansas State', 'Wisconsin', 'Villanova', 'Cincinnati',
                   'Ole Miss', 'Oklahoma', 'Iowa', "Saint Mary's", 'Oregon', 'UC Irvine', 'Old Dominion', 'Colgate',
                   'Gardner-Webb']
    midwest_teams = ['North Carolina', 'Kentucky', 'Huston', 'Kansas', 'Auburn', 'Iowa State', 'Woffford',
                     'Utah State', 'Washington', 'Seton Hall', 'Ohio State', 'New Mexico State', 'Northeastern',
                     'Georgia State', 'Abil Christian', 'Iona']

    team_info = [team_name]         # team info variable is [team_name, team_seed, team_region]

    if midwest_teams.index(team_name) > -1:
        team_seed = midwest_teams.index(team_name)
        team_region = 'mw'
    elif south_teams.index(team_name) > -1:
        team_seed = south_teams.index(team_name)
        team_region = 's'
    elif west_teams.index(team_name) > -1:
        team_seed = west_teams.index(team_name)
        team_region = 'w'
    elif east_teams.index(team_name) > -1:
        team_seed = east_teams.index(team_name)
        team_region = 'e'

    team_info.append(team_seed)
    team_info.append(team_region)

    return team_info




def round_matchups():
    round_1_winners = []
    round_1_matchups = (0, 16, 15, 14, 13, 12, 11, 10, 9)



    for x in range(1):
        print(random.randint(1, total + 1))




get_seed_prob(1, 1)


