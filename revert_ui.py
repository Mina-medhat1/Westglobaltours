import os
import re

old_egypt_hero = '''
                            <div class="swiper-content">
                                <div class="entry-meta mb-2">
                                    <h5 class="entry-category mb-0 white">Explore Egypt</h5>
                                </div>
                                <h1 class="mb-2">
                                    <a href="/en/destinations/egypt/" class="white">
                                        Make Your Trip to Egypt Unforgettable
                                    </a>
                                </h1>
                                <p class="white mb-4">
                                    Experience the Magic of the Pharaohs. Embark on a luxurious journey through ancient history, golden deserts, and the breathtaking Nile.
                                </p>
                                <a href="https://wa.me/201277273438" class="nir-btn"><i class="fab fa-whatsapp"></i> Book via WhatsApp</a>
                            </div>
'''

old_dubai_hero = '''
                            <div class="swiper-content">
                                <div class="entry-meta mb-2">
                                    <h5 class="entry-category mb-0 white">Explore Dubai</h5>
                                </div>
                                <h1 class="mb-2">
                                    <a href="/en/destinations/dubai/" class="white">
                                        Make Your Trip to Dubai Unforgettable
                                    </a>
                                </h1>
                                <p class="white mb-4">
                                    Step Into the Future of Luxury. Discover a world where gravity-defying architecture meets pristine golden sands and unmatched exclusivity.
                                </p>
                                <a href="https://wa.me/201277273438" class="nir-btn"><i class="fab fa-whatsapp"></i> Book via WhatsApp</a>
                            </div>
'''

old_sections = '''
<section class="about-us pt-10" style="background-image: url(/images/uploads/shape4.png); background-position: center">
    <div class="container">
        <!-- why us starts -->
        <div class="row align-items-center">
            <div class="col-lg-6 col-md-12">
                <div class="about_us__ot position-relative mb-lg-0 mb-4">

                    <span class="experience-badge">25 Years of Experience</span>
                    <img src="/images/uploads/excellent-tours-Home-76de9.webp" alt="" class="img-fluid rounded mt-3">
                    <div class="video-thumbnail mt-3" data-bs-toggle="modal" data-bs-target="#videoModal">
                        <img src="/images/uploads/excellent-tours-Incentives-25143.webp" alt="">

                    </div>
                    <img src="/images/uploads/009-airplane.png" class="icon__png" alt="">
                    <div class="dot-pattern"></div>
                </div>
            </div>
            <div class="col-lg-6 col-md-12">
                <div class="d-flex flex-column">

                    <h4 class="theme mb-0">About Us</h4>
                    <h2 class="fw-bold">Exploring New Adventures and Creating Exceptional Travel Journeys</h2>

                    <div class="text-muted">

<p style='text-align:justify;'    >For over 25 years, Excellent Tours has been dedicated to delivering inspiring travel experiences across the globe. We combine deep industry expertise with a passion for discovery, offering personalized journeys that connect travelers with the culture, beauty, and spirit of every destination.</p>

<p style='text-align:justify;'    >Our commitment to excellence drives everything we do—from crafting seamless itineraries to providing outstanding support for our partners and clients. Whether you're seeking unforgettable adventures or reliable travel solutions, we ensure every journey is designed with care, precision, and a touch of inspiration.</p>
  
                    </div>

                   

                    <div class="mt-4">
                        <a href="/en/about-us" class="nir-btn">Discover Us</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- why us ends -->
    </div>
    <div class="white-overlay"></div>
</section>



<!-- counter -->


<section class="featured-counter bg-theme pb-6 pt-10">
    <div class="container">


        <div class="row align-items-center">
            <div class="col-lg-7">
                <div class="section-title mb-5">
                    <h2 class="white">Trusted by Over 150 Partners and Travel Professionals Worldwide</h2>
                    <p class="mb-0 white">We empower travel agencies and corporate partners with scalable solutions, seamless operations, and proven expertise across global destinations.</p>
                </div>
            </div>
            <div class="col-lg-5">
                <div class="counter text-center d-inline-block w-100 mt-0">
                    <div class="row">
                        <div class="col-lg-6 col-md-6 mb-4">
                            <div class="counter-item p-3 py-4 rounded bg-white">
                                <h3 class="value mb-0 theme fs-1">50000</h3>
                                <p class="m-0">Hotel Contracts &amp; Rate Agreements</p>
                            </div>
                        </div>

                        <div class="col-lg-6 col-md-6 mb-4">
                            <div class="counter-item p-3 py-4 rounded bg-white">
                                <h3 class="value mb-0 theme fs-1">150</h3>
                                <p class="m-0">Partner Clients Served Globally</p>
                            </div>
                        </div>

                        <div class="col-lg-6 col-md-6 mb-4">
                            <div class="counter-item p-3 py-4 rounded bg-white">
                                <h3 class="value mb-0 theme fs-1">12000</h3>
                                <p class="m-0">Successful Group Operations</p>
                            </div>
                        </div>

                        <div class="col-lg-6 col-md-6 mb-4">
                            <div class="counter-item p-3 py-4 rounded bg-white">
                                <h3 class="value mb-0 theme fs-1">8500</h3>
                                <p class="m-0">Corporate &amp; MICE Travel Programs</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>



<!-- top destinations -->
<section class="trending pb-5 pt-10">
    <div class="container">

        <div class="section-title mb-6 w-50 mx-auto text-center">
            <h4 class="mb-1 theme">Featured Destinations</h4>
            <h2 class="mb-1">Explore the World’s Most Inspiring Destinations</h2>
            <p>Discover unforgettable places and unique experiences curated to bring out the best of every destination.</p>
        </div>
        <div class="row align-items-center">
                <div class="col-lg-6 mb-4">
                    <div class="trend-item1">
                        <a href="/en/destinations/egypt/">
                            <div class="trend-image position-relative rounded">
                                <img src="/images/uploads/excellent-tours-Home-9bc84.webp" alt="Egypt">
                                <div class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index">
                                    <div class="trend-content-title">

                                        <h3 class="mb-0 white">Egypt</h3>
                                    </div>
                                    <span class="white bg-theme p-1 px-2 rounded">54 Tours</span>
                                </div>
                                <div class="color-overlay"></div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-lg-6 mb-4">
                    <div class="trend-item1">
                        <a href="/en/destinations/dubai/">
                            <div class="trend-image position-relative rounded">
                                <img src="/images/uploads/excellent-tours-Home-6e439.webp" alt="Dubai">
                                <div class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index">
                                    <div class="trend-content-title">

                                        <h3 class="mb-0 white">Dubai</h3>
                                    </div>
                                    <span class="white bg-theme p-1 px-2 rounded">42 Tours</span>
                                </div>
                                <div class="color-overlay"></div>
                            </div>
                        </a>
                    </div>
                </div>


        </div>
    </div>
</section>

<!-- about-us starts -->
'''

old_toggle = '''<a href="#" id="theme-toggle-btn" class="white" style="font-size: 20px;" title="Toggle Light/Dark Mode">
                                <i class="fas fa-moon"></i>
                            </a>'''

# Process index.html first
index_path = r'd:\vabi voding\new-redesign\index.html'
try:
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Revert Hero
    html = re.sub(r'<div class="swiper-content text-start".*?EXPLORE<br>THE WORLD.*?</a>\s*</div>', old_egypt_hero, html, count=1, flags=re.DOTALL)
    html = re.sub(r'<div class="swiper-content text-start".*?EXPLORE<br>THE WORLD.*?</a>\s*</div>', old_dubai_hero, html, count=1, flags=re.DOTALL)

    # Revert the middle sections
    html = re.sub(r'<!-- Stats Section -->\s*<section class="stats-section.*?<!-- Stats Section Ends -->', old_sections, html, flags=re.DOTALL)
    
    # Remove the Destinations auto-slider
    html = re.sub(r'<!-- Featured Destinations Slider -->.*?<!-- Featured Destinations Ends -->\s*<!-- about-us starts -->', '<!-- about-us starts -->', html, flags=re.DOTALL)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Reverted index.html")
except Exception as e:
    print(f"Error reverting index.html: {e}")

# Process all files for the toggle switch revert
def revert_toggle(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        original_html = html
        
        # Replace the switch back to the icon
        html = re.sub(r'<label class="theme-switch".*?</label>', old_toggle, html, flags=re.DOTALL)
        
        if html != original_html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
    except:
        pass

for root, dirs, files in os.walk(r'd:\vabi voding\new-redesign'):
    for file in files:
        if file.endswith('.html'):
            revert_toggle(os.path.join(root, file))

print("Reverted toggle globally.")
