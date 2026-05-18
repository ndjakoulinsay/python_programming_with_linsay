# arbitrary list of ages
ages = [25, 30, 35, 25, 40, 30, 45]

# duplicate ages in ages
ages = ages + ages
print("Ages with duplicates:", ages)

# get unique ages
unique_ages = set(ages)
print("Unique ages:", unique_ages)

# check if 25 is in unique ages
print("Is 25 in unique ages?", 25 in unique_ages)

# alternatively
if 25 in unique_ages:
    print("25 is in unique ages.")