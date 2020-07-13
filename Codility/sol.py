class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        i_max = len(self.rooms)
        j_max = len(self.rooms[0])
        for i in range(i_max):
            for j in range(j_max):
                if self.rooms[i][j] is not -1 and self.rooms[i][j] is not 0:
                    self.rooms[i][j] = findGate(self.rooms, (i, j), i_max, j_max)

    def findGate(rooms, *(i, j), i_max, j_max):
        queue = [(i, j)]
        distance = 1
        while queue:
            i, j = queue.popleft()
            room = rooms[i][j]
            if room == 0:
                return distance
            if i+1 < i_max and rooms[i+1][j] is not -1:
                queue.append((i+1, j))
            if j+1 < j_max and rooms[i][j+1] is not -1:
                queue.append((i, j+1))
            if i-1 > -1 and rooms[i-1][j] is not -1:
                queue.append((i-1, j))
            if j-1 > -1 and rooms[i][j-1] is not -1:
                queue.append((i, j-1))
            distance += 1
