import json
from jinja2 import Environment, FileSystemLoader
import subprocess

with open("cv_data.json", encoding="utf-8") as f:
    data = json.load(f)

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("cv_template.tex.j2")
rendered = template.render(data)

with open("custom_cv.tex", "w", encoding="utf-8") as f:
    f.write(rendered)

# Uncomment to compile with pdflatex if available
# subprocess.run(["pdflatex", "custom_cv.tex"])