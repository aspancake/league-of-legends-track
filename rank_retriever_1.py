# ***********************#
# * Rank Retriever 1.0 * #
# ***********************#

# Get your tools ready
import re
import time
import cassiopeia
import numpy as np
import csv
from cassiopeia import riotapi
from cassiopeia import baseriotapi
from cassiopeia.type.core.common import LoadPolicy

# Create a list of all the players you are looking up
players = ['cakesofspan','Crs Risen','Maknae Seohyun']
ids = [30864736,30251656,49359126]

# Setting a rate limit for how often you are pinging Riot's API so they don't get mad
# 10 calls per 10 seconds AND 500 calls per 10 minutes
riotapi.set_rate_limits((10, 10), (500, 600));

# Set your region and API Key which can be found here: (https://developer.riotgames.com/)
# Do NOT release your API Key to the public
riotapi.set_region("NA")
riotapi.set_api_key("VALUE HERE")

# Get the information for each summoner
division_list = []
tier_list = []
points_list = []
wins_list = []
losses_list = []

for i in range(0,len(ids)):
    full = baseriotapi.get_league_entries_by_summoner(ids[i])
    info_string = str(full['%d' % ids[i]][0])
    division = re.findall('"division": "(.+?)",', info_string)
    tier = re.findall('"tier": "(.+?)"', info_string)
    points = re.findall('"leaguePoints": (.+?),', info_string)
    # wins = re.findall('"wins": (.+?),', info_string)
    losses = re.findall('"losses": (.+?),', info_string)

    division_list.append(division)
    tier_list.append(tier)
    points_list.append(points)
    # wins_list.append(wins)
    losses_list.append(losses)

# Create a numpy arrays and put them together
date = str(time.strftime("%d_%m_%Y"))
f = open("player_stats_%s.csv" % date, "w")

for i in range(0,len(players)):
    f.write("{},{},{},{} \n".format(players[i],tier_list[i],division_list[i],points_list[i]))

f.close()



