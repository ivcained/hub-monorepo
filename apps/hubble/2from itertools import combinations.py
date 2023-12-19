from itertools import combinations

def combine(nums, mod):
    result = 1
    for num in nums:
        result = (result * num) % mod
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_combinations(data, prime_modulus):
    valid_combinations = []

    for combo in combinations(data, 6):
        ids, magic = zip(*combo)
        nums = [id * magic for id, magic in combo]
        product = combine(nums, prime_modulus)

        if is_prime(product):
            valid_combinations.append(combo)

    return valid_combinations

data = [[1, 630042791],[2, 1696708182],[3, 1696546177],[4, 629274640],[5, 1185099359],[6, 387740542],[7, 564812136],[8, 990848323],[9, 267748251],[10, 852704412]]
modulus = 2147483647

valid_combinations = find_combinations(data, modulus)

if valid_combinations:
    for combo in valid_combinations:
        print("Valid combination:", combo)
else:
    print("No valid combinations found")