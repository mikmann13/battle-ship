class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.data = [[0 for i in range(self.width)] for j in range(self.height)]
    def is_full(self,r,c):
        if self.data[r][c]
