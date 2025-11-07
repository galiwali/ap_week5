def advanced_slice():
        # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    # a. Extract the letters 'hij'.
    # b. Extract every second letter starting from 'a' to 'm'.

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hij=alphabet[7:10]
    hij_index = alphabet.index('hij') # index of substring
    print(f'hij {hij_index}') #7
    every_second_letter = alphabet[0:13:2]