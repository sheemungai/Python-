with open("files.txt", "w") as file:
    file.write("This is my new file!\n")
with open("files.txt", "r") as original_file:
    content = original_file.read()

modified_content = content.upper()
with open("modified_example.txt", "w") as new_file:
    new_file.write(modified_content)
print(" File has been read and modified successfully.")


def read_file_safely():
    filename = input(" Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print(" File content:\n")
            print(content)
    except FileNotFoundError:
        print(" Error: That file doesn't exist.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

read_file_safely()
