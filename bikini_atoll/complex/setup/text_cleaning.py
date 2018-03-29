#!/usr/bin/env python3


filename = 'test.txt'

with open(filename, 'r') as f:
    s = f.readline()
    keywords = []
    for s in f:
        keywords.append('_' + s[:-1] + '_greg_')
    keywords = list(set(keywords))

for word in keywords:
    if " " in word:
        res_word = word
        word = word.replace(' ', '_')
    else:
        res_word = word[1:-6]
    with open("../run/core/templates/{word}.html".format(word=word), "w+") as t:
        t.write('{% extends "template.html" %}')
        t.write("\n{% block main %}\n")
        t.write("<h1>\n")
        t.write("{0}".format(res_word))
        t.write("</h1>")
        t.write("\n{% endblock main %}\n")
    #copyfile("template.py", "/Users/Greg/byteacademy/monza/bikini_atoll/complex/run/core/controllers/controller_trash/{word}.py".format(word=word))
    with open("../run/core/controllers/controller_trash/{word}.py".format(word=word), 'w+') as c:
        c.write("#!/usr/bin/env python3")
        c.write("\nfrom flask import Blueprint, render_template")
        c.write("\ncontroller = Blueprint('{word}', __name__, url_prefix='/{res_word}')".format(word=word, res_word=res_word))
        c.write("\n@controller.route('/', methods=['GET'])")
        c.write("\ndef show_{word}():".format(word=word))
        c.write("\n   return render_template('{word}.html')".format(word=word))
    with open("../run/core/__init__.py", 'a') as i:
        i.write('\nfrom core.controllers.controller_trash.{word} import controller as {word}'.format(word=word))
        i.write('\nomnibus.register_blueprint({word})'.format(word=word))
    with open("../run/core/templates/index.html", 'a') as h:
        h.write("\n<a href = \"/{res_word}\">{res_word}</a><br>".format(res_word=res_word))
with open("../run/core/templates/index.html", 'a') as h:
    #h.write("</p>\n")
    #h.write("</select>\n")
    #h.write("<button class=\"btn btn-lg btn-primary btn-block\" type=\"submit\">Submit</button>\n")
    #h.write("</fieldset>\n")
    #h.write("</form>\n")
    h.write("\n{% endblock main %}\n")


print('---------------------------------')
print('           All done!!            ')
print('---------------------------------')

