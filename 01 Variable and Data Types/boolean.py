# Bool values are either True or False
# They are used to represent the truth value of an expression
# Falsy values: False, None, 0, 0.0, 0j, "", [], (), {}
# Rather than anything else is truthy

is_active = True
print(is_active)
print(type(is_active))

# False
age = 0
print(bool(age)) # False

# Boolean operators
# and, or, not
# or: if any of the operands is True, then the expression evaluates to True, otherwise it evaluates to False
# True or True = True
# True or False = True
# False or True = True
# False or False = False