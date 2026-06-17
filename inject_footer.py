import os
import re

new_footer = '''
<!-- Footer Starts -->
<footer class="footer-new" style="background-color: #f8f9fa; padding: 60px 0 20px 0; border-top: 1px solid #eaeaea;">
    <div class="container">
        <div class="row">
            <!-- Column 1: About -->
            <div class="col-lg-4 col-md-6 mb-4 pe-lg-5">
                <h5 style="color: #0f172a; font-weight: 600; margin-bottom: 20px;">About Tour</h5>
                <p style="color: #64748b; font-size: 14px; margin-bottom: 20px; line-height: 1.8;">
                    Welcome to West Tours, your gateway to unforgettable experiences. We specialize in curating the finest travel packages and excursions across the most magical destinations. Let us make your journey extraordinary!
                </p>
                <div class="social-icons d-flex mt-3">
                    <a href="#" style="background: #0f172a; color: #fff; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; margin-right: 10px; text-decoration: none;"><i class="fab fa-twitter"></i></a>
                    <a href="#" style="background: #0f172a; color: #fff; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; margin-right: 10px; text-decoration: none;"><i class="fab fa-instagram"></i></a>
                    <a href="#" style="background: #0f172a; color: #fff; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; margin-right: 10px; text-decoration: none;"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" style="background: #0f172a; color: #fff; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; text-decoration: none;"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </div>
            
            <!-- Column 2: Pages -->
            <div class="col-lg-2 col-md-6 mb-4">
                <h5 style="color: #0f172a; font-weight: 600; margin-bottom: 20px;">Pages</h5>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 15px;"><a href="/en/#home" style="color: #0f172a; font-size: 14px; text-decoration: none;">Home</a></li>
                    <li style="margin-bottom: 15px;"><a href="/en/destinations/egypt/" style="color: #0f172a; font-size: 14px; text-decoration: none;">Destinations</a></li>
                    <li style="margin-bottom: 15px;"><a href="/en/egypt/excursions/" style="color: #0f172a; font-size: 14px; text-decoration: none;">Excursions</a></li>
                </ul>
            </div>
            
            <!-- Column 3: Resources -->
            <div class="col-lg-2 col-md-6 mb-4">
                <h5 style="color: #0f172a; font-weight: 600; margin-bottom: 20px;">Resources</h5>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 15px;"><a href="/en/#about" style="color: #0f172a; font-size: 14px; text-decoration: none;">About Us</a></li>
                    <li style="margin-bottom: 15px;"><a href="/en/become-partner/" style="color: #0f172a; font-size: 14px; text-decoration: none;">Become Partner</a></li>
                    <li style="margin-bottom: 15px;"><a href="/en/#contact" style="color: #0f172a; font-size: 14px; text-decoration: none;">Contact Us</a></li>
                </ul>
            </div>
            
            <!-- Column 4: Contact -->
            <div class="col-lg-4 col-md-6 mb-4">
                <h5 style="color: #0f172a; font-weight: 600; margin-bottom: 20px;">Contact</h5>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 15px; color: #0f172a; font-size: 14px; display: flex; align-items: flex-start;">
                        <i class="fa fa-envelope" style="color: #64748b; margin-right: 15px; margin-top: 4px;"></i> 
                        <a href="mailto:info@excellenttours.com" style="color: #0f172a; text-decoration: none;">info@excellenttours.com</a>
                    </li>
                    <li style="margin-bottom: 15px; color: #0f172a; font-size: 14px; display: flex; align-items: flex-start;">
                        <i class="fa fa-phone" style="color: #64748b; margin-right: 15px; margin-top: 4px;"></i> 
                        <a href="tel:+201277273438" style="color: #0f172a; text-decoration: none;">+201277273438</a>
                    </li>
                    <li style="color: #0f172a; font-size: 14px; display: flex; align-items: flex-start;">
                        <i class="fa fa-map-marker" style="color: #64748b; margin-right: 15px; margin-top: 4px;"></i> 
                        <span style="line-height: 1.8;">2, Al Zohour Street, Old Hadaek Al Ahram, Giza, Egypt</span>
                    </li>
                </ul>
            </div>
        </div>
        
        <div class="row mt-4">
            <div class="col-12 border-top pt-4 text-center">
                <p style="color: #94a3b8; font-size: 13px; margin: 0;">© 2026 West Tours. All rights reserved.</p>
            </div>
        </div>
    </div>
</footer>
<!-- Footer Ends -->
'''

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return

    original_html = html

    # 1. Remove Top Bar (everything before Navbar)
    html = re.sub(r'<div class="header-content[^>]*>.*?</div>\s*<!-- Navigation Bar -->', '<!-- Navigation Bar -->', html, flags=re.DOTALL)

    # 2. Update Logo
    html = re.sub(r'src="/images/uploads/logowhite.png"', r'src="/images/uploads/west-tours-logo.png"', html)
    html = re.sub(r'src="/images/uploads/logo\.(png|jpg|webp)"', r'src="/images/uploads/west-tours-logo.png"', html)

    # 3. Replace Footer
    # Replace the old footer element entirely
    html = re.sub(r'<footer class="pt-20 pb-4".*?</footer>', new_footer, html, flags=re.DOTALL)
    
    # Remove the old footer-copyright div up to the back-to-top section
    html = re.sub(r'<div class="footer-copyright">.*?<!-- Back to top start -->', '<!-- Back to top start -->', html, flags=re.DOTALL)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

for root, dirs, files in os.walk(r'd:\vabi voding\new-redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Injected new footer, updated logo, and removed top bar.")
