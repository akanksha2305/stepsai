def rank_sections(sections, query):
    """
    Rank sections based on relevance to the query.
    
    Args:
        sections (list of dict): List of sections with their content.
        query (str): User query.
    
    Returns:
        list of dict: Ranked sections.
    """
    # Simple ranking based on the presence of the query
    return sorted(sections, key=lambda x: x['text'].count(query), reverse=True)
