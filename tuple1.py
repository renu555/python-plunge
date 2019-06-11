//Remove empty tuples
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
tuples = [t for t in tuples if t]
print(tuples)
