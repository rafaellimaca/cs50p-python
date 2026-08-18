def shorten(string):
    output = ""
    for char in string:
        if char.lower() not in "aieou":
            output += char
    return output

def main():
    string = input("Input: ")
    print(f"Output: {shorten(string)}")

if __name__ == "__main__":
    main()