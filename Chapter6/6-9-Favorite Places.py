favorite_places = {
    'Joe': ['kokomo', 'aruba', 'jamaica'],
    'John': ['pizza hut', 'krispy kreme'],
    'Jane': ['lorien', 'narnia', 'hogwarts'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")