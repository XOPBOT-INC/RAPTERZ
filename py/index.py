import codecs
import webbrowser
f = open('second.html', 'w')
html_template = """<html><head><script>function click() { const x = document.getElementById("rar");x.write("Hello!"); }</script></head><body><h1>HELLO WORLD | 2!</h1><button id="rar" onclick="click()">Click ME</button></body></html>"""
f.write(html_template)
f.close()
file = codecs.open("second.html", 'r', "utf-8")
print(file.read())
webbrowser.open('second.html')