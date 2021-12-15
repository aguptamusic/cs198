
### String Loops ###

def alpha_1(s):
    """
    Return the substring starting at the first alpha char and 
    continuing through and including the last digit. 
    Otherwise return the empty string. 

    '^^99abc$$123xx' -> 'abc$$123'
    'abc1' -> 'abc1'
    '1abc' -> ''
    """

    # Find first alphabetitc character
    alpha_idx = 0
    while (alpha_idx < len(s)):
        if s[alpha_idx].isalpha():
            break
        alpha_idx += 1
    
    if (alpha_idx == len(s)):
        return ''
    
    # Find last numeric character
    digit_idx = len(s) - 1
    while (digit_idx >= 0):
        if s[digit_idx].isdigit():
            break
        digit_idx -= 1
    
    # Return substring
    if (alpha_idx < digit_idx):
        return s[alpha_idx:digit_idx + 1]
    else:
        return ''

## Test ##
print(alpha_1('^^99abc$$123xx') == 'abc$$123')
print(alpha_1('abc1') == 'abc1')
print(alpha_1('1abc') == '')