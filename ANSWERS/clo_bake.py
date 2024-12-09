def mkpower(base):
    def n(exp):
        return base ** exp

    return n

f_2 = mkpower(2)
f_10 = mkpower(10)

print(f_2(5))
print(f_2(8))
print(f_2(.5))
print(f_10(7))
print(f_10(0))
