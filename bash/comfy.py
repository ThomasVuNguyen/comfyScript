import sys
from separator import paragraph_to_command_execution
from interpreter import command_separated

system_variable = sys.argv
paragraph = " ".join(system_variable[1:])

# Run separator - input: paragraph & output: list of commands to be run sequentially & in parallel

commands = paragraph_to_command_execution(paragraph)

# Run intepreter


# Code execution

