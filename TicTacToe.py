class GameBoard:
    boardSpots = [" "] * 9
    turn = 0
    boardWidth = 3

    def startGame(self):
        print("What width of board would you like to play on?")
        while True:
            try:
                width = int(input())
                if width == 0:
                    print("Invalid value, width must be greater than 0.")
                else:
                    print("Width set to " + str(width) + ".")
                    break
            except ValueError:
                print("Invalid input.")
        self.boardWidth = width
        self.boardSpots = [" "] * self.boardWidth**2
        self.turn = 0
        self.printBoard()
        self.promptMove()

    def printBoard(self):
        print("  ", end="")
        for i in range(self.boardWidth):
            print(chr(i+65) + " ", end="")
        print("")
        for i in range(self.boardWidth):
            print(str(i) + " ", end='')
            for j in range(self.boardWidth - 1):
                print(self.boardSpots[i*self.boardWidth+j] + "|", end='')
            print(self.boardSpots[(i+1)*self.boardWidth-1])

    def getActivePlayer(self):
        return ("O", "X")[self.turn == 0]

    def checkWins(self, letter):
        for i in range(0, self.boardWidth):
            if all(self.boardSpots[i+v] == letter for v in range(0, self.boardWidth**2-self.boardWidth+1, self.boardWidth)):
                return True

            if all(self.boardSpots[self.boardWidth*i+v] == letter for v in range(0, self.boardWidth)):
                return True

        if all(self.boardSpots[v] == letter for v in range(0, self.boardWidth**2, self.boardWidth+1)):
            return True

        if all(self.boardSpots[v] == letter for v in range(self.boardWidth-1, self.boardWidth**2-self.boardWidth+1, self.boardWidth-1)):
            return True

        return False

    def promptMove(self):
        print("Player " + ("O", "X")[self.turn == 0] + ", make your move. (Input a single letter and a single number)")
        inp = input().lower().replace(" ", "")
        if len(inp) != 2:
            print("Invalid move.")
            self.promptMove()
        elif ((ord(inp[0]) - 97) not in range(0, self.boardWidth)) or (int(inp[1]) not in range(0, self.boardWidth)):
            print("Invalid move.")
            self.promptMove()
        else:
            self.makeMove(inp)

    def makeMove(self, inp):
        spot = (ord(inp[0]) - 97) + self.boardWidth*int(inp[1])
        if self.boardSpots[spot] == " ":
            self.boardSpots[spot] = self.getActivePlayer()
            if self.checkWins(self.getActivePlayer()):
                self.printBoard()
                print("Player " + self.getActivePlayer() + " wins!!")
                print("Starting a new game.")
                self.startGame()
            else:
                self.turn = (self.turn + 1) % 2
                self.printBoard()
                self.promptMove()
        else:
            print("Invalid move.")
            self.promptMove()

b = GameBoard()
b.startGame()