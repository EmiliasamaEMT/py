players=['charles','martina','michael','florence','eli']
print(players[1:4])
print(players[-3:])
print("Here are the first team members:")
for player in players[-2:]:
    print(player.title())
a_players=players[:]

b_players=players
players.append('cake')
print(a_players)
print(b_players)

dim=(200,50)
print(dim)
dim=(390,12)
print(dim)
