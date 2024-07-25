from transformers import pipeline

def setup_qa_pipeline():
    """
    Setup the question-answering pipeline with a specific model.
    
    Returns:
        pipeline: The Hugging Face question-answering pipeline.
    """
    return pipeline("question-answering", model="bert-large-cased-whole-word-masking-finetuned-squad")

def generate_response(sections, query):
    """
    Generate a response using the question-answering pipeline.
    
    Args:
        sections (list of dict): List of sections containing 'section' and 'text' keys.
        query (str): The question to be answered.
    
    Returns:
        str: The generated answer.
    """
    qa_pipeline = setup_qa_pipeline()
    
    # Combine relevant sections into a single context string
    context = " ".join(section['text'] for section in sections)
    
    # Ensure context is not empty and within acceptable length
    if not context:
        raise ValueError("The context provided is empty. Please check the retrieved sections.")
    
    # Truncate context to fit model input size if necessary
    # (Example for BERT: maximum 512 tokens, which is roughly 500-600 words)
    max_length = 512
    context_tokens = context.split()[:max_length]
    context = " ".join(context_tokens)
    
    # Pass the context and query to the pipeline
    result = qa_pipeline(question=query, context=context)
    
    return result['answer']
