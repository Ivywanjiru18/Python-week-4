def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.readlines()
        
        # Modify the content (example: converting to uppercase)
        modified_content = [line.upper() for line in content]
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Prompt user for filenames
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

# Call the function with user-provided filenames
read_and_modify_file(input_file, output_file)
