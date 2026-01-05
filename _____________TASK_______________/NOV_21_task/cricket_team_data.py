team = { 
"player1": {"name": "Rohit", "role": "Batsman"}, 
"player2": {"name": "Bumrah", "role": "Bowler"} 
} 


# print(team["player2"]["role"])

# Add data
team["Matches"] = {"name" : "Rohit", "Matches" :  30}

# print(team)

# remove data

team["player2"].pop("role")

print(team)

