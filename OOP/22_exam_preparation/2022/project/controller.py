class Controller:
    def __init__(self):
        self.players = []  # An empty list that will contain all the players (objects)
        self.supplies = []  # An empty list that will contain all the supplies (objects)

    @property
    def food_left(self):
        return len([x for x in self.supplies if x.__class__.__name__ == "Food"])

    @property
    def drinks_left(self):
        return len([x for x in self.supplies if x.__class__.__name__ == "Drink"])

    def __find_player(self, name: str):
        return [x for x in self.players if x.name == name][0]

    def add_player(self, *players):
        added_players = []

        for current_player in players:
            for searched_player in self.players:
                if current_player.name == searched_player.name:
                    raise Exception(f"Name {current_player.name} is already used!")
                
            self.players.append(current_player)
            added_players.append(current_player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supply):
        self.supplies.extend(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        current_player = self.__find_player(player_name)

        if not current_player:
            return
        if sustenance_type not in ["Food", "Drink"]:
            return
        if sustenance_type == "Food" and not self.food_left:
            raise Exception("There are no food supplies left!")
        if sustenance_type == "Drink" and not self.food_left:
            raise Exception("There are no drink supplies left!")
        if not current_player.need_sustenance:
            return f"{player_name} have enough stamina."

        for current_supply in self.supplies[::-1]:
            if current_supply.__class__.__name__ == sustenance_type:
                before_stamina = current_player.stamina
                if current_player.stamina + current_supply.energy > 100:
                    current_player.stamina = 100
                diff = current_player.stamina - before_stamina
                return f"{player_name} sustained successfully with {diff}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = self.__find_player(first_player_name)
        player_two = self.__find_player(second_player_name)

        if player_one.stamina == 0 and player_two.stamina == 0:
            return f"Player {player_one.name} does not have enough stamina.\n" \
                   f"Player {player_two.name} does not have enough stamina."

        for player in (player_two, player_one):
            if player.stamina == 0:
                return f"Player {player.name} does not have enough stamina."

        players_list = sorted([player_one, player_two], key=lambda x: x.stamina)

        attacker = players_list[0]
        defensive_player = players_list[1]

        damage = attacker.stamina / 2
        defensive_player.stamina -= damage
        if defensive_player.stamina <= 0:
            return f"Winner: {attacker.name}"

        damage = defensive_player.stamina / 2
        attacker.stamina -= damage
        if attacker.stamina <= 0:
            return f"Winner: {defensive_player.name}"

        winner = sorted([player_one, player_two], key=lambda x: -x.stamina)[0]
        return f"Winner: {winner}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0
            for supply in self.supplies:
                pass

    def __str__(self):
        players_output = "\n".join([str(player) for player in self.players]) + "\n"
        supply_output = "\n".join([supply.details() for supply in self.supplies]) + "\n"
        return players_output, supply_output
