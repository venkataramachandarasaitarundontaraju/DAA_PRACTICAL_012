def tsp(cost, n):
    memo = {}
    
    def g(i, s):
        if not s:
            return cost[i][0]
        
        if (i, s) in memo:
            return memo[(i, s)]
        
        ans = float('inf')
        
        for j in s:
            remaining = tuple(x for x in s if x != j)
            ans = min(ans, cost[i][j] + g(j, remaining))
            
        memo[(i, s)] = ans
        return ans

    s = tuple(range(1, n))
    return g(0, s)

# Standard 4-city cost matrix for validation
matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

num_cities = len(matrix)
result = tsp(matrix, num_cities)
print(result)
