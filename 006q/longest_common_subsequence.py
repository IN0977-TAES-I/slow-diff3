class Solution:
    """ Function to calculate the length
    of the Longest Common Subsequence"""
    def lcs(self, str1, str2):
        n = len(str1)
        m = len(str2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Initialize the base cases
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(m + 1):
            dp[0][i] = 0

        # Fill in the DP table to calculate length of LCS
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                
                # Characters match, increment LCS length
                if str1[ind1 - 1] == str2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        
        # Return the length of Longest Common Subsequence
        print("DP Table:")
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                print(dp[ind1][ind2], end=" ")
            print()
        return dp[n][m]

if __name__ == "__main__":
    s1 = "ABCXYD"
    s2 = "AWXCDY"

    
    # Create an instance of Solution class
    sol = Solution()
    
    # Call the function to find and output
    print("Texto I", s1);
    print("Texto 2", s2);
    print("The Length of Longest Common Subsequence is", sol.lcs(s1, s2))
