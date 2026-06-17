import os
import re

new_footer = '''
<!-- Footer Starts -->
<footer class="footer-dark" style="background-color: #0f172a; padding: 25px 0; border-top: 2px solid #1e293b; width: 100%;">
    <div class="container d-flex flex-column flex-md-row justify-content-between align-items-center">
        <div class="contact-info text-white mb-3 mb-md-0" style="font-size: 14px;">
            <p class="mb-1 text-white">Phone: <a href="tel:+201277273438" style="color: #cbd5e1; text-decoration: none;">+201277273438</a></p>
            <p class="mb-0 text-white">Email: <a href="mailto:Westglobaltours.info@gmail.com" style="color: #cbd5e1; text-decoration: none;">Westglobaltours.info@gmail.com</a></p>
        </div>
        <div class="social-icons mb-3 mb-md-0 d-flex gap-3">
            <a href="https://www.facebook.com/share/18Sz4nP34C/" class="text-white mx-2 fs-5"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="text-white mx-2 fs-5"><i class="fab fa-instagram"></i></a>
            <a href="#" class="text-white mx-2 fs-5"><i class="fab fa-twitter"></i></a>
            <a href="#" class="text-white mx-2 fs-5"><i class="fab fa-youtube"></i></a>
        </div>
        <div class="copyright-text text-white text-center text-md-end" style="font-size: 13px; color: #94a3b8 !important;">
            &copy; 2026 West Tours. All rights reserved.
        </div>
    </div>
</footer>
<!-- Footer Ends -->
'''

new_theme_toggle = '''
<div class="theme-switch-wrapper me-3 d-flex align-items-center">
    <label class="theme-switch" for="theme-toggle-btn" style="position: relative; display: inline-block; width: 50px; height: 26px; margin: 0;">
        <input type="checkbox" id="theme-toggle-btn" style="opacity: 0; width: 0; height: 0;" />
        <span class="slider-toggle round" style="position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #cbd5e1; transition: .4s; border-radius: 34px;">
            <i class="fas fa-sun" style="position: absolute; left: 6px; top: 6px; font-size: 14px; color: white; z-index: 1;"></i>
            <i class="fas fa-moon" style="position: absolute; right: 6px; top: 6px; font-size: 14px; color: white; z-index: 1;"></i>
        </span>
    </label>
</div>
'''

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return

    original_html = html

    # Replace footer
    html = re.sub(r'<footer class="footer-new".*?</footer>', new_footer, html, flags=re.DOTALL)
    
    # Replace theme toggle
    html = re.sub(r'<div class="theme-switch-wrapper[^>]*>.*?</div>\s*<!-- Language Switcher -->', new_theme_toggle + '\n                        <!-- Language Switcher -->', html, flags=re.DOTALL)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

for root, dirs, files in os.walk(r'd:\vabi voding\new-redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Updated footer and theme toggle globally.")
