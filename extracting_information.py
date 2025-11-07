def extract_information():
        # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    quote="Ask not what your country can do for you - ask what you can do for your country. - John F. Kennedy"
    print(quote.find('John F. Kennedy'))
    # Manipulating Words:
    # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    # a. Extract the word 'subjective' without knowing its exact position.
    # b. Extract every third word.
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    info = "Python is fun. Fun is good. Good is subjective."
    print(info.rfind('subjective'))
    subjective_word =info[36:]
    print(subjective_word)
    every_third_word = info.split()[: :3]
    reversed_word_positions = info.split()[::3]