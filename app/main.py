import sys


def main():
    while 1: 
        sys.stdout.write("$ ")
        user_input = input()
        if user_input == "exit":
            break
        elif "echo" in user_input:
            print(user_input[5:])
        else:
            print(f"{user_input}: command not found")

        # match user_input:
        #     case "exit":
        #         break
        #     case "echo":
        #         print(f"{user_input}")
        #     case _:
        #         print(f"{user_input}: command not found")

        
    pass

if __name__ == "__main__":
    main()
