fully_valid = False
len_valid = False
starts_with_two_letters = False
no_periods_spaces_or_punctuation = False
no_numbers_in_the_middle = False
while not fully_valid:
    plate = input("Plate : ")
    if (len(plate) > 1) and (len(plate) < 7):
        len_valid = True
    if plate[0].isalpha() and plate[1].isalpha():
        starts_with_two_letters = True
    no_periods_spaces_or_punctuation = True

    for char in plate:
        if not char.isalnum():
            no_periods_spaces_or_punctuation = False
            break
    if plate[:-3].isalpha():
        no_numbers_in_the_middle = True
    else:
        no_numbers_in_the_middle = False

    if  (len_valid == True) and (starts_with_two_letters == True) and (no_periods_spaces_or_punctuation == True) and (no_numbers_in_the_middle == True):
        fully_valid = True


    if(fully_valid == False):
        print("Invalid.")

print("Valid")

