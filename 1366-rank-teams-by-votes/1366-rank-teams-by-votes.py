class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rank = [[-1 if i!= 26 else chr(j+65) for i in range(27)] for j in range(27)]
        output = ''
        for vote in votes:
            for pos,team in enumerate(vote):
                if rank[ord(team)-65][pos] == -1:  rank[ord(team)-65][pos] = 1  
                else: rank[ord(team)-65][pos] += 1  
        rank =sorted(rank, reverse=True,key = lambda row: tuple(row[i] for i in range(26)))
        for team in rank  : output += team[-1] if team[-1] in votes[0] else ''
        return output