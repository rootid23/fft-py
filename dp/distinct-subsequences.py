

#What is the subproblem?
#Recurrece relation
#


#So if the first char of s != the first char of t , the answer is obvious:
#return num_distinct(s.substr(1, end), t.substr(1, end))
#else the first char of s == the first char of t , the answer is obvious:
#return num_distinct(s.substr(1, end), t.substr(0, end)) + num_distinct(s.substr(1, end),
#t.substr(1, end))
#Then you can implement it with:
#    Recursive method + memoization
#    Loop with DP

int
numDistinct(char *s, char *t)
{
	char ch, *p;

	ch = *t;
	if (ch == '\0')
		return 1;
	p = strchr(s, ch);
	if (p == NULL)
		return 0;
	++p;
  }



#So if the first char of s != the first char of t , the answer is obvious:
#return num_distinct(s.substr(1, end), t.substr(1, end))
#else the first char of s == the first char of t , the answer is obvious:
#return num_distinct(s.substr(1, end), t.substr(0, end)) + num_distinct(s.substr(1, end),
#t.substr(1, end))
#Then you can implement it with:
#    Recursive method + memoization
#    Loop with DP
	return numDistinct(p, t) + numDistinct(p, t + 1);
}


class Solution(object):
    def numDistinct(self, s, t):
        m, n = map(len, [t, s])
        #s -m > t
        dp = [ [1]  * (n+1) ]
        for i in range(0, m) :
            dp += [ [0] * (n+1) ]

        for i in range(1, m+1) :
            for j in range(1, n+1) :
                if(t[i-1] == s[j-1]) :
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else :
                    dp[i][j] = dp[i][j-1]
        # print(dp)
        return dp[m][n]





#Solution (DP):
#We keep a m*n matrix and scanning through string S, while
#m = T.length() + 1 and n = S.length() + 1
#and each cell in matrix Path[i][j] means the number of distinct subsequences of
#T.substr(1...i) in S(1...j)
#
#Path[i][j] = Path[i][j-1]            (discard S[j])
#             +     Path[i-1][j-1]    (S[j] == T[i] and we are going to use S[j])
#                or 0                 (S[j] != T[i] so we could not use S[j])
#while Path[0][j] = 1 and Path[i][0] = 0.

int numDistinct(string S, string T) {
    int m = T.length();
    int n = S.length();
    if (m > n) return 0;    // impossible for subsequence
    vector<vector<int>> path(m+1, vector<int>(n+1, 0));
    for (int k = 0; k <= n; k++) path[0][k] = 1;    // initialization

    for (int j = 1; j <= n; j++) {
        for (int i = 1; i <= m; i++) {
            path[i][j] = path[i][j-1] + (T[i-1] == S[j-1] ? path[i-1][j-1] : 0);
        }
    }

    return path[m][n];
}


#Distinct Subsequences
#Given a string S and a string T, count the number of distinct subsequences of T in S.
#A subsequence of a string is a new string which is formed from the original string by deleting some
#(can be none) of
#the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is
#a subsequence of
#"ABCDE" while "AEC" is not).
#Here is an example:
#S = "rabbbit", T = "rabbit"
#Return 3.
