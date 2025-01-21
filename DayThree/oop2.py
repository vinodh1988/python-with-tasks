class Team:
    def __init__(self, members):
        self.members = members

    def __add__(self, other):
        return Team(self.members + other.members)

    def __repr__(self):
        return f"Team({self.members})"

# Example usage:
team1 = Team(["Alice", "Bob"])
team2 = Team(["Charlie", "David"])
team3 = team1 + team2 # team1.__add__(team2) ,self is team1
print(team3)  # Output: Team(['Alice', 'Bob', 'Charlie', 'David'])