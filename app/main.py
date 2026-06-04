import sys


def main():
    while 1: 
        sys.stdout.write("$ ")
        cmd = input()

        builtin_commands = ["exit", "echo", "type"];

        if cmd == "exit":
            break
        elif cmd.startswith("echo"):
            print(cmd[5:])
        elif cmd.startswith("type"):
            if cmd[5:] in builtin_commands:
                print(f'{cmd[5:]} is a shell builtin')
            else: 
                print(f'{cmd[5:]}: not found')
        else:
            print(f'{cmd}: command not found')

        # match cmd:
        #     case "exit":
        #         break
        #     case s if s.startswith("echo"):
        #         print(f'{cmd[5:]}')
        #     case _:
        #         print(f'{cmd}: cmd not found')

        
    pass

if __name__ == "__main__":
    main()
