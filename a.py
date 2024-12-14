n=len(s) 
dp=[[0] * n for _ in range(n)]
max_len=1
start=0
for i in range(n):
    dp[i][i]=1
for i in range(n-1):
    if s[i]==s[i+1]:
        dp[i][i+1]=1
        start=i
        max_len=2

# for i in range(n): 
#     print(dp[i])

for k in range(3,n+1):
    for i in range(n-k+1):
        j=i+k-1
        if dp[i+1][j-1]==True and s[i]==s[i+1]:
            dp[i][j]=True
            if k > max_len: 
                start=i
                max_len=k
return s[start:start+max_len]

        