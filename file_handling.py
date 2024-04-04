def write_to_file():
    try:
        # Open the file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("Line 1: Hi My name is Violeth a PLP student.\n")
            file.write("Line 2: 2024\n")
            file.write("Line 3: I am in a Project Management Department: 3.14, 42\n")
        print("File 'my_file.txt' created and written successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")
    finally:
        print("Writing process completed.")


def read_from_file():
    try:
        # Open the file in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to access 'my_file.txt'.")
    finally:
        print("Reading process completed.")


def append_to_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the file
            file.write("Line 4: Appended line 1.\n")
            file.write("Line 5: Appended line 2.\n")
            file.write("Line 6: Appended line 3.\n")
        print("File 'my_file.txt' appended successfully.")
    except IOError as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Appending process completed.")


# Perform file creation and writing
write_to_file()

# Perform file reading and display
read_from_file()

# Perform file appending
append_to_file()
