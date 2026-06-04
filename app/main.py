import sys


def main():
    while 1: 
        sys.stdout.write("$ ")
        user_input = input()

        type_list = ["exit", "echo", "type"];

        if user_input == "exit":
            break
        elif user_input.startswith("echo"):
            print(user_input[5:])
        elif user_input.startswith("type"):
            if user_input[5:] in type_list:
                print(f'{user_input[5:]} is a shell builtin')
            else: 
                print(f'{user_input[5:]}: not found')
        else:
            print(f'{user_input}: command not found')

        # match user_input:
        #     case "exit":
        #         break
        #     case s if s.startswith("echo"):
        #         print(f'{user_input[5:]}')
        #     case _:
        #         print(f'{user_input}: command not found')

        
    pass

if __name__ == "__main__":
    main()
