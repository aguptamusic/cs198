def first_chars(strs):
    """
    Takes a list of strings and creates a dictionary
    mapping unique first letters of the strings to the frequency that
    they are first letters in the strings. 
    """
    counts = {}
    for s in strs:
        first_char = s[0]
        if first_char not in counts:
            counts[first_char] = 0
        counts[first_char] += 1
    return counts

    # OR #
    """
        if first_char not in counts:
            counts[first_char] = 1
        else:
          counts[first_char] += 1
    return counts
    """


words = ['stanford', 'py', 'charm', 'python']
first_char_counts = first_chars(words)
print(first_char_counts)
