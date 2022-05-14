s = list(map(int, input()))
num_of_block = [0] * 2
before = s[0]
i = 1
while i < len(s):
    if s[i] != before:
        num_of_block[before] += 1
    before = s[i]
    i += 1
num_of_block[s[i-1]] += 1

print(min(num_of_block))
