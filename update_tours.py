import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Egypt Image
html = html.replace('url(/images/uploads/slider1.jpg)', 'url(/images/uploads/egypt_tour.png)')
html = html.replace('url(/images/uploads/slider2.jpg)', 'url(/images/uploads/dubai_tour.png)')

# Update Egypt Text
html = html.replace(
    'From the Pyramids and the Nile to the Red Sea, Egypt offers history, beauty, and adventure in one unforgettable journey.',
    'Experience the Magic of the Pharaohs. Embark on a luxurious journey through ancient history, golden deserts, and the breathtaking Nile.'
)

# Update Dubai Text
html = html.replace(
    'From iconic skyscrapers and luxury shopping to golden deserts and pristine beaches,\nDubai offers a world of experiences like no other.',
    'Step Into the Future of Luxury. Discover a world where gravity-defying architecture meets pristine golden sands and unmatched exclusivity.'
)
html = html.replace(
    'From iconic skyscrapers and luxury shopping to golden deserts and pristine beaches, Dubai offers a world of experiences like no other.',
    'Step Into the Future of Luxury. Discover a world where gravity-defying architecture meets pristine golden sands and unmatched exclusivity.'
)

# Change Loading Animation (Preloader)
old_preloader = '<div id=\"status\"></div>'
new_preloader = '<div id=\"status\" style=\"border: 4px solid var(--accent-primary); border-top: 4px solid transparent; border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite;\"></div><style>@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>'
html = html.replace(old_preloader, new_preloader)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
