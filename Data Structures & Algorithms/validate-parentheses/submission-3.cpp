class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char, char> correctPair = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };

        for (char c: s) {
            if (correctPair.count(c)) {
                stack.push(c);
            } else {
                if (stack.empty() || correctPair[stack.top()] != c) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.size() == 0;
    }
};
