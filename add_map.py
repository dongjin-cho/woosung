import glob

html_files = glob.glob('*.html')

old_footer = """            <div class="footer-info">
                <h3>우성기업(주)</h3>
                <p>소재지: 경기도 화성시 송산면 송산산단1길 58</p>
                <div class="contact-details">
                    <span><strong>Tel.</strong> 031-357-9611</span>
                    <span><strong>Fax.</strong> 031-357-9615</span>
                    <span><strong>E-mail</strong> woosung.contact@gmail.com</span>
                </div>
            </div>"""

new_footer = """            <div class="footer-top" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; width: 100%;">
                <div class="footer-info">
                    <h3 style="margin-bottom: 10px;">우성기업(주)</h3>
                    <p style="margin-bottom: 15px;">소재지: 경기도 화성시 송산면 송산산단1길 58</p>
                    <div class="contact-details" style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 10px;">
                        <span><strong style="color:var(--accent-color);">Tel.</strong> 031-357-9611</span>
                        <span><strong style="color:var(--accent-color);">Fax.</strong> 031-357-9615</span>
                        <span><strong style="color:var(--accent-color);">E-mail</strong> woosung.contact@gmail.com</span>
                    </div>
                </div>
                <div class="footer-map">
                    <iframe src="https://maps.google.com/maps?q=경기도%20화성시%20송산면%20송산산단1길%2058&t=&z=14&ie=UTF8&iwloc=&output=embed" width="300" height="150" style="border:0; border-radius: 8px;" allowfullscreen="" loading="lazy"></iframe>
                </div>
            </div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_footer, new_footer)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Maps added.")
