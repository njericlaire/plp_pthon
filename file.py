try:
    # Ask the user for the filename to read
    input_filename = input("Enter the name of the file to read from: ")
    
    # Attempt to open the file for reading
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()
    
    # Generate the output filename
    output_filename = f"modified_{input_filename}"
    
    # Write the modified content to a new file
    with open(output_filename, 'w') as outfile:
        for line_number, line in enumerate(lines, start=1):
            outfile.write(f"{line_number}: {line}")
    
    print(f"Modified content has been written to {output_filename}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied for reading the file '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

