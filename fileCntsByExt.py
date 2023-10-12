import os
import csv
from collections import defaultdict

# Function to categorize files by extension
def categorize_files(directory):
    file_count_by_extension = defaultdict(int)

    file_cnt = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:

            file_cnt += 1
            _, extension = os.path.splitext(filename)
            extension = extension.lstrip('.').lower()  # Normalize extension

            # Update the count for this extension
            file_count_by_extension[extension] += 1

    print(file_cnt)
    return file_count_by_extension

# Specify the root directory to start from
root_directory = "/Volumes/5TB ExFAT"

if os.path.exists(root_directory) and os.path.isdir(root_directory):
    file_count_by_extension = categorize_files(root_directory)

    # Sort the extensions by count in descending order
    sorted_extensions = sorted(file_count_by_extension.items(), key=lambda x: x[1], reverse=True)

    # Specify the CSV output file
    output_file = "/Users/alanjackson/Documents/Environments/5TB_ExFAT_file_counts.csv"

    # Write the results to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Extension", "Count"])  # Write header

        for extension, count in sorted_extensions:
            csv_writer.writerow([extension, count])

    print(f"Results saved to '{output_file}'")
else:
    print("Invalid directory path.")
