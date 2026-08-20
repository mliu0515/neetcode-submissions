class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::set<string> operators = {"+", "-", "*", "/"};
        std::stack<int> stack;

        for (const string& c : tokens) {
            if (operators.count(c)) {
                int second = stack.top(); stack.pop();
                int first = stack.top(); stack.pop();
                if (c == "+") {
                    stack.push(first + second);
                } else if (c == "-") {
                    stack.push(first - second);
                } else if (c == "*") {
                    stack.push(first * second);
                } else if (c == "/") {
                    stack.push(first / second);
                }
            } else {
                stack.push(std::stoi(c));
            }
        }
        return stack.top();
    }
};
