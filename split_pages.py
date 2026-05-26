import os
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

header_match = re.search(r'(<!DOCTYPE html>.*?</header>)', html, re.DOTALL)
header_str = header_match.group(1)

footer_match = re.search(r'(<footer.*</html>)', html, re.DOTALL)
footer_str = footer_match.group(1)

nav_map = {
    '#about': 'index.html',
    '#history': 'history.html',
    '#organization': 'organization.html',
    '#partners': 'partners.html',
    '#services': 'services.html',
    '#esg': 'esg.html',
    '#certifications': 'certifications.html',
}

for old, new in nav_map.items():
    header_str = header_str.replace(f'href="{old}"', f'href="{new}"')

sections = [
    ('about', '회사 소개', 'COMPANY'),
    ('history', '회사 연혁', 'HISTORY'),
    ('organization', '조직도', 'ORGANIZATION'),
    ('partners', '함께하는 파트너', 'PARTNERS'),
    ('services', '우리의 서비스', 'SERVICES'),
    ('esg', 'ESG 경영', 'ESG STRATEGY'),
    ('certifications', '인증현황', 'CERTIFICATIONS')
]

for sid, title_ko, title_en in sections:
    regex = rf'<section id="{sid}".*?</section>'
    match = re.search(regex, html, re.DOTALL)
    if not match:
        continue
    content = match.group(0)
    
    hero = f"""
    <section class="hero-section">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>{title_ko}</h1>
            <p>{title_en}</p>
        </div>
    </section>
    <main>
"""
    
    out_html = header_str + hero + content + '\n    </main>\n\n    ' + footer_str
    
    out_file = f'{sid}.html'
    if sid == 'about':
        out_file = 'index.html'
        
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(out_html)

print("Pages split successfully.")
