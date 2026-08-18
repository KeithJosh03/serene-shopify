import os
import json
import re

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace references to settings.color_palette with empty string
    content = content.replace('"{{ settings.color_palette.background }}"', '""')
    content = content.replace('"{{ settings.color_palette.foreground }}"', '""')
    content = content.replace('"{{ settings.color_palette.color1 }}"', '""')
    content = content.replace('"{{ settings.color_palette.color2 }}"', '""')
    
    # Update type: "section" to "custom-section"
    # But only if it's a section type in JSON
    # It's safer to just replace '"type": "section"' with '"type": "custom-section"'
    content = content.replace('"type": "section"', '"type": "custom-section"')
    
    with open(filepath, 'w') as f:
        f.write(content)

def process_directory(directory):
    if not os.path.exists(directory): return
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') or file.endswith('.liquid'):
                replace_in_file(os.path.join(root, file))

process_directory('templates')
process_directory('sections')
process_directory('blocks')

# Fix settings_schema.json
schema_path = 'config/settings_schema.json'
with open(schema_path, 'r') as f:
    schema = json.loads(f.read())

# Find and remove color_palette setting
for category in schema:
    if 'settings' in category:
        category['settings'] = [s for s in category['settings'] if s.get('type') != 'color_palette']

with open(schema_path, 'w') as f:
    json.dump(schema, f, indent=2)

