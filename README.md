# Textbook Retrieval-Augmented Generation (RAG) System

## Overview

This project implements a sophisticated Retrieval-Augmented Generation (RAG) system that utilizes hierarchical tree-based indexing of textbooks for answering user queries. The system includes content extraction, hierarchical indexing, advanced retrieval techniques, and a user interface for interaction.

## Project Structure

1. **`retrieval/`** - Contains functions for loading hierarchical indexes and retrieving relevant sections.
2. **`generation/`** - Contains functions for generating responses using a Language Model.
3. **`chatbot/`** - Contains the Streamlit user interface for interacting with the system.
4. **`index/`** - Directory for hierarchical index files of the textbooks.

## Textbooks Used

1. **Textbook 1 Title** - [Link to Book](#)
2. **Textbook 2 Title** - [Link to Book](#)
3. **Textbook 3 Title** - [Link to Book](#)

*(Replace placeholders with actual textbook titles and links.)*

## Task Breakdown

### 1. Textbook Selection and Content Extraction

- **Objective**: Select three textbooks with more than 300 pages and extract all relevant content.
- **Files**:
  - `retrieval/retrieval.py`: Contains functions for loading hierarchical indexes and retrieving relevant sections.
  - **Note**: Ensure the content extraction process is thorough, capturing all necessary text from the textbooks.

### 2. Hierarchical Tree-based Indexing

- **Objective**: Create hierarchical tree-based indexes for each textbook, capturing chapters, sections, and subsections.
- **Files**:
  - `index/`: Contains JSON files representing hierarchical indexes of each textbook.
  - **Note**: Each index file should follow a structure with root, intermediate, and leaf nodes, including unique identifiers and parent-child relationships.

### 3. Retrieval Techniques

- **Objective**: Implement and experiment with various retrieval techniques such as BM25, BERT-based retrieval (DPR, SPIDER), and query expansion methods.
- **Files**:
  - `retrieval/retrieval.py`: Contains retrieval functions including query expansion and hybrid retrieval methods.
  - **Note**: Experiment with different strategies and evaluate their effectiveness in retrieving relevant content.

### 4. Multi-document/Topic/Section-based RAG

- **Objective**: Develop a RAG system that retrieves and ranks relevant sections from hierarchical indexes to generate coherent responses.
- **Files**:
  - `generation/generation.py`: Contains functions for setting up the question-answering pipeline and generating responses.
  - **Note**: Ensure that the system can traverse hierarchical indexes, retrieve relevant sections, and utilize them to generate accurate answers.

### 5. Question Answering

- **Objective**: Use an LLM to generate answers based on the retrieved content.
- **Files**:
  - `generation/generation.py`: Contains setup and usage of the question-answering pipeline.
  - **Note**: Make sure to use appropriate LLMs and configurations for generating accurate answers.

### 6. User Interface

- **Objective**: Create a user interface using Streamlit to allow users to input queries and display answers.
- **Files**:
  - `chatbot/main.py`: Streamlit application for interacting with the RAG system.
  - **Note**: Ensure the UI is functional, allowing users to input queries and see relevant answers along with textbook references.

## Setup Instructions

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
