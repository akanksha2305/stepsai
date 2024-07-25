def generate_response(sections):
    """
    Generate a response based on the retrieved sections.
    
    Args:
        sections (list): List of retrieved sections.
    
    Returns:
        str: The generated response.
    """
    if not sections:
        return "No relevant sections found."

    response = "Here are the relevant sections:\n"
    for section in sections:
        response += f"- {section}\n"
    
    return response
