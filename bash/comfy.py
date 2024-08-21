import sys
from separator import paragraph_to_command_execution
from interpreter import command_separated
from execute import execute_command
from read_file import read_file

# Work sequence 
#   Paragraph + paragraph_to_command_execution = command_list_list
#   command_list_list + execute_sequence = executed code blocks
system_variable = sys.argv
paragraph = " ".join(system_variable[1:])

if '.comfy' in sys.argv[1]:
    paragraph = read_file(sys.argv[1])

# Run separator - input: paragraph & output: list of list of commands to be run sequentially & in parallel

commands = paragraph_to_command_execution(paragraph)
print('commands are: ', commands)
# Onterpreter & Code execution

def execute_sequence(command_list_list):
    for command_list in command_list_list:
        print('command list: ', command_list)
        for command in command_list:
            separated_command = command_separated(command)
            print('executing ', separated_command)
            execute_command(separated_command)

execute_sequence(commands)