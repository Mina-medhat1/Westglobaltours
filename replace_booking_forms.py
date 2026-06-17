import os
import re

whatsapp_widget = '''
<div class="form-content rounded overflow-hidden bg-title text-center" style="padding: 30px;">
    <h4 class="white text-center border-b pb-2 mb-4">Book Now</h4>
    <p class="white mb-4">For immediate booking and personalized assistance, please contact us directly via WhatsApp.</p>
    <a href="https://wa.me/20233776552" class="nir-btn w-100" style="display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 18px; padding: 15px;">
        <i class="fa fa-whatsapp" style="font-size: 24px;"></i> Chat on WhatsApp
    </a>
</div>
'''

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return

    original_html = html

    # Regex to match the entire form block that has the Book Now heading
    # We look for <form ... </form> that contains "Book Now"
    # Using re.sub with a function or just a pattern.
    # The form might span many lines, so we use DOTALL.
    # To avoid matching the newsletter form, we ensure it contains "txt_ProductName" or "ddl_AdultsNo" or "Book Now" inside a bg-title class.
    
    # Let's match the form specifically used for booking:
    # <form ... class="form-content ... bg-title" ... > ... </form>
    
    pattern = r'<form[^>]*class="[^"]*form-content[^"]*bg-title[^"]*"[^>]*>.*?</form>'
    
    html = re.sub(pattern, whatsapp_widget, html, flags=re.DOTALL)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            # just count how many we change
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if re.search(r'<form[^>]*class="[^"]*form-content[^"]*bg-title[^"]*"[^>]*>', content):
                        count += 1
            except:
                pass
            process_file(filepath)

print(f"Replaced booking forms in {count} HTML files.")
