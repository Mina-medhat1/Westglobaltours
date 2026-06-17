document.addEventListener('DOMContentLoaded', () => {
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
    }

    const toggleButton = document.getElementById('theme-toggle-btn');
    if (toggleButton) {
        toggleButton.addEventListener('click', function(e) {
            e.preventDefault();
            let theme = document.documentElement.getAttribute('data-theme');
            
            let icon = this.querySelector('i');
            if (theme === 'light') {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'dark');
                if (icon) { icon.classList.remove('fa-sun'); icon.classList.add('fa-moon'); }
            } else {
                document.documentElement.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
                if (icon) { icon.classList.remove('fa-moon'); icon.classList.add('fa-sun'); }
            }
        });
    }

    // Set initial icon state based on theme
    const icon = document.querySelector('#theme-toggle-btn i');
    if (icon && currentTheme === 'light') {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }
});
