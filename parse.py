# Define a function to filter a log file and create a new file without specific lines.
def filter_log_file(input_file, output_file, filter_string):
    try:
        # Open the input log file for reading and the output file for writing.
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Iterate through each line in the input file.
            for line in infile:
                # Check if the filter string is NOT present in the line.
                if filter_string not in line:
                    # If the filter string is not found, write the line to the output file.
                    outfile.write(line)
        # Print a message indicating that the filtered log file has been saved.
        print(f"Filtered log file saved to {output_file}")
    except FileNotFoundError:
        # Handle the case where the input file is not found.
        print("File not found. Please provide a valid input file.")

if __name__ == "__main__":
    # Define the paths to the input and output files.
    input_file = "3success.log"  # Replace with your input log file
    output_file = "3filtered.log"  # Replace with the desired output file
    # Define the filter string you want to remove from the log file.
    filter_string = "SUCCESS  | src.auto_archiver.feeders.gsheet_feeder:__iter__:93 - Finished worksheet Sheet1"

    # Call the filter_log_file function with the specified parameters.
    filter_log_file(input_file, output_file, filter_string)
