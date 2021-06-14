players_dict = {
1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

for player in players_dict.values():
    if player["team"] == "A" and player["status"] == "Rest":
        print("игроки из команды А, которые отдыхают", player["name"])
    elif player["team"] == "B" and player["status"] == "Training":
        print("игроки из команды B, которые тренируются", player["name"])
    elif player["team"] == "C" and player["status"] == "Travel":
        print("игроки из команды С, которые путешествуют", player["name"])

a_rest = [
    player["name"]
    for player in players_dict.values()
    if player["team"] == "A"
    and player["status"] == "Rest"
]
print("Игроки команды А, которые отдыхают:", "\n", a_rest)
b_training = [
    player["name"]
    for player in players_dict.values()
    if player["team"] == "B"
    and player["status"] == "Training"
]

b_training = [
    player["name"]
    for player in players_dict.values()
    if player["team"] == "B"
    and player["status"] == "Training"
]
print("Игроки команды B, которые тренируются:", "\n", b_training)

с_travel = [
    player["name"]
    for player in players_dict.values()
    if player["team"] == "C"
    and player["status"] == "Travel"
]
print("Игроки команды C, которые путешествуют:", "\n", с_travel)

