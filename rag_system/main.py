from retrieval.retrieval import load_index, retrieve_sections
from generation.generation import generate_response

def main(query):
    # Define paths to your index files
    index_paths = {
        "Introduction to Data Science Using Python": "Introduction-to-Data-Science-AAgah-20240620-1_index.json",
        "Dynamics of the Standard Model": "Dynamicsl_index.json",
        "Research Data Management in the Canadian Context": "Research-Data-Management-in-the-Canadian-Context-1712778191_index.json"
    }

    # Load indexes for each book
    indexes = {name: load_index(path) for name, path in index_paths.items()}

    # Retrieve sections for each book
    all_sections = []
    for name, index in indexes.items():
        print(f"Retrieving sections from {name}...")
        sections = retrieve_sections(query, index["root"])
        all_sections.extend(sections)

    # Generate and print response
    response = generate_response(all_sections)
    print("Generated Response:")
    print(response)

if __name__ == "__main__":
    user_query = "Variables"  # Example query
    main(user_query)
