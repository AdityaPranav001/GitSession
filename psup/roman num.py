def romannum(s):
    
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C':100, 'M':1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
       
        current_value = roman_to_int[s[i]]
        
        if i < n - 1 and current_value < roman_to_int[s[i + 1]]:
            total -= current_value
        else:
            total += current_value
    
    return total

print(romannum("III"))
print(romannum("II"))
print(romannum("MMVI"))
