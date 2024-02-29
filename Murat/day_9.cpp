class Solution {
public:
    
    int climbStairs(int n) {
        int *memo = new int[n+1];
        for (int i=0; i < n+1; i++) {
            memo[i] = -1;
        }
        return helper(n,memo);
    }

    int helper(int n, int* memo) {
        if (n < 1) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (memo[n] != -1) return memo[n];
        
        int result = helper(n-1, memo) + helper(n-2, memo);
        memo[n] = result;
        return result;
    }
};