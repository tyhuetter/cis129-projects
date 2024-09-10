print('************************************')
print('My Coffee and Muffin Shop')
coffees = input('Number of coffees bought?\n')
coffees = int(coffees)
muffins = input('Number of muffins bought?\n')
muffins = int(muffins)

coffeecost = coffees * 5
muffincost = muffins * 4
tax = (coffeecost + muffincost) * 0.06
totalcost = coffeecost + muffincost + tax 
print('************************************')
print('                                     ')                                   
print('************************************')
print('My Coffee and Muffin Shop Receipt')
print(' ')
print('', coffees, 'coffees for $5 each: $ ', coffeecost, '')
print('', muffins,' muffins for $4 each: $ ', muffincost, '')
print('6% tax : $ ', tax,'')
print('-------------')
print('Total: $ ', totalcost, '')
print('***********************************')


