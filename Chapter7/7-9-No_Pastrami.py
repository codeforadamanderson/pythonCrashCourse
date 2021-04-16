sandwich_orders = [
    'hogi', 'pastrami', 'pb&j', 'pastrami', 'po boy', 'pastrami', 'turkey club'
    ]

print("\nThe following orders have been placed:")
for sandwich in sandwich_orders:
    print(sandwich.title())

print("\nThe deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nThe following sandwich orders are finished:")
for sandwich in sandwich_orders:
    print(sandwich.title())
