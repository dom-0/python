import itertools


print(list(itertools.combinations(numbers, 2))) # will contain uniques without repeating the same number

print(list(itertools.combinations_with_replacement(numbers, 2))) # will contain aaa, bbb

print(list(itertools.permutations(numbers, 2))) # will contain a,b and b,a

print(list(itertools.product(numbers, 2))) # will contain a,b and b,a and aa bb