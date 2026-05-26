import os
import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert burger menu before </nav> or after </nav>? Let's put it inside header-container
    if '<div class="burger-menu"' not in content:
        content = content.replace('</nav>', '</nav>\n            <div class="burger-menu" id="burger-menu">\n                <span></span>\n                <span></span>\n                <span></span>\n            </div>')
    
    # Insert script before </body>
    if '<script src="script.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="script.js"></script>\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files updated.")
