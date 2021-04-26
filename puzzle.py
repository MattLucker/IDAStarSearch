from dict import colors


class cube:
    """
    DESC: Creates a 2x2x2 cube object with all sides solved.
    """
    def __init__(self):
        self.cube = []
        self.scramble = []
        self.cubeSolved = []
        self.clean()


    def clean(self):
        """
        DESC: Creates a solved state cube.
        """
        for i in range(24):
            self.cube.append(i)
            self.cubeSolved.append(i)


    def save(self):
        """
        DESC: Remembers a specific state of the cube to be able to revert back to.
        """
        self.scramble = []
        for num in self.cube:
            self.scramble.append(num)


    def reset(self):
        """
        DESC: Reverts cube back to saved state.
        """
        self.cube = []
        for num in self.scramble:
            self.cube.append(num)


    def solved(self):
        """
        DESC: Checks to see if the cube is solved.
        IN:   self
        RET:  True for a solved cube and False for an unsolved cube
        solvedState = []
        for num in self.cube:
            solvedState.append(colors[num])
        for i in range(0,24,4):
            for ii in range(1,4):
                if solvedState[i] != solvedState[i+ii]:
                    return False
        return True
        """
        if self.cube == self.cubeSolved:
            return True
        return False




    def display(self):
        """
        DESC: Displays the cube in the terminal with the given format:
             y y                   00 01
             y y                   02 03
         o o b b r r g g    04 05  08 09  12 13  16 17
         o o b b r r g g    06 07  10 11  14 15  18 19
             w w                   20 21
             w w                   22 23
        IN:   self
        RET:  None
        """
        sequence = [0,1,2,3,4,5,8,9,12,13,16,17,6,7,10,11,14,15,18,19,20,21,22,23]
        line = ""
        for num in sequence:
            if num in [0,2,20,22]:
                line += "     "
            else: line += " "
            line += colors[self.cube[num]]
            if num in [1,3,17,19,21]:
                line += "\n"
        print(line)


    def decode(self, text, safe = True):
        """
        DESC: Turns any string and turns it into an algorithm the cube can
              read if it is a valid algorithm.
        IN:   string alg
        RET:  array alg
        """
        alg = text.split()
        if safe:
            for move in alg:
                if move not in ("r","rp","l","lp","u","up","d","dp","f","fp","b","bp","r2","l2","u2","d2","f2","b2"):
                    print(move + " is not a valid turn.")
                    return ["null"]
        return alg


    def h(self):
        """
        DESC: Determines a heuristic score of the current cube state based on a
              sum of how many turns all corners need before being in their correct positions.
              Max: 16, Min: 0
        IN:   None
        RET:  score
        """
        score = 0
        if self.cube[0] != 0:
            possiblePositions0 = [1,2,3,8,20,19,6,13,23]
            found = False
            for option in possiblePositions0:
                if 0 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        if self.cube[1] != 1:
            possiblePositions1 = [0,2,3,9,21,18,4,15,22]
            found = False
            for option in possiblePositions1:
                if 1 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        if self.cube[2] != 2:
            possiblePositions2 = [0,1,3,10,22,17,7,12,21]
            found = False
            for option in possiblePositions2:
                if 0 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        if self.cube[3] != 3:
            possiblePositions3 = [0,1,2,11,23,16,5,14,20]
            found = False
            for option in possiblePositions3:
                if 0 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        if self.cube[20] != 20:
            possiblePositions20 = [21,22,23,0,8,19,3,5,14]
            found = False
            for option in possiblePositions20:
                if 0 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        if self.cube[21] != 21:
            possiblePositions21 = [20,22,23,1,9,18,2,7,12]
            found = False
            for option in possiblePositions21:
                if 0 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        if self.cube[22] != 22:
            possiblePositions22 = [20,21,23,2,10,17,1,4,15]
            found = False
            for option in possiblePositions22:
                if 0 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        if self.cube[23] != 23:
            possiblePositions23 = [20,21,22,3,11,16,0,6,13]
            found = False
            for option in possiblePositions23:
                if 0 == self.cube[option]:
                    score += 1
                    found = True
                    break
            if not found:
                score += 2
        return score


    def execute(self, alg):
        """
        DESC: Executes a specific algorithm.
        IN:   self, alg
        RET:  None
        """
        for move in alg:
            if move == "r":
                self.r_turn()
            elif move == "l":
                self.l_turn()
            elif move == "u":
                self.u_turn()
            elif move == "f":
                self.f_turn()
            elif move == "d":
                self.d_turn()
            elif move == "b":
                self.b_turn()
            elif move == "rp":
                self.rp_turn()
            elif move == "lp":
                self.lp_turn()
            elif move == "up":
                self.up_turn()
            elif move == "fp":
                self.fp_turn()
            elif move == "dp":
                self.dp_turn()
            elif move == "bp":
                self.bp_turn()
            elif move == "r2":
                self.r_turn()
                self.r_turn()
            elif move == "l2":
                self.l_turn()
                self.l_turn()
            elif move == "u2":
                self.u_turn()
                self.u_turn()
            elif move == "f2":
                self.f_turn()
                self.f_turn()
            elif move == "d2":
                self.d_turn()
                self.d_turn()
            elif move == "b2":
                self.b_turn()
                self.b_turn()


    def swap(self, i, j):
        """
        DESC: Helper function for turn functions to swap two colors on a piece.
        IN:   self, side1, index1, side2, index2
        RET:  None
        """
        temp = self.cube[i]
        self.cube[i] = self.cube[j]
        self.cube[j] = temp


    def f_turn(self):
        """
        DESC: Executes a single turn move. Same for the following functions
        IN:   None
        RET:  None
        """
        self.swap(8,9)
        self.swap(8,11)
        self.swap(8,10)
        self.swap(2,12)
        self.swap(2,21)
        self.swap(2,7)
        self.swap(3,14)
        self.swap(3,20)
        self.swap(3,5)


    def fp_turn(self):
        self.swap(8,10)
        self.swap(8,11)
        self.swap(8,9)
        self.swap(2,7)
        self.swap(2,21)
        self.swap(2,12)
        self.swap(3,5)
        self.swap(3,20)
        self.swap(3,14)

    def r_turn(self):
        self.swap(12,13)
        self.swap(12,15)
        self.swap(12,14)
        self.swap(3,16)
        self.swap(3,23)
        self.swap(3,11)
        self.swap(1,18)
        self.swap(1,21)
        self.swap(1,9)

    def rp_turn(self):
        self.swap(12,14)
        self.swap(12,15)
        self.swap(12,13)
        self.swap(3,11)
        self.swap(3,23)
        self.swap(3,16)
        self.swap(1,9)
        self.swap(1,21)
        self.swap(1,18)

    def u_turn(self):
        self.swap(0,1)
        self.swap(0,3)
        self.swap(0,2)
        self.swap(17,13)
        self.swap(17,9)
        self.swap(17,5)
        self.swap(16,12)
        self.swap(16,8)
        self.swap(16,4)

    def up_turn(self):
        self.swap(0,2)
        self.swap(0,3)
        self.swap(0,1)
        self.swap(17,5)
        self.swap(17,9)
        self.swap(17,13)
        self.swap(16,4)
        self.swap(16,8)
        self.swap(16,12)

    def l_turn(self):
        self.swap(4,5)
        self.swap(4,7)
        self.swap(4,6)
        self.swap(0,8)
        self.swap(0,20)
        self.swap(0,19)
        self.swap(2,10)
        self.swap(2,22)
        self.swap(2,17)

    def lp_turn(self):
        self.swap(4,6)
        self.swap(4,7)
        self.swap(4,5)
        self.swap(0,19)
        self.swap(0,20)
        self.swap(0,8)
        self.swap(2,17)
        self.swap(2,22)
        self.swap(2,10)

    def b_turn(self):
        self.swap(16,17)
        self.swap(16,19)
        self.swap(16,18)
        self.swap(1,4)
        self.swap(1,22)
        self.swap(1,15)
        self.swap(0,6)
        self.swap(0,23)
        self.swap(0,13)

    def bp_turn(self):
        self.swap(16,18)
        self.swap(16,19)
        self.swap(16,17)
        self.swap(1,15)
        self.swap(1,22)
        self.swap(1,4)
        self.swap(0,13)
        self.swap(0,23)
        self.swap(0,6)

    def d_turn(self):
        self.swap(20,21)
        self.swap(20,23)
        self.swap(20,22)
        self.swap(10,14)
        self.swap(10,18)
        self.swap(10,6)
        self.swap(11,15)
        self.swap(11,19)
        self.swap(11,7)

    def dp_turn(self):
        self.swap(20,22)
        self.swap(20,23)
        self.swap(20,21)
        self.swap(10,6)
        self.swap(10,18)
        self.swap(10,14)
        self.swap(11,7)
        self.swap(11,19)
        self.swap(11,15)


if __name__ == "__main__":

    text = "f b2 f2 d b bp"
    alg = text.split()
    puzzle = cube()
    puzzle.execute(alg)
    print(puzzle.h())
