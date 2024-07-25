# Textbook Retrieval-Augmented Generation (RAG) System

## Overview

This project implements a sophisticated Retrieval-Augmented Generation (RAG) system that utilizes hierarchical tree-based indexing of textbooks for answering user queries. The system includes content extraction, hierarchical indexing, advanced retrieval techniques, and a user interface for interaction.


## Textbooks Used

1. **Introduction to Data Science Using Python** - [Link to Book](https://open.umn.edu/opentextbooks/textbooks/introduction-to-data-science-using-python)
2. **Dynamics of the Standard Model - [Link to Book](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FF8A95F0F22A67FABA729DBB39BA2816/9781009291002AR.pdf/Dynamics_of_the_Standard_Model.pdf?event-type=FTLA)
3. **Research Data Management in the Canadian Context** - [Link to Book](https://ecampusontario.pressbooks.pub/canadardm/)


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
   git clone https://github.com/akanksha2305/stepsai.git
   cd stepsai

2. **Create a Virtual Environment**

   ```sh
   python -m venv venv
venv\Scripts\activate

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt

##Running the System
1. **Start the Streamlit Interface**

```sh
  Copy code
  streamlit run chatbot/main.py
Open your browser and navigate to http://localhost:8501 to interact with the chatbot.


