import sys
import re

paragraph = sys.argv[1]

def split_string_with_punctuation(paragraph):
    # Split the paragraph into sentences
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    result = []
    
    for sentence in sentences:
        # Split each sentence by commas, but keep float numbers intact
        parts = re.split(r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', sentence)
        
        for part in parts:
            # Remove trailing periods
            part = part.rstrip('.')
            if part:
                result.append(part.strip())
        
        # Add a period to mark the end of the sentence
        result.append('.')
    
    return result

def create_multiple_lists(separated_paragraph):
    result = []
    current_list = []
    
    for item in separated_paragraph:
        if item == '.':
            if current_list:
                result.append(current_list)
                current_list = []
        else:
            current_list.append(item)
    
    if current_list:
        result.append(current_list)
    
    return result

def paragraph_to_command_execution(paragraph):
    return create_multiple_lists(split_string_with_punctuation(paragraph))

paragraph_to_command_execution(paragraph)
