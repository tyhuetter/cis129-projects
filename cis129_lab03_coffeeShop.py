
print('************************************')
print('My Coffee and Muffin Shop')
coffees = input('Number of coffees bought?\n')
coffees = int(coffees)
muffins = input('Number of muffins bought?\n')
muffins = int(muffins)
hotchocolates = input('Number of hot chocolates bought?\n')
hchoc = int(hotchocolates)
sandwiches = input('Number of sandwiches bought? \n')
swich = int(sandwiches)

coffeecost = coffees * 5
muffincost = muffins * 4
hchoccost = hchoc * 3
swichcost = swich * 6
tax = (coffeecost + muffincost + hchoccost + swichcost) * 0.06
totalcost = coffeecost + muffincost + hchoccost + swichcost + tax 
print('************************************')
print('                                     ')                                   
print('************************************')
print('My Coffee and Muffin Shop Receipt')
print(' ')
print('', coffees, 'coffees for $5 each: $ ', coffeecost, '')
print('', muffins,' muffins for $4 each: $ ', muffincost, '')
print('', hchoc,' hotchocolates for $3 each: $ ', hchoccost, '')
print('', swich,' sandwiches for $6 each: $ ', swichcost, '')
print('6% tax : $ ', tax,'')
print('-------------')
print('Total: $ ', totalcost, '')
print('***********************************')
print(' ')
print('Thank you for stopping by, have a wonderful day!')
print('    ')
print("USE THIS CODE FOR A FREE COFFEE NEXT VISIT: '7dclts53i'")




