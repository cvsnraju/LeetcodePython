# 1232. Check If It Is a Straight Line
# Easy
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)  == 2:
            return True
        p = coordinates[1][1] - coordinates[0][1]
        q = coordinates[1][0] - coordinates[0][0]
        if p == 0 or q == 0 :
            s = 0
        else:
            s = p/q
            
        for k in range(2,len(coordinates)):
            y = coordinates[k][1] - coordinates[0][1]
            x = coordinates[k][0] - coordinates[0][0]
            if s != y/x:
                return False
        return True