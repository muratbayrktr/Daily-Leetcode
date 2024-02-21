// Solution for 78. Subsets
// link: https://leetcode.com/problems/subsets/description/

import java.util.ArrayList;
import java.util.List;


// ALTERNATIVE SOLUTION, WORKS SLOWER THAN MAIN SOLUTION
// BUT I LIKED THE WAY OF THINKING

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i=0 ; i<Math.pow(2,nums.length)  ;i++)
            result.add(new ArrayList<>());

        int stepCounter = result.size()/2;
        for (int number : nums) {
            int writeCounter = stepCounter;
            int waitCounter = 0;
            for (int index=0; index<result.size(); index++) {
                if (waitCounter==0) {
                    result.get(index).add(number);
                    writeCounter -= 1;
                    if (writeCounter==0)
                        waitCounter=stepCounter;
                } else {
                    waitCounter -= 1;
                    writeCounter = stepCounter;
                }
            }
            stepCounter/=2;
        }

        return result;
    }
}