import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while 1: 
        sys.stdout.write("$ ")
        user_input = input()
        print(f"{user_input}: command not found")
    pass


if __name__ == "__main__":
    main()
