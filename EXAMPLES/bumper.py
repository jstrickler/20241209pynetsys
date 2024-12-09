def mk_bumper(bump_amount): # Define outer function -- this will return the function to use
    def bump(n): # Define inner function -- this will be the function actually used
        return n + bump_amount # Inner function returns increased by stored bump amount (parameter, and thus local variable, to mk_bumper()
    return bump # Outer function returns inner function

a = mk_bumper(1)  # Call outer function to get an instance of the inner function which "knows" the bumper and saves the inner function in a variable
b = mk_bumper(1000)
c = mk_bumper(37)

print(a(5)) # Call the created copy of the inner function, which increments its argument by the bump amount
print(b(5))
print(c(5))
