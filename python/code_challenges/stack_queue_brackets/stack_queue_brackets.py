# Write a function called validate brackets
# Arguments: string
# Return: boolean
# representing whether or not the brackets in the string are balanced
import re

regex_list = [r'[(][)]',r'[[][]]',r'[{][}]',r'[(]\w+[)]',r'[[]\w+[]]',r'[{]\w+[}]']


def stack_queue_brackets(str):
    valid_list = []
    for valid_item in regex_list:
        pattern = re.compile(valid_item)
        if pattern.match(str):

            valid_list.append(True)
        valid_list.append(False)
        print(valid_list)
    if True in valid_list:
        return True
    return False

stack_queue_brackets('[]')
