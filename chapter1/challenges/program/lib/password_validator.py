# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

def is_valid(password):
    sym_list = ["!","@","$","%","&"]
    if len(password) > 7 and any(i in sym_list for i in password):
        print("wow")
        return True
        
    else:
        print("fail")
        return False
        
    
is_valid("passworddjgv")
        