for age in range(0, 65, 1):
    if age == 0:
        print str(age) + ": New born"
    elif age > 0 and age <= 12:
        print str(age) + ": Childhood"
    elif age > 12 and age < 18:
        print str(age) + ": Adolescence"
    elif age >= 18 and age <= 59:
        print str(age) + ": Adulthood"
    elif age >= 60:
        print str(age) + ": Senior citizen"
    else:
        print "Old age"
