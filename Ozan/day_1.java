// Solution for 20. Valid Parentheses
// link: https://leetcode.com/problems/valid-parentheses/description/


class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (Character ch : s.toCharArray()) {
            if (List.of('(','[','{').contains(ch)) {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) 
                    return false;
                
                Character topElement = stack.peek();
                boolean validation = (topElement.equals('(') && ch.equals(')'))
                    || (topElement.equals('[') && ch.equals(']'))
                    || (topElement.equals('{') && ch.equals('}'));
                
                if (validation)
                    stack.pop();
                else
                    return false;
            }
        }

        if (stack.isEmpty())
            return true;
        return false;
    }
}