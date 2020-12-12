foo = "kdjbgfYGSF928754"

for char in foo:
    if char in ["a","b","c"]:
        pass
        # do something

# \/

for char in foo:
    if char in "abc":
        pass
        # do something

# \/

print(all((char in "abc") for char in foo))

# \/

print([(char in "abc") for char in foo])
