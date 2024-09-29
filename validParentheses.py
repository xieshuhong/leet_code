

def isValid(s):
        stack = []
        # Dictory to hold the mappings of closing to opening brackets
        mapping = {')' : '(', '}' :'{', ']': '['}
        
        for char in s:
            print('char', char)
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                print('top_element', top_element)
                
                if mapping[char] != top_element:
                    return False
                
            else: 
                stack.append(char)
                    
        return not stack

s = "([{}])"
print(isValid(s)) # Output: True
# s = "([)]"
# print(isValid(s)) # Output: False
    
    