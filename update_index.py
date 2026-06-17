import os
import re

stats_html = '''
<!-- Stats Section -->
<section class="stats-section" style="margin-top: -60px; position: relative; z-index: 10;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-3 col-md-6 mb-4">
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); padding: 25px 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: center; gap: 15px;">
                    <div class="icon-wrapper" style="background: #e0f2f1; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-globe-americas" style="color: #208b8b; font-size: 24px;"></i>
                    </div>
                    <div>
                        <h3 style="margin: 0; font-size: 24px; font-weight: 800; color: #0f172a;">500+</h3>
                        <p style="margin: 0; font-size: 14px; color: #64748b; font-weight: 500;">Destinations</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 mb-4">
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); padding: 25px 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: center; gap: 15px;">
                    <div class="icon-wrapper" style="background: #e0f2f1; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-user-friends" style="color: #208b8b; font-size: 24px;"></i>
                    </div>
                    <div>
                        <h3 style="margin: 0; font-size: 24px; font-weight: 800; color: #0f172a;">10k+</h3>
                        <p style="margin: 0; font-size: 14px; color: #64748b; font-weight: 500;">Happy Travelers</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 mb-4">
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); padding: 25px 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: center; gap: 15px;">
                    <div class="icon-wrapper" style="background: #e0f2f1; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-calendar-check" style="color: #208b8b; font-size: 24px;"></i>
                    </div>
                    <div>
                        <h3 style="margin: 0; font-size: 24px; font-weight: 800; color: #0f172a;">25 Years</h3>
                        <p style="margin: 0; font-size: 14px; color: #64748b; font-weight: 500;">Experience</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 mb-4">
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); padding: 25px 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: center; gap: 15px;">
                    <div class="icon-wrapper" style="background: #e0f2f1; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-headset" style="color: #208b8b; font-size: 24px;"></i>
                    </div>
                    <div>
                        <h3 style="margin: 0; font-size: 24px; font-weight: 800; color: #0f172a;">24/7</h3>
                        <p style="margin: 0; font-size: 14px; color: #64748b; font-weight: 500;">Support</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- Stats Section Ends -->
'''

destinations_html = '''
<!-- Featured Destinations Slider -->
<section class="trending pb-5 pt-8">
    <div class="container">
        <div class="section-title mb-5 w-50 mx-auto text-center">
            <h2 class="mb-1" style="font-weight: 800; color: #0f172a;">Featured Destinations</h2>
        </div>
        
        <div class="swiper-container dest-slider">
            <div class="swiper-wrapper">
                <!-- Slide 1: Egypt -->
                <div class="swiper-slide">
                    <div class="trend-item1" style="margin: 0 10px;">
                        <a href="/en/destinations/egypt/">
                            <div class="trend-image position-relative" style="border-radius: 24px; overflow: hidden; height: 300px;">
                                <img src="/images/uploads/excellent-tours-Home-9bc84.webp" alt="Egypt" style="width: 100%; height: 100%; object-fit: cover;">
                                <div class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index" style="background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);">
                                    <div class="trend-content-title">
                                        <h3 class="mb-0 white" style="font-weight: 700; font-size: 28px;">Egypt</h3>
                                        <p class="white mb-0" style="font-size: 14px;">54 Tours</p>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
                <!-- Slide 2: Dubai -->
                <div class="swiper-slide">
                    <div class="trend-item1" style="margin: 0 10px;">
                        <a href="/en/destinations/dubai/">
                            <div class="trend-image position-relative" style="border-radius: 24px; overflow: hidden; height: 300px;">
                                <img src="/images/uploads/excellent-tours-Home-6e439.webp" alt="Dubai" style="width: 100%; height: 100%; object-fit: cover;">
                                <div class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index" style="background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);">
                                    <div class="trend-content-title">
                                        <h3 class="mb-0 white" style="font-weight: 700; font-size: 28px;">Dubai</h3>
                                        <p class="white mb-0" style="font-size: 14px;">42 Tours</p>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
            <!-- Pagination if needed -->
            <div class="swiper-pagination"></div>
        </div>
    </div>
</section>

<script>
document.addEventListener('DOMContentLoaded', function() {
    new Swiper('.dest-slider', {
        slidesPerView: 2,
        spaceBetween: 20,
        autoplay: {
            delay: 2000,
            disableOnInteraction: false,
        },
        loop: true,
        breakpoints: {
            320: { slidesPerView: 1 },
            768: { slidesPerView: 2 }
        }
    });
});
</script>
<!-- Featured Destinations Ends -->
'''

def process_index(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return

    original_html = html

    # 1. Update Hero Text (Explore the world style)
    # Replace the text inside swiper-content for Egypt
    egypt_hero = '''
                            <div class="swiper-content text-start" style="padding-left: 10%;">
                                <h1 class="mb-2" style="font-size: 64px; font-weight: 900; line-height: 1.1; text-transform: uppercase;">
                                    <span style="color: #fff; text-shadow: 0 2px 10px rgba(0,0,0,0.3);">EXPLORE<br>THE WORLD</span>
                                </h1>
                                <p class="white mb-4" style="font-size: 18px; max-width: 500px; text-shadow: 0 2px 5px rgba(0,0,0,0.5);">
                                    Discover unforgettable adventures and curated travel experiences in Egypt.
                                </p>
                                <a href="https://wa.me/201277273438" class="nir-btn" style="background: #fff; color: #0f172a; border-radius: 50px; font-weight: 700; padding: 12px 30px;">Book Now <i class="fa fa-angle-right ms-2"></i></a>
                            </div>
    '''
    dubai_hero = '''
                            <div class="swiper-content text-start" style="padding-left: 10%;">
                                <h1 class="mb-2" style="font-size: 64px; font-weight: 900; line-height: 1.1; text-transform: uppercase;">
                                    <span style="color: #fff; text-shadow: 0 2px 10px rgba(0,0,0,0.3);">EXPLORE<br>THE WORLD</span>
                                </h1>
                                <p class="white mb-4" style="font-size: 18px; max-width: 500px; text-shadow: 0 2px 5px rgba(0,0,0,0.5);">
                                    Discover unforgettable adventures and curated travel experiences in Dubai.
                                </p>
                                <a href="https://wa.me/201277273438" class="nir-btn" style="background: #fff; color: #0f172a; border-radius: 50px; font-weight: 700; padding: 12px 30px;">Book Now <i class="fa fa-angle-right ms-2"></i></a>
                            </div>
    '''
    # We replace the old swiper-content block in index.html
    html = re.sub(r'<div class="swiper-content">.*?<div class="entry-meta mb-2">.*?<h5 class="entry-category mb-0 white">Explore Egypt</h5>.*?</div>.*?<a href="https://wa\.me/201277273438"[^>]*>.*?</a>\s*</div>', egypt_hero, html, flags=re.DOTALL)
    html = re.sub(r'<div class="swiper-content">.*?<div class="entry-meta mb-2">.*?<h5 class="entry-category mb-0 white">Explore Dubai</h5>.*?</div>.*?<a href="https://wa\.me/201277273438"[^>]*>.*?</a>\s*</div>', dubai_hero, html, flags=re.DOTALL)

    # 2. Replace Why Us / About Us section with Stats Section
    html = re.sub(r'<section class="about-us pt-10".*?<!-- why us ends -->\s*</div>\s*<div class="white-overlay"></div>\s*</section>', stats_html, html, flags=re.DOTALL)
    
    # 3. Remove Counter section entirely (it's redundant now)
    html = re.sub(r'<!-- counter -->\s*<section class="featured-counter bg-theme pb-6 pt-10">.*?</section>', '', html, flags=re.DOTALL)
    
    # 4. Replace Top Destinations with the new Slider version
    html = re.sub(r'<!-- top destinations -->\s*<section class="trending pb-5 pt-10">.*?</section>', destinations_html, html, flags=re.DOTALL)

    if html != original_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            print(f"Updated {filepath}")

process_index(r'd:\vabi voding\new-redesign\index.html')
