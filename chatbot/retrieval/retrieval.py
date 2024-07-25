import json

def load_index(file_path):
    """
    Load the hierarchical index from a JSON file.
    
    Args:
        file_path (str): Path to the JSON index file.
    
    Returns:
        dict: Hierarchical index loaded from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        index = json.load(file)
    return index

def retrieve_sections(query, index):
    """
    Retrieve sections from the hierarchical index that match the query.
    
    Args:
        query (str): The query string.
        index (dict): Hierarchical index.
    
    Returns:
        list of dict: List of sections that match the query.
    """
    matching_sections = []

    def search_sections(sections, query):
        for key, value in sections.items():
            if isinstance(value, str) and query.lower() in value.lower():
                matching_sections.append({'section': key, 'text': value})
            elif isinstance(value, dict):
                search_sections(value, query)

    search_sections(index, query)
    return matching_sections
