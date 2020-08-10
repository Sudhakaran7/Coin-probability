class Solution(object):
    def probabilityOfHeads(self, prob, target):
        dp = [[0]*(len(prob) + 1) for _ in prob]

        dp[0][0] = 1 - prob[0]
        dp[0][1] = prob[0]

        for i in range(1,len(prob)):
            for j in range(min(target+1,len(prob))):
                if j == 0:
                    dp[i][j] = float(dp[i-1][j]) * (1 - prob[i])
                    continue
                dp[i][j] = float(dp[i-1][j-1]) * prob[i] + float(dp[i-1][j]) * (1 - prob[i])
        return dp[-1][target]

val=Solution()
n,target=map(int,input().split())
prob=list(map(float,input().split()))
print(val.probabilityOfHeads(prob,target))
