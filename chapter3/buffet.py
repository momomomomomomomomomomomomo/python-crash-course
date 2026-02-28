buffet = ('beef', 'chicken', 'fish', 'vegetables', 'fruit')

for meal in buffet:
    print(meal)


# tuples are immutable  
# buffet[0] = 'pork'    

buffet = ('pork', 'lamb', 'salmon', 'tofu', 'fruit')
print("\nNew buffet menu:")
for meal in buffet:
    print(meal)