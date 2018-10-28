# Tuples are immutable

fullname = "Neelkanth Kaushik"
tuple = (999, "Neelkanth", fullname, (1, 2, 3, 4, 5))
print tuple  # (999, 'Neelkanth', 'Neelkanth Kaushik', (1, 2, 3, 4, 5))
print tuple[0]  # 999
print tuple[2]  # Neelkanth Kaushik
print tuple[0:3]  # (999, 'Neelkanth', 'Neelkanth Kaushik')
print 'Neelkanth' in tuple  # True
print len(tuple)  # 4
print tuple.index(fullname)  # 2
tuple2 = tuple[0:2]
print tuple2  #(999, 'Neelkanth')
