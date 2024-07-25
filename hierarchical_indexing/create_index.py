import json
import re

def parse_text_structure(text):
    # Adjust regex patterns for varying formats
    chapter_patterns = [r'^Chapter\s+\d+\s*[:\-]?\s*', r'^\d+\.\s*.*']  # Example patterns for different formats
    section_patterns = [r'^Section\s+\d+(\.\d+)?\s*[:\-]?\s*', r'^\d+\.\d+(\.\d+)?\s*[:\-]?\s*']  # Example patterns for different formats
    
    structure = {}
    current_chapter = None
    current_section = None
    current_text = ""
    
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        print(f"Processing line: {line}")  # Debug print

        matched = False
        # Check for chapter
        for pattern in chapter_patterns:
            if re.match(pattern, line):
                if current_chapter:
                    if current_section:
                        structure[current_chapter][current_section] = current_text
                        current_section = None
                    else:
                        structure[current_chapter] = current_text
                current_chapter = line
                structure[current_chapter] = {}
                current_text = ""
                matched = True
                break
        
        if matched:
            continue

        # Check for section
        for pattern in section_patterns:
            if re.match(pattern, line):
                if current_section:
                    structure[current_chapter][current_section] = current_text
                current_section = line
                current_text = ""
                matched = True
                break
        
        if matched:
            continue

        # Accumulate text
        if current_section:
            current_text += line + '\n'
        elif current_chapter:
            if structure[current_chapter] == {}:
                structure[current_chapter] = line + '\n'
            else:
                structure[current_chapter] += line + '\n'
    
    # Add remaining content
    if current_section:
        structure[current_chapter][current_section] = current_text
    elif current_chapter:
        if structure[current_chapter] == {}:
            structure[current_chapter] = current_text
        else:
            structure[current_chapter] += current_text
    
    return {"root": structure}

def create_hierarchical_index(text):
    index = parse_text_structure(text)
    return index

def save_index_to_file(index, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(index, file, indent=4)

if __name__ == "__main__":
    text_paths = [
        'Introduction-to-Data-Science-AAgah-20240620-1.txt',
        'Dynamicsl.txt',
        'Research-Data-Management-in-the-Canadian-Context-1712778191.txt'
    ]
    
    for text_path in text_paths:
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        index = create_hierarchical_index(text)
        output_path = text_path.replace('.txt', '_index.json')
        save_index_to_file(index, output_path)
        print(f"Hierarchical index saved to {output_path}")
