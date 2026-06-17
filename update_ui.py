import os
import re

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return

    original_html = html

    # Update Footer Email
    html = html.replace('info@excellenttours.com', 'Westglobaltours.info@gmail.com')
    
    # Update Facebook link
    # Find the facebook icon link and replace its href
    html = re.sub(
        r'<a href="[^"]*"([^>]*><i class="fab fa-facebook-f">)',
        r'<a href="https://www.facebook.com/share/18Sz4nP34C/"\1',
        html
    )

    # Remove "Become Partner" from Resources
    html = re.sub(r'<li[^>]*><a href="/en/become-partner/"[^>]*>Become Partner</a></li>', '', html)

    # Fix Logo size by adding class or inline style
    # Look for the logo img tag and add inline style if not present
    html = re.sub(r'(<img src="/images/uploads/west-tours-logo\.png"[^>]*)>', r'\1 style="max-height: 70px; width: auto;" >', html)
    # To avoid duplicate styles if run multiple times, just clean up first
    html = re.sub(r'style="max-height: 70px; width: auto;"\s*style="max-height: 70px; width: auto;"', 'style="max-height: 70px; width: auto;"', html)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

for root, dirs, files in os.walk(r'd:\vabi voding\new-redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Updated HTML files for logo size, footer info, and links.")
