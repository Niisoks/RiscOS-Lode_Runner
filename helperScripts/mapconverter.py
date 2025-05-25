"""
Level Converter Script
Converts JSON level data to individual level files for Lode Runner game.

Usage: python convert_levels.py input.json
"""

import json
import sys
import os

def convert_character(char):
    """Convert input character to game character based on mapping."""
    mapping = {
        '&': 'P',  
        '0': 'E',  
        '#': '#',  
        'X': 'X',  
        '@': 'S',  
        'H': 'H',  
        'S': 'W',  
        '-': '-',  
        '$': 'G',  
        ' ': ' '   
    }
    return mapping.get(char, char)

def convert_level(level_data):
    """Convert a single level's data using character mapping."""
    converted_lines = []
    for line in level_data:
        converted_line = ''.join(convert_character(char) for char in line)
        converted_lines.append(converted_line)
    return converted_lines

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_levels.py input.json")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    try:

        with open(input_file, 'r') as f:
            data = json.load(f)

        print(f"Found {len(data)} levels in {input_file}")

        for level_key, level_data in data.items():

            converted_level = convert_level(level_data)

            level_number = int(level_key) + 1
            output_filename = f"level{level_number}"

            with open(output_filename, 'w') as f:
                for line in converted_level:
                    f.write(line + '\n')

            print(f"Converted level {level_key} -> {output_filename}")
            print(f"  Dimensions: {len(converted_level)} rows x {len(converted_level[0]) if converted_level else 0} columns")

        print(f"\nConversion complete! Created {len(data)} level files.")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{input_file}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()