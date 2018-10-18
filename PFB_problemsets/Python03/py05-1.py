#!/usr/bin/env python3

fav = {'food':'jellybeans', 'book':'No Clue', 'organism':'Nematostella'}
fav_keys = list(fav.keys())

print('I have many favorite things, including:', fav_keys[0], fav_keys[1], fav_keys[2])

str = input('Enter one of these to see my favorite:')
print('My favorite', str ,'is ', fav[str]) 







