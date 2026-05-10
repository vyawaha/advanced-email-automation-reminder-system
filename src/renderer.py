from jinja2 import Template


def render_template(template_path, context):
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    template = Template(template_content)

    return template.render(context)