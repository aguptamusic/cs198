# Building dictionary problem.
# Bleets because Tweets but different.

"""
Lines in file:
hello #omgthere+hi and#idk
as if#omg+#idkwhat

Dictionary:
{
  'omg': ['hello #omgthere', 'as if#omg']
  'idk': ['hi and#idk', '#idkwhat']
}

"""

# Starter Code:
def read_bleets(filename):
    bleets = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()  # remove \n
            pass


    return bleets

# Solution:
def read_bleets(filename):
    bleets = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()  # remove \n
            bleets = line.split('+')
            for bleet in bleets:
              
              # Now dealing with a single bleet, such as 'hello #omgthere'.
              # First, extract the first three characters after the '#'.
              hash = bleet.find('#')
              tag = bleet[hash + 1: hash + 4]

              # Add tag to dictionary:
              if tag not in bleets:
                bleets[tag] = []
              bleets[tag].append(bleet)

    return bleets