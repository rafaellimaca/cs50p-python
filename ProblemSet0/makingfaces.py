def main():
    string = input("Enter a string: ")
    string = convert(string)
    print (string)

def convert(word):
    return word.replace(":)","🙂").replace(":(", "🙁")
main()