from retrieval.retrieval import load_index, retrieve_sections
from generation.generation import generate_response

def main(query):
    # Load indexes for each book
    book1_index = load_index("Dynamicsl_index.json")
    book2_index = load_index("Introduction-to-Data-Science-AAgah-20240620-1_index.json")
    book3_index = load_index("Research-Data-Management-in-the-Canadian-Context-1712778191_index.json")

    # Retrieve sections for each book
    book1_sections = retrieve_sections(query, book1_index["root"])
    book2_sections = retrieve_sections(query, book2_index["root"])
    book3_sections = retrieve_sections(query, book3_index["root"])

    # Combine sections from all books
    all_sections = book1_sections + book2_sections + book3_sections

    # Generate and print response
    response = generate_response(all_sections, query)
    print(response)

if __name__ == "__main__":
    user_query = "about"  # Example query
    main(user_query)
