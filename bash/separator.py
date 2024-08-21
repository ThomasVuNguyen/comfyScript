import sys

paragraph  = sys.argv[1]

def split_string_with_punctuation(paragraph):
    result = []
    current_word = ""
    
    for char in paragraph:
        if char in ".,":
            if current_word:
                result.append(current_word)
                current_word = ""
            result.append(char)
        else:
            current_word += char
    
    if current_word:
        result.append(current_word)
    #result in the form of command1 - , - command2 - . - command 3
    return result

def create_multiple_lists(separated_paragraph):
    result = []
    current_list = []
    
    for item in separated_paragraph:
        if item == '.':
            if current_list:
                result.append(current_list)
                current_list = []
        elif item != ',':
            current_list.append(item)
    
    if current_list:
        result.append(current_list)
    
    return result

def paragraph_to_command_execution(paragraph):
    return create_multiple_lists(split_string_with_punctuation(paragraph))

paragraph_to_command_execution(paragraph)