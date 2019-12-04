import csv

class fileRead:

    def __init__(self):
        with open('players_20.csv', encoding='utf8') as data:
            players = csv.reader(data, delimiter=',')

            goalkeepers = list()
            goalkeepers_overalls = list()
            goalkeepers_values = list()
            field_players = list()
            field_players_overalls = list()
            field_players_values = list()

            row_number = 0
            column_number = 0

            for row in players:
                if row_number == 0:
                    for column in row:
                        if column == 'player_positions':
                            player_position = column_number
                        elif column == 'overall':
                            overall = column_number
                        elif column == 'value_eur':
                            value_eur = column_number
                        elif column == 'pace':
                            pace = column_number
                        elif column == 'shooting':
                            shooting = column_number
                        elif column == 'passing':
                            passing = column_number
                        elif column == 'dribbling':
                            dribbling = column_number
                        elif column == 'defending':
                            defending = column_number
                        elif column == 'physic':
                            physic = column_number
                        elif column == 'gk_diving':
                            gk_diving = column_number
                        elif column == 'gk_handling':
                            gk_handling = column_number
                        elif column == 'gk_kicking':
                            gk_kicking = column_number
                        elif column == 'gk_reflexes':
                            gk_reflexes = column_number
                        elif column == 'gk_speed':
                            gk_speed = column_number
                        elif column == 'gk_positioning':
                            gk_positioning = column_number
                        column_number += 1
                else:
                    player_attributes = []
                    if row[player_position] == 'GK':
                        player_attributes.append(int(row[gk_diving]))
                        player_attributes.append(int(row[gk_handling]))
                        player_attributes.append(int(row[gk_kicking]))
                        player_attributes.append(int(row[gk_reflexes]))
                        player_attributes.append(int(row[gk_speed]))
                        player_attributes.append(int(row[gk_positioning]))
                        player_overall = int(row[overall])
                        player_value = int(row[value_eur])
                        goalkeepers.append(player_attributes)
                        goalkeepers_overalls.append(player_overall)
                        goalkeepers_values.append(player_value)
                    else:
                        player_attributes.append(int(row[pace]))
                        player_attributes.append(int(row[shooting]))
                        player_attributes.append(int(row[passing]))
                        player_attributes.append(int(row[dribbling]))
                        player_attributes.append(int(row[defending]))
                        player_attributes.append(int(row[physic]))
                        player_overall = int(row[overall])
                        player_value = int(row[value_eur])
                        field_players.append(player_attributes)
                        field_players_overalls.append(player_overall)
                        field_players_values.append(player_value)

                row_number += 1
