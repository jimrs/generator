from src.generate import generate, generate_a_file, generate_with_file

print("Available commands: 'g' for generate, 'gg' for generate in a file, 'o' to generate an output file, 'h' for help, 'q' for quit.\n")

while True:
    cmd = input(">")

    if cmd == "g":
        print(generate(), end='')

    elif cmd == "gg":
        filename = input("Type in the filename:\n")
        n_of_attacks = input("Type in the number of attacks to generate:\n")
        generate_with_file(filename, n_of_attacks)
        print("Done.")

    elif cmd == "h":
        print("""The 'g' command generates 1 sample attack.
The 'gg' command will add a number of attacks to a specified file.
The 'o' command will create a new file filled with a specified number of attacks. Useful for testing purposes.
The 'h' command will print this.
The 'q' command will quit the program.""")

    elif cmd == "i":
        print("input")

    elif cmd == "o":
        filename = input("Type in the filename:\n")
        n_of_lines = input("Type in the number of lines to generate:\n")
        generate_a_file(filename, n_of_lines)
        print("Done.")

    elif cmd == "q":
        print("quit")
        break

    else:
        print("Wrong command. Type 'h' for help.")