import sys, shutil, subprocess, os

def main():
    builtin_commands = ["exit", "echo", "type", "pwd", "cd"];

    while 1: 
        sys.stdout.write("$ ")

        user_input = input()
        cmd = user_input[5:]
        

        program_name = user_input.split()[0]
        
        if user_input == "exit":
            break
        elif user_input.startswith("echo"):
            print(cmd)
        elif user_input.startswith("type"):
            file_path = shutil.which(cmd)
            # if command is built-in
            if cmd in builtin_commands:
                print(f'{cmd} is a shell builtin')
            elif file_path:
                print(f'{cmd} is {file_path}')
            else: 
                print(f'{cmd}: not found')
        elif user_input.startswith("pwd"):
            print(os.getcwd())
        elif user_input.startswith("cd"):
            PATH = user_input.split()[1]
            if os.path.isdir(PATH):
                os.chdir(PATH)
            else: 
                print(f'cd: {PATH}: No such file or directory')
        elif shutil.which(program_name):
            arguments = user_input.split()[1:]
            res = subprocess.run([program_name] + arguments, capture_output=True, text=True)
            print(res.stdout, end='')
        else: 
            print(f'{user_input}: command not found')
    pass

if __name__ == "__main__":
    main()
