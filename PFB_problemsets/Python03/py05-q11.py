#!/usr/bin/env python3


a = {3,14,15,9,26,5,35,9}
b = {60, 22, 14, 0, 9}

Diff = a - b
Shared = a & b
Total = a | b
SymmDiff = a ^ b

print(Diff)
print(Shared)
print(Total)
print(SymmDiff)

