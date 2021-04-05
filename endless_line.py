import readchar

n = 0

# Return a string composed by n spaces
def spaces(n):
    return "".join([" "]*n)

while True: 
    # Read input
    c = readchar.readchar()
    
    # Down-left
    if c == "a" and n > 0:
        n -= 1
        print(spaces(n) + "/")
    
    # Down
    elif c == "s" or (c == "a" and n == 0):
        print(spaces(n) + "|")
        
    # Down-right
    elif c == "d":
        n += 1
        print(spaces(n) + "\\")
    else:
        break