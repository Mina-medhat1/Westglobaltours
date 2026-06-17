with open(r'd:\vabi voding\new-redesign\TITSolutions\ws\css\redesign.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add Light Theme variables
light_theme = '''
/* Light Theme Colors */
[data-theme="light"] {
  --bg-main: #FFFFFF;
  --bg-secondary: #F8FAFC;
  --bg-glass: rgba(255, 255, 255, 0.85);
  
  --text-primary: #0F172A;
  --text-secondary: #334155;
  --text-muted: #64748B;
  
  --border-color: rgba(0, 0, 0, 0.1);
}
'''
if '[data-theme="light"]' not in css:
    css = css.replace('}', '}\n' + light_theme, 1)

# Remove smooth scroll
css = css.replace('scroll-behavior: smooth !important;', '/* scroll-behavior removed */')

# Add Airplane Preloader CSS
preloader_css = '''
/* Airplane Preloader */
#preloader {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: var(--bg-main) !important;
}
.airplane-loader {
    position: relative;
    width: 100px;
    height: 100px;
}
.globe-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 40px;
    color: var(--accent-primary);
    opacity: 0.8;
}
.plane-container {
    position: absolute;
    width: 100%;
    height: 100%;
    animation: fly-around 2s linear infinite;
}
.plane-icon {
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translate(-50%, -50%) rotate(90deg);
    font-size: 24px;
    color: var(--text-primary);
}
@keyframes fly-around {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
'''
if 'Airplane Preloader' not in css:
    css += '\n' + preloader_css

with open(r'd:\vabi voding\new-redesign\TITSolutions\ws\css\redesign.css', 'w', encoding='utf-8') as f:
    f.write(css)
