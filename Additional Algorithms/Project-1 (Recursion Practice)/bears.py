
# Given integer n, returns True or False based on reachability of goal
# See write up for "rules" for bears
def bears(n: int) -> bool:
    
    if n == 42:
        return True

    if n % 5 == 0 and n > 42:
        if (bears(n-42)):
            return True

    if n % 3 == 0 or n % 4 == 0 and n > 42:
        last_two = (n % 10) * ((n % 100) // 10)
        if (last_two != 0):
            if(bears(n - last_two)):
                return True
        
    if n % 2 == 0 and n > 42:
        if(bears(n//2)):
            return True

    return False