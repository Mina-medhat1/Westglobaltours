import os
import re

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return

    original_html = html

    # 1. Remove Email from header
    html = re.sub(r'<li>\s*<a href=\"mailto:info@westtours\.com\".*?</a>\s*</li>', '', html, flags=re.DOTALL)

    # 2. Update Navbar Links to hash links since it's an SPA (well, actually, if they are on another page, they should go to /en/#about. But the root index redirects to /en/. So "/en/#about" is safer).
    html = re.sub(r'<li[^>]*>\s*<a href=\"/en/\">Home</a>\s*</li>', '<li class=\"active\"><a href=\"/en/#home\">Home</a></li>', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/en/about-us\">About Us</a>\s*</li>', '<li><a href=\"/en/#about\">About Us</a></li>', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/en/contact-us\">Contact Us</a>\s*</li>', '<li><a href=\"/en/#contact\">Contact Us</a></li>', html)

    # 3. Remove unwanted Navbar Links
    html = re.sub(r'<li[^>]*>\s*<a href=\"/en/plan-trip\">Plan your Trip</a>\s*</li>', '', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/en/incentives\">Incentives</a>\s*</li>', '', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/en/events\">Events</a>\s*</li>', '', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/en/become-partner\">Become a Partner</a>\s*</li>', '', html)

    # Spanish versions just in case
    html = re.sub(r'<li[^>]*>\s*<a href=\"/es/\">Inicio</a>\s*</li>', '<li class=\"active\"><a href=\"/es/#home\">Inicio</a></li>', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/es/quienes-somos\">Quiénes somos</a>\s*</li>', '<li><a href=\"/es/#about\">Quiénes somos</a></li>', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/es/contacte-con-nosotros\">Contacte con nosotros</a>\s*</li>', '<li><a href=\"/es/#contact\">Contacte con nosotros</a></li>', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/es/plan-trip\">.*?</a>\s*</li>', '', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/es/incentivos\">Incentivos</a>\s*</li>', '', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/es/eventos\">Eventos</a>\s*</li>', '', html)
    html = re.sub(r'<li[^>]*>\s*<a href=\"/es/become-partner\">.*?</a>\s*</li>', '', html)

    # Remove the Become a partner button
    html = re.sub(r'<a href=\"/en/become-partner\" class=\"nir-btn white\">Become a Partner</a>', '', html)
    html = re.sub(r'<a href=\"/es/become-partner\" class=\"nir-btn white\">.*?</a>', '', html)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Updated all HTML files.")
