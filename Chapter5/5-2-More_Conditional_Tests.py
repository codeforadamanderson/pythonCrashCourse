cheese = 'string cheese'
print("Should print True, then False:")
print(cheese == 'string cheese')
print(cheese == 'gouda')

instrument = 'sTrInGeD iNsTrUmEnT'
print("\nShould print True, then False:")
print(instrument.lower() == 'stringed instrument')
print(instrument == 'stringed instrument')

senior_age = 55
print("\nIs 55 year old eligible for senior coffee?  Should print True.")
print(senior_age >= 55)

kid_age1 = 93
kid_age2 = 37
print("\nCan 93 year old have happy holiday?  Should print False.")
print(kid_age1 >= 1 and kid_age1 <= 92)
print("Can 37 year old have happy holiday?  Should print True.")
print(kid_age2 >= 1 and kid_age2 <= 92)

pizza_topping1 = 'banana'
pizza_topping2 = 'pineapple'
print(f"\nIs {pizza_topping1} and acceptable pizza topping?")
print(pizza_topping1 == 'mushroom' or pizza_topping1 == 'pineapple')
print(f"Is {pizza_topping2} an acceptable pizza topping?")
print(pizza_topping2 == 'mushroom' or pizza_topping2 == 'pineapple')

star_trek_captains = ['kirk', 'picard', 'sisko', 'janeway', 'archer']
captain1 = 'sOlo'
captain2 = 'siSko'
print(f"\nIs Captain {captain1.capitalize()} a Star Trek captain?")
print(captain1.lower() in star_trek_captains)
print(f"Is Captain {captain2.capitalize()} a Star Trek captain?")
print(captain2.lower() in star_trek_captains)