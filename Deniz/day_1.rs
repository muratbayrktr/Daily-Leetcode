impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        let opening = ['(', '[', '{'];
        let closing = [')', ']', '}'];

        for c in s.chars() {
            if opening.contains(&c) {
                stack.push(c);
            } else {
                match stack.pop() {
                    Some(top) => {
                        let index_open = opening.iter().position(|&x| x == top);
                        let index_close = closing.iter().position(|&x| x == c);
                        if index_open != index_close {
                            return false;
                        }
                    },
                    None => return false,
                }
            }
        }

        stack.is_empty() 
    }
}