from flask import Flask
import requests
import json
app=Flask(__name__)

@app.route("/")
def home():
    #return "Hia"
    #swid: "{5219793E-A1E1-409D-B4F6-4553002DE3C5}"
    #espn2 AECFdZN2ME9jC0RpPvn0iFSucTA6zC2Aci1594ItlyXeW7OarK8YC1p2qWoATmAVYklBskhYNcfrAc%2FCeVsB7T2wesET%2BYRZfOE7e9mJeQJoXNzdZsGjMfJ13pN1uRMnhYT%2FWrWkdWY%2F7GX9HiO%2BWzDHiAF8zLhB68PyvqN0LjzeFtZYhBbOfDNMsyi4rUVXZGjdq%2FqxpjbJF%2F4Sj1Y0dUJ2bW6NInbZem2HoEGYKHpK8gV5hSbZjNFAUTg3L4hqqNQijChIF7Rd0PF4Ogrh0b1q
    leagueID="21251"
    seasonID="2020"

    #for private leagues
    swid_cookie="{5219793E-A1E1-409D-B4F6-4553002DE3C5}"
    espn2_cookie= "AECFdZN2ME9jC0RpPvn0iFSucTA6zC2Aci1594ItlyXeW7OarK8YC1p2qWoATmAVYklBskhYNcfrAc%2FCeVsB7T2wesET%2BYRZfOE7e9mJeQJoXNzdZsGjMfJ13pN1uRMnhYT%2FWrWkdWY%2F7GX9HiO%2BWzDHiAF8zLhB68PyvqN0LjzeFtZYhBbOfDNMsyi4rUVXZGjdq%2FqxpjbJF%2F4Sj1Y0dUJ2bW6NInbZem2HoEGYKHpK8gV5hSbZjNFAUTg3L4hqqNQijChIF7Rd0PF4Ogrh0b1q"

    url="https://fantasy.espn.com/apis/v3/games/ffl/seasons/"+seasonID+"/segments/0/leagues/"+leagueID #team/league info
    #url="https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leagues/21251?view=mMatchup" #Can get final score segment is week and player points
    #url="https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leagues/21251?view=mMatchupScore" #not sure
    #url="https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leagues/21251?view=mMatchup&view=mMatchupScore"
    #url="https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leagues/21251?view=mMatchup"
    #mTeam what moves were made
    #mRoster news
    #mBoxscore complex but maybe can get the data from here
    r=requests.get(url,cookies={"swid": swid_cookie,"espn_s2": espn2_cookie}, params={"view": "mMatchup"})
   
    d = r.json()
    
    #for i in d:
    #    print(i)
    #print(d["schedule"])
    #for i in d["schedule"]:
    #    print(i)
    #for i in d["schedule"][12]:
    #    print(i)
    '''
    away
    home
    id
    matchupPeriodId
    winner
    '''
    #print(d["schedule"][12]["home"]["rosterForCurrentScoringPeriod"]["entries"])
    #for i in d["schedule"][12]["home"]["rosterForCurrentScoringPeriod"]["entries"]:
    #    print(i["playerPoolEntry"]["player"]["fullName"])
    #0-11 are nothing prob week data
    '''
    mMatchup
    draftDetail-nope
    gameId-nope
    id-nope
    schedule - lot #this is were the points are but it big
    scoringPeriodId - what week is it
    seasonId -nope
    segmentId -nope
    status - nitch info
    teams
    '''
    return(d)
  
  #what we need for each player
    #name, points, team/

  #jobs
  #espn data-ryan
  #nfl data-Arya
  # dream team -shamar
  # find out how to use cookies -colton
  
  # testing testing
"""
Ryan

"""

"""
Comment - Shamar
"""
#hello guys -Arya
