import json


class Database:
    def __init__(self, player_name, score):
        if isinstance(player_name, str) is True:
            self.player_name = player_name
        else:
            raise TypeError("Name must be string only")
        self.score = score

    def write_database(self):
        data = {self.player_name: self.score}
        try:
            with open('database.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('database.json', 'w') as file:
                json.dump(data, file, indent=5)
        else:
            data.update(data)
            with open('database.json', 'w') as file:
                json.dump(data, file, indent=5)

    def sorted_score(self):
        with open('database.json', 'r') as data_file:
            data = json.load(data_file)
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        convected_data = dict(sorted_data)
        top = [{x: convected_data[x]} for x in convected_data]
        return top
