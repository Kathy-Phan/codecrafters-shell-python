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
            
        if '>' in tokens or '1>' in tokens:
            symbol = '>' if '>' in tokens else '1>'
            redirect_symbol = tokens.index(symbol)
            cmd = tokens[:redirect_symbol]
            result = subprocess.run(cmd, capture_output=True, text=True)
            redirect(result, tokens[redirect_symbol + 1])
            continue
       
        if program_name not in builtin_commands: 
            if shutil.which(program_name):
                res = subprocess.run([program_name] + arguments, capture_output=True, text=True)
                print(res.stdout, end='')
                if res.stderr:
                    print(res.stderr, end='')
            else:
                print_command_not_found(user_input)
            continue

        match program_name:
            case "exit": exit(0)
            case "echo": print(" ".join(arguments) )
            case "type":
                locate_executable_file(" ".join(arguments) )
            case "pwd": print(os.getcwd())
            case "cd":
                change_dir(" ".join(arguments) )
            case _ : print_command_not_found(user_input)

        
    pass 

def print_command_not_found(user_input):
    print(f'{user_input}: command not found')

def locate_executable_file(file):
    is_executable = shutil.which(file)
    if file in builtin_commands:
        print(f'{file} is a shell builtin')
    elif is_executable:
        print(f'{file} is {is_executable}')
    else:
        print(f'{file}: not found')

def change_dir(dir):
    if dir == '~':
        home_env = os.environ['HOME']
        os.chdir(home_env)
    elif os.path.isdir(dir):
        os.chdir(dir)
    else: 
        print(f'cd: {dir}: No such file or directory')

def redirect(res, file):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w") as f:
        f.write(res.stdout)
        
    if res.stderr:
        print(res.stderr, end='')

if __name__ == "__main__":
    main()
