import cgi
data = cgi.FieldStorage()
s1 = data.getvalue('slider')

with open('led-pwm.txt', 'w') as f:
  f.write(str(s1))

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/lab4py.py" method="POST">')
print('<input type="range" name="slider" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value=”Change Brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')

