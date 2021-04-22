import csv


# read the dataset file and calacualte the winrate
# write the win rate to the desire file
def calculate_winrate(file_name, output):
    print("Calculating winrate...")
    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        blue_wins = 0  # count blue wins
        total_games = 0
        for row in reader:
            blue_team_victory = True if int(row[10]) == 1 else False
            if blue_team_victory:
                blue_wins += 1
            total_games += 1
    f.close()
    print("Done calculating winrate.")
    # write to file
    with open(output, 'w') as f:
        f.write(str('\n'.join([str(blue_wins), str(total_games)])))
    f.close()
