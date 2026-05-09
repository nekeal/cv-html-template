import importlib
import os
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from cv.common_context import common_context

ctx_module = sys.argv[1] if len(sys.argv) > 1 else "context"
context = importlib.import_module(ctx_module).context
output_path = "index.html"
root_dir = os.path.relpath(os.getcwd(), os.path.dirname(output_path))


render_context = common_context | context | {"root_dir": root_dir}

# Set up the environment
env = Environment(
    loader=FileSystemLoader("."), autoescape=False, undefined=StrictUndefined
)

# Load the template
template = env.get_template("templates/basic/cv_template.html.j2")

# Render the template with context data
rendered_html = template.render(render_context)

with open(output_path, "w+") as file:
    file.write(rendered_html)

print("CV rendered successfully!")
