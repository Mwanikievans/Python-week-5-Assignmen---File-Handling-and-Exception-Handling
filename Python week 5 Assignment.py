def read_and_write_file():
    # Ask the user for a filename
    filename = input("Enter the filename: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Modify the content (for example, convert to uppercase)
    modified_content = content.upper()

    # Create a new filename by appending "_modified" to the original filename
    new_filename = f"{filename}_modified.txt"

    try:
        # Attempt to write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
    except Exception as e:
        print(f"An error occurred while writing to the new file: {e}")
        return

    print(f"Modified content has been written to '{new_filename}'.")

if _name_ == "_main_":
    read_and_write_file()