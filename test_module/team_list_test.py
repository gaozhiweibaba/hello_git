import json


team_list = []
for i in range(105):
    team_number = "TEAM024c1816e20773d" + str(i)
    team_name = "test" + str(i)
    rank = 1 + i
    score = 100 + i
    team_dict = {
        "team_number": team_number,
        "team_name": team_name,
        "team_avatar": "https://static.laohu8.com/default-avatar.jpg",
        "rank": rank,
        "score": score
    }

    json_str = str(team_dict).replace("'", '"')
    print(json_str, ",")



