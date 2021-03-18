import csv
def calculate_winrate(file_name, output):
    print("Calculating winrate...")
    with open(file_name,'r') as f:
        reader = csv.reader(f, delimiter = ',')
        next(reader)
        blue_wins = 0
        total_games = 0
        for row in reader:
            blue_team_victory = True if int(row[10]) == 1 else False
            if blue_team_victory:
                blue_wins += 1
            total_games += 1
    f.close()   
    print("Done calculating winrate.")
    with open(output, 'w') as f:
        f.write(str([blue_wins, total_games]))
    f.close()
    return [blue_wins, total_games]
    