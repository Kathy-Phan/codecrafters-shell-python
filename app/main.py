import sys, shutil, subprocess, os, shlex

builtin_commands = ["exit", "echo", "type", "pwd", "cd"];

def main():

    while 1: 
        sys.stdout.write("$ ")

        user_input = input()
        tokens = shlex.split(user_input)

        if not tokens:
            continue

        program_name = tokens[0]
        arguments = tokens[1:]

        ## Redirect stdout & stderr to a file ##
        redirect_operators = {
            ">": ("w", False),
            "1>": ("w", False),
            "2>": ("w", True),
            ">>": ("a", False),
            "1>>": ("a", False),
            "2>>": ("a", True)
        }

        symbol = next((op for op in tokens if op in redirect_operators), None)

        if symbol:
            redirect_symbol = tokens.index(symbol)
            context = tokens[:redirect_symbol]
            file = tokens[redirect_symbol + 1]

            mode, is_stderr = redirect_operators[symbol]
            redirect_or_append(mode, is_stderr, context, file)
            continue

        # if file is not builtin and is executable
        if program_name not in builtin_commands: 
            if check_executable(program_name):
                res = subprocess.run([program_name] + arguments, capture_output=True, text=True)
                print(res.stdout, end='')
                if res.stderr:
                    print(res.stderr, end='')
            else:
                print_command_not_found(user_input)
            continue

        match program_name:
            case "exit": exit(0)
            case "echo": 
                print(" ".join(arguments))
            case "type":
                file = " ".join(arguments)
                if file in builtin_commands:
                    print(f'{file} is a shell builtin')
                elif check_executable(file):
                    print(f'{file} is {check_executable(file)}')
                else:
                    print(f'{file}: not found')
            case "pwd": print(os.getcwd())
            case "cd":
                change_dir(" ".join(arguments) )
            case _ : print_command_not_found(user_input)

        
    pass 

def print_command_not_found(user_input):
    print(f'{user_input}: command not found')

def check_executable(file):
    is_executable = shutil.which(file)
    return is_executable

def change_dir(dir):
    if dir == '~':
        home_env = os.environ['HOME']
        os.chdir(home_env)
    elif os.path.isdir(dir):
        os.chdir(dir)
    else: 
        print(f'cd: {dir}: No such file or directory')
        
def redirect_or_append(mode, is_stderr, context, file):
    try:
        with open(file, mode) as f:
            subprocess.run(
                context,
                stdout=None if is_stderr else f,
                stderr=f if is_stderr else None,
                text=True
            )
    except FileNotFoundError:
        print(f"{file}: No such file or directory in append stdout", file=sys.stderr)
        

if __name__ == "__main__":
    main()
