'''
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
'''


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex_sum = 0
        lee_sum = 0
        alex_pointers = [0,len(piles)-1]
        return self.alex_can_win(piles,alex_sum, lee_sum,alex_pointers)
    
    def alex_can_win(self,piles,current_alex_sum,current_lee_sum,alex_pointers):
        if alex_pointers[0] >= alex_pointers[1]:
            alex_sum = current_alex_sum + piles[alex_pointers[0]]
            if alex_sum > current_lee_sum:
                return True
            else:
                return False
            
        if (alex_pointers[1] - alex_pointers[0]) == 1:
            alex_sum = current_alex_sum + piles[alex_pointers[0]]
            lee_sum = current_lee_sum + piles[alex_pointers[1]]
            if alex_sum > lee_sum:
                return True
            
            alex_sum = current_alex_sum + piles[alex_pointers[1]]
            lee_sum = current_lee_sum + piles[alex_pointers[0]]
            if alex_sum > lee_sum:
                return True
            return False
        
        alex_sum = piles[alex_pointers[0]] + current_alex_sum
        lee_sum = piles[alex_pointers[0]+1] + current_lee_sum
        alex_new_pointers = [alex_pointers[0]+2,alex_pointers[1]]
        can_alex_win = self.alex_can_win(piles,alex_sum,lee_sum,alex_new_pointers)
        if can_alex_win is True:
            return True
        
        alex_sum = piles[alex_pointers[0]] + current_alex_sum
        lee_sum = piles[alex_pointers[1]] + current_lee_sum
        alex_new_pointers = [alex_pointers[0]+1,alex_pointers[1]-1]
        can_alex_win = self.alex_can_win(piles,alex_sum,lee_sum,alex_new_pointers)
        if can_alex_win is True:
            return True
        
        alex_sum = piles[alex_pointers[1]] + current_alex_sum
        lee_sum = piles[alex_pointers[0]] + current_lee_sum
        alex_new_pointers = [alex_pointers[0]+1,alex_pointers[1]-1]
        can_alex_win = self.alex_can_win(piles,alex_sum,lee_sum,alex_new_pointers)
        if can_alex_win is True:
            return True
        
        alex_sum = piles[alex_pointers[1]] + current_alex_sum
        lee_sum = piles[alex_pointers[1]-1] + current_lee_sum
        alex_new_pointers = [alex_pointers[0],alex_pointers[1]-2]
        can_alex_win = self.alex_can_win(piles,alex_sum,lee_sum,alex_new_pointers)
        if can_alex_win is True:
            return True
        return False
        
        
            
        
