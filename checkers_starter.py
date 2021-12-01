import random
class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.data = [['O' for i in range(self.width)] for j in range(self.height)]
        self.available_guesses = []
        for row in range(0, 8):
            for col in range(0, 8):
                self.available_guesses += [(row, col)]
    
    def __repr__(self):
        s = ''                          
        for row in range(0, self.height):
            for col in range(0, self.width):
                s += self.data[row][col] 
            s += '\n'
        return s

    def can_place(self,r,c):
        if self.data[r][c] == 'O':
            return True 
        return False

    def place_ship(self, r_0,c_0,r_1,c_1):
        if r_0 == r_1:
            for i in range(c_0,c_1):
                if self.can_place(r_0,i):
                    self.data[r_0][i] = 'S'
        if c_0 == c_1:
            for i in range(r_0,r_1):
                if self.can_place(i,c_0):
                    self.data[i][c_0] = 'S'


    def init_game(self):
        while True:
            r_0 = int(input('start row for 5: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            if r_0 == r_1:
                if abs(c_0-c_1) == 5:
                    self.place_ship(r_0,c_0,r_1,c_1)
            if c_0 == c_1:
                if abs(r_0-r_1) == 5:
                    self.place_ship(r_0,c_0,r_1,c_1)
            print(self)

            r_0 = int(input('start row for 4: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            if r_0 == r_1:
                if abs(c_0-c_1) == 4:
                    self.place_ship(r_0,c_0,r_1,c_1)
            if c_0 == c_1:
                if abs(r_0-r_1) == 4:
                    self.place_ship(r_0,c_0,r_1,c_1)
            print(self)

            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            if r_0 == r_1:
                if abs(c_0-c_1) == 3:
                    self.place_ship(r_0,c_0,r_1,c_1)
            if c_0 == c_1:
                if abs(r_0-r_1) == 3:
                    self.place_ship(r_0,c_0,r_1,c_1)
            print(self)
            
            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            if r_0 == r_1:
                if abs(c_0-c_1) == 3:
                    self.place_ship(r_0,c_0,r_1,c_1)
            if c_0 == c_1:
                if abs(r_0-r_1) == 3:
                    self.place_ship(r_0,c_0,r_1,c_1)
            print(self)
            
            r_0 = int(input('start row for 2: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            if r_0 == r_1:
                if abs(c_0-c_1) == 2:
                    self.place_ship(r_0,c_0,r_1,c_1)
            if c_0 == c_1:
                if abs(r_0-r_1) == 2:
                    self.place_ship(r_0,c_0,r_1,c_1)
            print(self)
    
    

    def aiGuess(self):
        """Make a guess (random from list). Removes that guess from the list 
        so AI doesn't guess it again, and if there is a hit, then in the 
        next move it should check the four cardinal directions adjacent 
        to that point. (makes a list of those and choose randomly between them)
        Keeps guessing from those 4 directions until it gets another hit,
        which means it's figured out the orientation of the ship. Then check that
        direction and the direction on the opposite side (eg if north is a hit
        then check south as well, if east is a hit then check west as well) in case
        it hit in the middle of the ship. Keep guessing in those directions until
        it sinks the ship. Otherwise, if there has been no hit, then it guesses randomly."""
        
        
        list_HitTrue = []
        #Need a call to the hit register function here
        #Check if there's a hit, and look at the coordinates of that hit
        #If there is a hit, save the cardinal direction coordinates around that hit in a list: 
        #[(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        #Make a random guess from that list for the next move, and subtract that coordinate from 
        # both the mini-hit list and the overall available guesses list

        #else statement: if no move is advantageous (e.g. no hit), resort to random choice
        guess_location = random.choice(range(len(self.available_guesses)))
        guess = self.available_guesses[guess_location]
        print("I'll guess", guess, "!")
        self.available_guesses.remove(guess)
        print(self.available_guesses)
        return guess



    

