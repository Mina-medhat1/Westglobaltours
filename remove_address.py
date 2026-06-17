import os
import re

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return

    original_html = html

    # Regex to match the address <li> tag in the footer
    # Using DOTALL to handle newlines
    pattern = r'<li[^>]*>\s*<i class="fa fa-map-marker"[^>]*></i>\s*<span[^>]*>2, Al Zohour Street, Old Hadaek Al Ahram, Giza, Egypt</span>\s*</li>'
    
    html = re.sub(pattern, '', html, flags=re.DOTALL)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

for root, dirs, files in os.walk(r'd:\vabi voding\new-redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Address removed from all footers.")
