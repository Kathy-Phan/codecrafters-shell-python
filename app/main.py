import sys, shutil

def main():
    while 1: 
        sys.stdout.write("$ ")
        user_input = input()
        cmd = user_input[5:]
        file_path = shutil.which(cmd)
        builtin_commands = ["exit", "echo", "type"];

        if user_input == "exit":
            break
        elif user_input.startswith("echo"):
            print(cmd)
        elif user_input.startswith("type"):
            if cmd in builtin_commands:
                print(f'{cmd} is a shell builtin')
            elif file_path:
                print(f'{cmd} is {file_path}')
            else: 
                print(f'{cmd}: not found')
        else: 
            print(f'{user_input}: command not found')
    pass

if __name__ == "__main__":
    main()
