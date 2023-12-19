from math import factorial
def chinese_remainder(ids, magic_nums):
    n = len(ids)
    # Convert IDs and magic numbers to binary strings
    ids = [bin(i)[2:] for i in ids]
    magic_nums = [''.join(reversed(b)) if b[0] == '1' else b for b in magic_nums]
    # Perform modulo 2^32 arithmetic on IDs and magic numbers
    ids += [f'{i:0<32}0'*(len(ids) - i - 1) for i in range(n)]
    magic_nums = [''.join([str(int(b, 2))[j:] for j in range(8) if b[j] != "1"]) for b in magic_nums]
    ids = [int(i, 2) for i in ids]
    magic_nums = [int(''.join([str(x) for x in num])) for num in magic_nums]
    # Calculate the product of the first three pairs of IDs and magic numbers
    prod = 1
    for i in range(n - 2):
        prod *= ids[i] * magic_nums[i*3 + 1] * magic_nums[i*3 + 2]
    # Calculate the remainder of each pair of IDs modulo 2^32
    remainders = [ids[i] % (2**32) for i in range(n)]
    # Add the remainders together and convert to an integer modulo 2^32 - 1
    result = sum([remainders[j] * factorial(k) // (factorial(j)*factorial(n-j)) % (2**32 - 1)) for j in range(n) for k in range(j+1, n)]) % (2**32 - 1)
    # Divide by the multiplicative inverse modulo 2^32 - 1 to obtain the final answer
    return result // (factorial(n-1)) % (2**32 - 1))
ids = [630042791, 1696708182, 1696546177, 629274640, 1185099359, 387740542, 564812136, 990848323, 267748251, 852704412]
magic_nums = [''.join(reversed(b)) if b[0] == '1' else b for b in [630042791, 1696708182, 1696546177, 629274640, 1185099359, 387740542, 564812136, 990848323, 267748251, 852704412]]
print(chinese_remainder(ids, magic_nums)) 