from struct import Struct

# short int short short int (native, unsigned)
s = Struct('=ccIHHI')  # define layout of bitmap header

with open('../DATA/chimp.bmp', 'rb') as chimp_in:
    chimp_bmp = chimp_in.read(s.size)  # read the first 14 bytes of bitmap file in binary mode

(sig1, sig2, size, reserved1, reserved2, offset) = s.unpack(chimp_bmp)  # unpack the binary header into individual values

print("signature:", (sig1 + sig2).decode())  # output the individual values
print('size:', size)
print('reserved1:', reserved1)
print('reserved2:', reserved2)
print('offset:', offset)
