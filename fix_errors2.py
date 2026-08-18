import os

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace references to settings.color_palette with empty string or standard color string if needed.
    # In settings_schema.json, empty string is fine for a color default if it's optional, 
    # but maybe we should use a valid hex like "#ffffff" and "#000000" to avoid validation errors for color settings.
    content = content.replace('"{{ settings.color_palette.background }}"', '"#ffffff"')
    content = content.replace('"{{ settings.color_palette.foreground }}"', '"#000000"')
    content = content.replace('"{{ settings.color_palette.color1 }}"', '"#ffffff"')
    content = content.replace('"{{ settings.color_palette.color2 }}"', '"#000000"')
    
    with open(filepath, 'w') as f:
        f.write(content)

def process_directory(directory):
    if not os.path.exists(directory): return
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') or file.endswith('.liquid'):
                replace_in_file(os.path.join(root, file))

process_directory('config')
process_directory('snippets')

