#!/usr/bin/env python3

allgenes = open('alpaca_all_genes.tsv','r')
stemgenes = open('alpaca_stemcellproliferation_genes.tsv','r')
piggenes = open('alpaca_pigmentation_genes.tsv','r')
nonstem = open('alpaca_nonstem_genes.tsv','w')
pigstem = open('alpaca_pigstem_genes.tsv','w')
all_li = []
stem_li = []
pig_li = []

for line in allgenes:
	line = line.rstrip()
	all_li.append(line)
all_li.pop(0)

for line in stemgenes:
	line = line.rstrip()
	stem_li.append(line)
stem_li.pop(0)

for line in piggenes:
	line = line.rstrip()
	pig_li.append(line)
pig_li.pop(0)

set_all = set(all_li)
set_stem = set(stem_li)
set_pig = set(pig_li)

nonstem = set_all - set_stem
pigstem = set_pig & set_stem

print(nonstem)
print(pigstem)
