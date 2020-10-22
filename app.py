from flask import Flask, render_template
import requests
import json
app=Flask(__name__)

@app.route("/")
def home():
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


    #general league info
    r=requests.get(url,cookies={"swid": swid_cookie,"espn_s2": espn2_cookie})
   
    d = r.json()
    
    weekNumber=int(d["scoringPeriodId"]) #what week
    idToTeamName={}
    for x in d["teams"]:
        idToTeamName[x["id"]]=x["location"]+" "+x["nickname"]
    #print(idToTeamName)



    r=requests.get(url,cookies={"swid": swid_cookie,"espn_s2": espn2_cookie}, params={"view": "mMatchup"})
    d = r.json()
    with open('free_agent_details.json', 'r') as free_agent_details_file:
        free_agent_details = json.load(free_agent_details_file)
    
    TeamData={}

    for j in range(int(len(idToTeamName)/2)):
        name1=idToTeamName[d["schedule"][(weekNumber-1)*int(len(idToTeamName)/2)+j]["home"]["rosterForCurrentScoringPeriod"]["entries"][0]["playerPoolEntry"]["onTeamId"]]
        print(name1)

        TeamData[name1]={"players":[]}


        totalHome=0

        for i in d["schedule"][(weekNumber-1)*int(len(idToTeamName)/2)+j]["home"]["rosterForCurrentScoringPeriod"]["entries"]:
            print(i["playerPoolEntry"]["player"]["fullName"], end="")
            print("  "+str(i["playerPoolEntry"]["appliedStatTotal"]), end="")
            activeSwitch=False
            if(i["lineupSlotId"]!=20 and i["lineupSlotId"]!=21): #20 for bench 21 for IR
                totalHome+=i["playerPoolEntry"]["appliedStatTotal"]
                print(" active")
                activeSwitch=True
            else:
                print()
            if("D/ST" not in i["playerPoolEntry"]["player"]["fullName"] and "Antonio Brown" not in i["playerPoolEntry"]["player"]["fullName"] and "." not in i["playerPoolEntry"]["player"]["fullName"]):
                TeamData[name1]["players"].append({"name":i["playerPoolEntry"]["player"]["fullName"],
                                    "proTeam": free_agent_details[i["playerPoolEntry"]["player"]["fullName"]]["editorial_team_full_name"] ,
                                    "position": free_agent_details[i["playerPoolEntry"]["player"]["fullName"]]["primary_position"] , 
                                    "active": activeSwitch,
                                    "points": i["playerPoolEntry"]["appliedStatTotal"] ,
                                    "injured": i["playerPoolEntry"]["player"]["injured"],
                                    "fantasyteam": i["playerPoolEntry"]["onTeamId"] , 
                                    "img_url": free_agent_details[i["playerPoolEntry"]["player"]["fullName"]]["image_url"] ,
                                    "gameTime": "ETA"  , 
                                    "avgPoints": 0.0 ,
                                    "inPlay": False })
        print("total "+str(totalHome))
        print()
        print()
        name1=idToTeamName[d["schedule"][(weekNumber-1)*int(len(idToTeamName)/2)+j]["away"]["rosterForCurrentScoringPeriod"]["entries"][0]["playerPoolEntry"]["onTeamId"]]
        print(name1)

        TeamData[name1]={"players":[]}
        totalAway=0
        for i in d["schedule"][(weekNumber-1)*int(len(idToTeamName)/2)+j]["away"]["rosterForCurrentScoringPeriod"]["entries"]:
            print(i["playerPoolEntry"]["player"]["fullName"], end="")
            print("  "+str(i["playerPoolEntry"]["appliedStatTotal"]), end="")
            activeSwitch=False
            if(i["lineupSlotId"]!=20 and i["lineupSlotId"]!=21):
                totalAway+=i["playerPoolEntry"]["appliedStatTotal"]
                print(" active")
                activeSwitch=True
            else:
                print()
            if("D/ST" not in i["playerPoolEntry"]["player"]["fullName"] and "Antonio Brown" not in i["playerPoolEntry"]["player"]["fullName"] and "." not in i["playerPoolEntry"]["player"]["fullName"]):
                TeamData[name1]["players"].append({"name":i["playerPoolEntry"]["player"]["fullName"],
                                    "proTeam": free_agent_details[i["playerPoolEntry"]["player"]["fullName"]]["editorial_team_full_name"] ,
                                    "position": free_agent_details[i["playerPoolEntry"]["player"]["fullName"]]["primary_position"] , 
                                    "active": activeSwitch,
                                    "points": i["playerPoolEntry"]["appliedStatTotal"] ,
                                    "injured": i["playerPoolEntry"]["player"]["injured"],
                                    "fantasyteam": i["playerPoolEntry"]["onTeamId"] , 
                                    "img_url": free_agent_details[i["playerPoolEntry"]["player"]["fullName"]]["image_url"] ,
                                    "gameTime": "ETA"  , 
                                    "avgPoints": 0.0 ,
                                    "inPlay": False })
        print("total "+str(totalAway))
        print()
        print()


    #0-11 are nothing prob week data
    #r=requests.get(url,cookies={"swid": swid_cookie,"espn_s2": espn2_cookie}, params={"view": "kona_player_info"})
    #d = r.json()
    #return(d)
    return render_template("matchUp.html", TeamData=TeamData)
    #return free_agent_details["A.J. Brown"]
    #return TeamData
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
