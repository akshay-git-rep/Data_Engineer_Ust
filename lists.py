wc_teams = ["india","newzeland","bangladesh"]
wc_win = [1,2,3]
print(type(wc_teams),wc_teams)
wc_teams.append("austerlia")
print(wc_teams)
wc_teams.insert(1,"akshay")
print(wc_teams)
wc_teams.pop()
print(wc_teams)
wc_teams.remove("akshay")
print(wc_teams)

for team,won in zip(wc_teams,wc_win):
    print(team,":",won)

teams = ":".join(wc_teams)
print(teams)

print(wc_teams[1])
wc_teams.extend(["akshay","bharath"])
print(wc_teams)

wc_teams.sort()
print(wc_teams)
print(wc_teams[::-1])






    
