from google.appengine.ext import webapp
import webapp2,cgi
from google.appengine.ext.webapp.util import run_wsgi_app

table=[('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]

def int_to_roman (integer):
    parts = []
    for letter, value in table:
        while value <= integer:
            integer -= value
            parts.append(letter)
    return ''.join(parts)

def rom_to_int(string):
    result = 0
    for letter, value in table:
        while string.startswith(letter):
            result += value
            string = string[len(letter):]
    return result

MAIN_PAGE_HTML = """\
<!DOCTYPE html>
<html>
  <head>
    <link type="text/css" rel="stylesheet" href="/assets/stylesheets.css" />
  </head>
  <body style="background-image: url('assets/background.jpg');
    font-family: Verdana, Helvetica, sans-serif;
    background-size: cover;
    background-repeat: no-repeat;
    width: 100px;
    height: 100px;
    position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;>
    <form action="/roman" method="post">
        <textarea name="number" rows="1" cols="10"></textarea>
        <input type="submit" value="Convert to Roman" style="
        color:white;
        padding:5px 15px; 
        background:#ff3300;
        border:0
        border-style:none;
        box-shadow:none;
        cursor:pointer; 
        border: 0;">
    </form>
    <form action="/number" method="post">
        <textarea name="roman" rows="1" cols="10"></textarea>
        <input type="submit" value="Convert to Integer" style="color:white;
        padding:5px 15px; 
        background:#ff3300;
        border:0
        border-style:none;
        box-shadow:none;
        cursor:pointer;
        border: 0;"> 
    </form>
  </body>
</html>
"""

RESULT="""\
<!DOCTYPE html>
<html>
  <head>
    <link type="text/css" rel="stylesheet" href="/assets/stylesheets.css" />
  </head>
  <body style="background-image: url('assets/background.jpg');
    font-family: Verdana, Helvetica, sans-serif;
    background-size: cover;
    background-repeat: no-repeat;
    color:white">
    <div style="
    width: 90%;
    width: 100px;
    height: 100px;
    position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;">
    <div>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class IntToRoman(webapp2.RequestHandler):
    def post(self):
        number=cgi.escape(self.request.get('number'))
        self.response.write(RESULT+number+' in Roman is :<pre>')
        self.response.write(int_to_roman(int(number)))
        self.response.write('<</pre></div></body></html>')

class RomanToInt(webapp2.RequestHandler):
    def post(self):
        number=cgi.escape(self.request.get('roman'))
        self.response.write(RESULT+number+' in Integer is :<pre>')
        self.response.write(rom_to_int(number))
        self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/roman', IntToRoman),
    ('/number', RomanToInt),
], debug=True)
