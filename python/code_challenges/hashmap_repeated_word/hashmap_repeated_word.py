
def hashmap_repeated_word(string):
    cleaned_string = string_cleaner(string)
    mod_string = cleaned_string.split()
    if len(mod_string) == 1:
        return mod_string[0]

    mod_string_dict = dict.fromkeys(set(mod_string),0)
    for word in mod_string:
        mod_string_dict[word] += 1
        if 2 in mod_string_dict.values():
            return word

    return mod_string


def string_cleaner(string):
    new_string = string.lower()
    punctuation = '''!()-[]};:{'",<>\\./?@#$%^&*_~''' # also import string --> string.punctuation
    no_punctuation = ''
    for char in new_string:
       if char not in punctuation:
        no_punctuation = no_punctuation + char
    return no_punctuation
