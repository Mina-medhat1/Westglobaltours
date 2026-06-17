import os
import re

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        return

    original_html = html

    # 1. Update Title and Meta Tags
    html = re.sub(r'<title>(.*?)</title>', lambda m: f"<title>{m.group(1).replace('Excellent Tours', 'West Tours')}</title>", html)
    html = re.sub(r'<meta property="og:title" content="(.*?)"', lambda m: f'<meta property="og:title" content="{m.group(1).replace("Excellent Tours", "West Tours")}"', html)
    html = re.sub(r'<meta property="og:site_name" content="(.*?)"', lambda m: f'<meta property="og:site_name" content="{m.group(1).replace("Excellent Tours", "West Tours")}"', html)
    html = re.sub(r'<meta name="twitter:title" content="(.*?)"', lambda m: f'<meta name="twitter:title" content="{m.group(1).replace("Excellent Tours", "West Tours")}"', html)

    # 2. Update Favicon
    html = re.sub(r'<link rel="shortcut icon" href="/images/favicon.png">', '<link rel="shortcut icon" href="/images/uploads/logo1.png">', html)
    html = re.sub(r'<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.png">', '<link rel="shortcut icon" type="image/x-icon" href="/images/uploads/logo1.png">', html)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

for root, dirs, files in os.walk(r'd:\vabi voding\new-redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Updated site titles and favicons.")
