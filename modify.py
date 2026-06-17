import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Email from header
html = re.sub(r'<li>\s*<a href=\"mailto:info@excellenttours\.com\".*?</a>\s*</li>', '', html, flags=re.DOTALL)

# 2. Update Navbar Links
html = re.sub(r'<li[^>]*>\s*<a href=\"/en/\">Home</a>\s*</li>', '<li class=\"active\"><a href=\"#home\">Home</a></li>', html)
html = re.sub(r'<li[^>]*>\s*<a href=\"/en/about-us\">About Us</a>\s*</li>', '<li><a href=\"#about\">About Us</a></li>', html)
html = re.sub(r'<li[^>]*>\s*<a href=\"/en/contact-us\">Contact Us</a>\s*</li>', '<li><a href=\"#contact\">Contact Us</a></li>', html)

# 3. Remove unwanted Navbar Links
html = re.sub(r'<li[^>]*>\s*<a href=\"/en/plan-trip\">Plan your Trip</a>\s*</li>', '', html)
html = re.sub(r'<li[^>]*>\s*<a href=\"/en/incentives\">Incentives</a>\s*</li>', '', html)
html = re.sub(r'<li[^>]*>\s*<a href=\"/en/events\">Events</a>\s*</li>', '', html)
html = re.sub(r'<li[^>]*>\s*<a href=\"/en/become-partner\">Become a Partner</a>\s*</li>', '', html)

# Remove the Become a partner button
html = re.sub(r'<a href=\"/en/become-partner\" class=\"nir-btn white\">Become a Partner</a>', '', html)

# 4. Inject About Us and Contact Us content
about_html = '''
<!-- about-us starts -->
<section id="about" class="about-us pt-6" style="padding-top: 100px;">
    <div class="container">
        <div class="about-image-box">
            <div class="row d-flex align-items-center justify-content-between">
                <div class="col-lg-6 ps-4">
                    <div class="about-content text-lg-start">
                        <h4 class="theme d-inline-block mb-0">Excellent Tours</h4>
                        <h2 class="border-b mb-2 pb-1">Welcome to Excellence</h2>
                        <p class="mb-1 pb-2" style="text-align:justify;">
                            The pages that follow are the result of a constant commitment—day after day—to continuous improvement, a clear vision, and comprehensive services. 
                            They are built upon a solid foundation: a highly qualified and motivated team of professionals, ready to respond wherever, whenever, and however required. 
                            This is the only path that truly satisfies both you and us: excellence.
                        </p>
                        <p class="mb-1 pb-2" style="text-align:justify;">
                            They are also the result of a shared passion—the connection between the journey already traveled, which we do not look back on but never forget, and the path that still lies ahead. 
                            Above all, they are an expression of gratitude and recognition to all those who, through their personal and professional contributions, have made it possible for us to be where we are today.
                        </p>
                    </div>
                </div>
                <div class="col-lg-6 mb-4 pe-4">
                    <div class="about-image" style="animation: none; background: transparent">
                        <img src="/images/uploads/excellent-tours-AboutUs-64ce6.png" alt="" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- about-us ends -->
'''

contact_html = '''
<!-- contact starts -->
<section id="contact" class="contact-us pt-6" style="padding-top: 100px;">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title text-center mb-5 pb-2 w-50 mx-auto">
                    <h2 class="m-0">Get In <span>Touch</span></h2>
                    <p class="mb-0">We are ready to respond wherever, whenever, and however required.</p>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-4 mb-4">
                <div class="contact-info bg-white p-4 box-shadow rounded">
                    <h3 class="mb-3">Reach Us</h3>
                    <p><i class="fa fa-phone theme me-2"></i> +2 02 33776552</p>
                    <p><i class="fa fa-envelope theme me-2"></i> info@excellenttours.com</p>
                    <a href="https://wa.me/20233776552" class="nir-btn mt-3" style="width: 100%; text-align: center;">Chat on WhatsApp</a>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- contact ends -->
'''

# We need to insert this before the footer
if '<!-- footer starts -->' in html:
    html = html.replace('<!-- footer starts -->', about_html + '\n' + contact_html + '\n<!-- footer starts -->')
else:
    html = html.replace('</footer>', about_html + '\n' + contact_html + '\n</footer>')

# Change CTA buttons to WhatsApp
html = re.sub(r'<a href=\"/en/destinations/egypt/\" class=\"nir-btn\">.*?Start Your Journey.*?</a>', '<a href=\"https://wa.me/20233776552\" class=\"nir-btn\"><i class=\"fa fa-whatsapp\"></i> Book via WhatsApp</a>', html, flags=re.DOTALL)
html = re.sub(r'<a href=\"/en/destinations/dubai/\" class=\"nir-btn\">.*?Start Your Journey.*?</a>', '<a href=\"https://wa.me/20233776552\" class=\"nir-btn\"><i class=\"fa fa-whatsapp\"></i> Book via WhatsApp</a>', html, flags=re.DOTALL)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
