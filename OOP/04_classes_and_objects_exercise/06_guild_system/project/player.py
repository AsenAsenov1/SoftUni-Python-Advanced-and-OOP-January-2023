class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills.keys():
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        info = f"Name: {self.name}\n"
        info += f"Guild: {self.guild}\n"
        info += f"HP: {self.hp}\n"
        info += f"MP: {self.mp}\n"
        info += "\n".join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])
        return info.strip()
