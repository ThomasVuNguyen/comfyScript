import sys

#This function breaks down a command into: wake word, object, identification, and action
def command_separated(command):
    # Split the string by spaces and filter out any empty strings
    return [word for word in command.split() if word]

