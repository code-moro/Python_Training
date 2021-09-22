from jinja2 import Environment ,FileSystemLoader
persons = [
    {"name" : "Mayur","Age":21},
    {"name" : "Aniket", "Age": 23},
    {"name" : "yash", "Age": 18},
    {"name" : "sanket", "Age": 15}
]

file_loader = FileSystemLoader('Templates')
env = Environment(loader=file_loader)
Templates = env.get_template('show.txt')

output = Templates.render(persons=persons)
print(output)