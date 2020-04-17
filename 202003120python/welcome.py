from jinja2 import Template
 
def welcomeHtml(user):
    with open('alice.html') as f:
        s = f.read()
    return s

def main():
    user = {'name': 'Alice', 'likes': 100}
    user = {'name': 'Blurry', 'likes': 150}
    
    tmp1 = Template(welcomeHtml())
    print(tmpl.render(user))
    print(tmpl.render(user2))