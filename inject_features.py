import os
import re

preloader_html = '''
    <!-- Preloader Starts -->
    <div id="preloader">
        <div class="airplane-loader">
            <i class="fa fa-globe globe-icon"></i>
            <div class="plane-container">
                <i class="fa fa-plane plane-icon"></i>
            </div>
        </div>
    </div>
    <!-- Preloader Ends -->
'''

theme_script_tag = '<script src="/TITSolutions/ws/js/theme-toggle.js"></script>'
theme_toggle_btn = '''
                        <div class="theme-switch-wrapper me-3 d-flex align-items-center">
                            <a href="#" id="theme-toggle-btn" class="white" style="font-size: 20px;" title="Toggle Light/Dark Mode">
                                <i class="fa fa-moon-o"></i>
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

    # 1. Replace Preloader
    html = re.sub(r'<!-- Preloader -->\s*<div id=\"preloader\">\s*.*?</div>\s*<!-- Preloader Ends -->', preloader_html, html, flags=re.DOTALL)

    # 2. Inject Theme Toggle JS
    if 'theme-toggle.js' not in html:
        html = html.replace('</body>', theme_script_tag + '\n</body>')

    # 3. Inject Toggle Button in Navbar (before Become a partner button or Language Switcher)
    if 'theme-toggle-btn' not in html:
        html = html.replace('<!-- Language Switcher -->', theme_toggle_btn + '\n                        <!-- Language Switcher -->')

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Injected preloader and theme toggle into all HTML files.")
