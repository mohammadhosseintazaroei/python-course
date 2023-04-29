letters = ["a","c", "b","s", "c"]

# Add
letters.append("d")
print(letters)

letters.insert(0, "d")
print(letters)

# Remove
letters.pop()
result = letters.pop(1)
print(letters)
print(result)

letters.remove("b")
print(letters)

if "c" in letters:
    letters.remove("c")
print(letters)

del letters[0]
print(letters)

letters.clear()
print(letters)
