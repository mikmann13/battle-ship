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
    def __repr__(self):
        s = ''                          
        for row in range(0, self.height):
            s += 'O'
            for col in range(0, self.width):
                s += self.data[row][col] + 'O'
            s += '\n'
        return s
