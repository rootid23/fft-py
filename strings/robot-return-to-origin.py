
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        #x,y = R (x+1,y), L (x-1,y) , U (x,y+1) D - (x, y-1)
        # magnitude is same i.e. cuts the unit distance
        # How big the move?
        # Distance among each move?
        # Ida
        #1. Scan each move and update the position return true if reached to same origin
        #T - O(n)
        #2. Count # of U,D,R and L if U == D and R == L return true

        #w/ using the constraints in the problem
        if(len(moves) == 0) : return True
        return True if moves.count('R') == moves.count('L')
                    and moves.count('U') == moves.count('D') else False

        #w/ map
        aux_map = { 'R' : (1,0), 'L' : (-1, 0), 'U' : (0,1), 'D' : (0, -1) }
        loc = [0,0]
        for move in moves :
            cord = aux_map[move]
            loc[0] += cord[0]
            loc[1] += cord[1]
        return True if loc == [0,0] else False


#Robot Return to Origin
#There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its
#moves, judge if this robot ends up at (0, 0) after it completes its moves.
#The move sequence is represented by a string, and the character moves[i] represents its ith move.
#Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after
#it finishes all of its moves, return true. Otherwise, return false.
#Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the
#right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's
#movement is the same for each move.
#Example 1:
#Input: "UD"
#Output: true
#Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it
#ended up at the origin where it started. Therefore, we return true.
#
#Example 2:
#Input: "LL"
#Output: false
#Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return
#false because it is not at the origin at the end of its moves.
