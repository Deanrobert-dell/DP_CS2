# File Handling Module
def read_file(file_path):
    """
    Read the file and return the content without metadata.
    
    Args:
        file_path (str): Path to the document file
        
    Returns:
        str: Clean content without word count and timestamp
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove word count and timestamp from the end
    content = remove_metadata(content)
    return content.strip()


def remove_metadata(content):
    """
    Remove word count and timestamp metadata from content.
    
    Args:
        content (str): Full file content
        
    Returns:
        str: Content without metadata
    """
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
    """
    Write content to file and add word count and timestamp at the bottom.
    
    Args:
        file_path (str): Path to the document file
        content (str): Document content
        word_count (int): Word count of the document
        timestamp (str): Formatted timestamp
    """
    # Remove old metadata first
    clean_content = remove_metadata(content)
    
    # Create new content with metadata
    new_content = clean_content + "\n\n"
    new_content += f"Word Count: {word_count}\n"
    new_content += f"Last Updated: {timestamp}\n"
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


def append_content(file_path, new_content):
    """
    Append new content to the file without updating metadata yet.
    
    Args:
        file_path (str): Path to the document file
        new_content (str): Content to append
    """
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as file:
        current_content = file.read()
    
    # Remove metadata
    clean_content = remove_metadata(current_content)
    
    # Append new content
    updated_content = clean_content + "\n" + new_content
    
    # Write back without metadata (user will update info to add metadata)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)