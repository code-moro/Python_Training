from jinja2 import Template


name = input("Enter Name")
tm = Template("Hello {{name}}")
msg = tm.render(name=name)
print(msg)
