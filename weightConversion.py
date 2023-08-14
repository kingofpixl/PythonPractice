weight = float(input("weight: "))
conversionChecker = input("put K for kg or L for lbs: ")
if conversionChecker.upper == 'L':
    lbsWeight = weight * 0.45359237
    print("Weight in Kg is: " + str(lbsWeight))
elif conversionChecker.upper == 'K':
    kgWeight = weight * 2.2046226218
    print("Weight in lbs is: " + str(kgWeight))
    