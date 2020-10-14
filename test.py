class Team:
    a = 0
    def __init__(self):
        pass    
    def get_a(self):
        return self.a 
    def set_a(self, new_a):
        self.a = new_a


team = Team()
print(team.get_a())

team.set_a(5)
print(team.get_a())