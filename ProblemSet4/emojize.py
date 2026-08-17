import emoji
def main():
    alias = input("Which emote?: ")
    print(emoji.emojize( alias, language = 'alias' ))
main()