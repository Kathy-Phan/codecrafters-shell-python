import sys, shutil, subprocess

def main():
    builtin_commands = ["exit", "echo", "type"];

    while 1: 
        sys.stdout.write("$ ")

        user_input = input()
        cmd = user_input[5:]
        file_path = shutil.which(cmd)
        
        program_name = user_input.split()[0]
        arguments = user_input.split()[1:]
        
        if user_input == "exit":
            break
        elif user_input.startswith("echo"):
            print(cmd)
        elif user_input.startswith("type"):
            # if command is built-in
            if cmd in builtin_commands:
                print(f'{cmd} is a shell builtin')
            elif file_path:
                print(f'{cmd} is {file_path}')
            else: 
                print(f'{cmd}: not found')
        elif shutil.which(program_name):
            res = subprocess.run([program_name] + arguments, capture_output=True, text=True)
            print(res.stdout, end='')
        else: 
            print(f'{user_input}: command not found')
    pass

if __name__ == "__main__":
    main()
