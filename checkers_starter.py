class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.data = [[' ' for i in range(self.width)] for j in range(self.height)]
    def can_make_move(self,r,c):
        if self.data[r][c] == ' ':
            return True 
        return False
    def make_move(self, r, c):
        if self.can_make_move(r,c):
            self.data[r][c] = 'S'
