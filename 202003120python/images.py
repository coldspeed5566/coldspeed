from jinja2 import Template

def getHtm():
    with open('items.html') as f:
        s = f.read()
    return s

def main():
    item_list = [
        { 'title': 'apple;', 'url' : "https://stonecampus.net/img/weblogo.png"}
    ]
    tmpl = Template(getHtml())
    print(tmpl.render({ 'images': images_list }))

main()