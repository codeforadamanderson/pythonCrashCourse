sandwich_orders = ['hogi', 'pb&j', 'po boy', 'turkey club']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made your {sandwich} sandwich and probably didn't taste it.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made and probably not tasted first:")
for prepared_sandwich in finished_sandwiches:
    print(prepared_sandwich.title())