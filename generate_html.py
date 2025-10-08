import json
from pathlib import Path


# Entrée et sortie
input_file = Path("data/favoris.json")
output_file = Path("outpute.html")

# Lecture du JSON
with input_file.open(encoding="utf-8") as f:
    favoris = json.load(f)

#favoris = json.load(open("data/favoris.json", encoding="utf-8"))
html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Mes Favoris</title>
    <style>
    body { font-family: Arial; margin: 20px; }
    a { text-decoration: none; color: blue; }
    li { margin-bottom: 6px; }
    </style>
    </head>
    <body>
    <h1>Mes Favoris</h1>
    <ul>
"""
for fav in favoris:
    title = fav["title"] or fav["url"]
    html += f'<li><a href="{fav["url"]}" target="_blank">{title}</a>'
    if fav["description"]:
        html += f" – {fav['description']}"
    html += "</li>\n"

html += """
</ul>
</body>
</html>
"""


# Écriture du fichier HTML
with output_file.open("w", encoding="utf-8") as f:
    f.write(html_content)
    
# Pth("indexeu.html").write_text(html, encoding="utf-8")
print("✅ Page HTML générée : indexeu.html")
