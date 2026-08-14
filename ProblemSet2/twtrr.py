string = input("Input: ")
output = ""
for char in string:
    if char.lower() not in "aieou":
        output += char
print (f"Output: {output}")
