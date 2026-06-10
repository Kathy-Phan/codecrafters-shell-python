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

        match program_name:
            case "exit": exit(0)
            case "echo": 
                print(shlex.join(arguments).replace("'", ""))
            case "type":
                locate_executable_file(" ".join(arguments))
            case "pwd": print(os.getcwd())
            case "cd":
                change_dir(" ".join(arguments))
            case _ if shutil.which(program_name): 
                res = subprocess.run([program_name] + arguments, capture_output=True, text=True)
                print(res.stdout, end='')
            case _ : print(f'{user_input}: command not found')
    pass 

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


if __name__ == "__main__":
    main()
