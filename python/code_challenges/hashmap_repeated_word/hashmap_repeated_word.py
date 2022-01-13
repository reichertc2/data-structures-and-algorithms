import re

def hashmap_repeated_word(string):
    new_string = string.lower()
    punctuation = '''!()-[]};:{'",<>\\./?@#$%^&*_~'''
    no_punctuation = ''
    for char in new_string:
       if char not in punctuation:
        no_punctuation = no_punctuation + char
    mod_string = no_punctuation.split()
    if len(mod_string) == 1:
        return mod_string[0]

    # for item in new_list:
    #     if re.compile(item):
    #         pass

    # for word in new_list:
    #     word.lower()



    # create list of words in string
    # compare lists to match first word pair
    return mod_string
