# バージョン情報を削除するコード
import re
import os

def remove_version_info(input_file, output_file):
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
        return
    
    with open(input_file, 'r') as file:
        content = file.read()

    # Use regex to remove version information, handling versions like '==21.12b0'
    cleaned_content = re.sub(r"==[^\s]+", "", content)

    # Create output file and write cleaned content to it
    with open(output_file, 'w') as file:
        file.write(cleaned_content)

    print(f"Version info removed. Output saved to {output_file}")

# Usage
input_file = "requirements.txt"  # Replace with your input file path
output_file = "cleaned_requirements.txt"  # Replace with your output file path
remove_version_info(input_file, output_file)
