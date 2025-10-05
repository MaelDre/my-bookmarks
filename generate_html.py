import json
from pathlib import Path

# Entrée et sortie
input_file = Path("data/favoris.json")
output_file = Path("output.html")

# Lecture du JSON
with input_file.open(encoding="utf-8") as f:
    data = json.load(f)

# Conversion en HTML
html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Rapport JSON</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #fafafa;
            padding: 2em;
        }}
        pre {{
            background: #eee;
            padding: 1em;
            border-radius: 8px;
        }}
        h1 {{
            color: #333;
        }}
    </style>
</head>
<body>
    <h1>Données JSON converties</h1>
    <pre>{json.dumps(data, indent=2, ensure_ascii=False)}</pre>
</body>
</html>
"""

# Écriture du fichier HTML
with output_file.open("w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Fichier HTML généré : {output_file.resolve()}")
