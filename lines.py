import sys
import os

def main():
    # Ensure exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")

    # Get the file name from command-line arguments
    filename = sys.argv[1]

    # Check if the file has a .py extension
    if not filename.endswith(".py"):
        sys.exit("Error: File must have a .py extension")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit(f"Error: File '{filename}' does not exist")

    try:
        with open(filename, 'r') as file:
            lines_of_code = 0

            # Iterate over each line in the file
            for line in file:
                stripped_line = line.lstrip()  # Remove leading whitespace

                # Ignore blank lines and comments
                if stripped_line == "" or stripped_line.startswith("#"):
                    continue

                # If it's a valid line of code, increment the counter
                lines_of_code += 1

        # Output the total number of lines of code
        print(f"Lines of code: {lines_of_code}")

    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found")

if __name__ == "__main__":
    main()

