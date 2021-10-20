import cgi
import json

s_data = cgi.FieldStorage()
s1 = s_data.getvalue('slider')
b1 = s_data.getvalue('button')
data = {"slider":s1, "button":b1}
with open('lab4_CGI.txt', 'w') as f:
  json.dump(data,f)


print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/lab4py.py" method="POST">')
print('<input type="range" name="slider" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" name ="button" value=”Change Brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')

