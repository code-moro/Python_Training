from jinja2 import Template

name=input("Enter Name")
tm=Template("hello{{name}}")
msg=tm.render(name=name)

print(msg)

print(msg)
name='john'
age=25

tm=Template("my name is {{name}} and I am {{age}}")
msg=tm.render(name=name, age=age)
print(msg)