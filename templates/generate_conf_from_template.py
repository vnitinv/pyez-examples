import yaml
from jinja2 import Template

data = yaml.load(open('data_vars.yaml'))
print data

tmpl = Template(open('template.j2').read())
conf = tmpl.render(data)
print conf
