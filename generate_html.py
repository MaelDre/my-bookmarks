import json
from pathlib import Path

favoris = json.load(open("favoris.json", encoding="utf-8"))
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
    title = fav["titre"] or fav["url"]
    html += f'<li><a href="{fav["url"]}" target="_blank">{title}</a>'
    if fav["description"]:
        html += f" – {fav['description']}"
    html += "</li>\n"

html += """
</ul>
</body>
</html>
"""

Path("output.html").write_text(html, encoding="utf-8")
print("✅ Page HTML générée : output.html")
