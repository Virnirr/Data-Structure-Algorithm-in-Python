from typing import List
# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in: str) -> List:
    
    perm_list = []

    for c in str_in:

        if len(str_in) <= 1:
            return [str_in]
        
        new_str = str_in.replace(c, "")
        new_perm = perm_gen_lex(new_str)
        for p in new_perm:
            perm_list.append(c+p)

    return perm_list
