import os

def append_all_files_recursively(directory, output_file='combined_files.txt'):
    result = []

    # Walk through all directories recursively
    for root, dirs, files in os.walk(directory):
        for filename in sorted(files):
            # Skip the output file itself to avoid recursion
            if filename == output_file or filename == "a.py":
                continue

            filepath = os.path.join(root, filename)

            # Get relative path for cleaner display
            relative_path = os.path.relpath(filepath, directory)

            try:
                # Try to read as text file
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
            except (UnicodeDecodeError, PermissionError):
                # Handle binary files or permission issues
                try:
                    with open(filepath, 'rb') as f:
                        content = f"[Binary file - {len(f.read())} bytes]"
                except Exception as e:
                    content = f"[Error reading file: {e}]"
            except Exception as e:
                content = f"[Error reading file: {e}]"
            result.append("------------------------------------------------------------\n")
            result.append(relative_path)
            result.append("\n")
            result.append(content)
            result.append("------------------------------------------------------------\n\n\n")


    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))

    print(f"Output written to: {output_file}")
    print(f"Total files processed: {len(result) // 2}")

# Usage
directory_path = '.'
append_all_files_recursively(directory_path, 'all_extension_files.txt')
