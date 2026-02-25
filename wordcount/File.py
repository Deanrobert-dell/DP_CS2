# File Handling Modules
def read_file(file_path):
   #readsa nd returns data from file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove word count and timestamp from the end of the contents
    content = remove_metadata(content)
    return content.strip()


def remove_metadata(content):
    #removed count
    lines = content.split('\n')
    
    # Find and remove metadata lines
    while lines and lines[-1].startswith('Word Count:'):
        lines.pop()
    while lines and lines[-1].startswith('Last Updated:'):
        lines.pop()
    while lines and lines[-1].strip() == '':
        lines.pop()
    
    return '\n'.join(lines)


def write_file(file_path, content, word_count, timestamp):
    #write data to a file with count and a timestamp
    # Remove old data first
    clean_content = remove_metadata(content)
    
    # Create new content with data
    new_content = clean_content + "\n\n"
    new_content += f"Word Count: {word_count}\n"
    new_content += f"Last Updated: {timestamp}\n"
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


def append_content(file_path, new_content):
   #append new content to the file
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as file:
        current_content = file.read()
    
    # Remove metadata
    clean_content = remove_metadata(current_content)
    
    # Append new content
    updated_content = clean_content + "\n" + new_content
    
    # Write back without data e user will add
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)