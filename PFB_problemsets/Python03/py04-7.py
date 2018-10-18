list6 = [101,2,15,22,95,33,2,27,72,15,52]
evenlist6 = []
oddlist6 = []

for x in list6:
	if x % 2 == 0:
		evenlist6.append(x)
	else:
		oddlist6.append(x)


evensum = 0
for x in evenlist6:
	evensum += x
print(evensum)

oddsum = 0
for x in oddlist6:
	oddsum += x
print(oddsum)


