#Define a list of anything.
captains = ['Kirk', 'Picard', 'Sisko', 'Janeway', 'Archer']

#Print the original list for reference.
print("The original list:")
print(captains)

#Use pop.
poppedCaptain = captains.pop()
print(f"\nThe popped captain is {poppedCaptain}.")
print("\nNew list:")
print(captains)

#Use insert.
print(f"\nInserting {poppedCaptain} back into list.")
captains.insert(4, poppedCaptain)
print("\nList after insert:")
print(captains)

#Use remove.
print("\nRemoving Archer.")
captains.remove('Archer')
print("\nNew list:")
print(captains)

#Use len.
print("\nNumber of Star Trek captains (nope, not forgetting anything):")
print(len(captains))
