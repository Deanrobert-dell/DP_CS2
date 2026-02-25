# Append Module - Legacy file for compatibility
# Note: Append functionality is now handled in file_handler.py
# This file is kept for backward compatibility

def add_to_document(doc_path, content):
    """
    Legacy function - use file_handler.append_content instead.
    
    Args:
        doc_path (str): Path to document
        content (str): Content to append
        
    Returns:
        bool: True on success
    """
    try:
        from File import append_content
        append_content(doc_path, content)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False