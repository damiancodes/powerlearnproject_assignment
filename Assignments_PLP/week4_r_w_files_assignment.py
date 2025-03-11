def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()  # Convert text to uppercase
        new_filename = "modified_" + filename

        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File modified and saved as {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Error: The file could not be read or written.")


read_and_modify_file()
