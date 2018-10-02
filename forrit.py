#Höfundur: Huginn Þór Jóhannsson
from bottle import *
from sys import argv 
@route('/hello')
def helloworld():
    return '''
<p> Hello world!</p>
    '''
@route('/')
def index():
    return '''
<nav>
    <ul>
        <li><a href="/hello">Hello World</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/photos">Photos</a></li>
    </ul>
</nav>
    '''
@route('/photos')
def photos():
    return "<p>This is a photos page</p>"
@route('/about')
def about():
    return '''<p>This is an about page</p>'''
run(host="0.0.0.0",port=argv[1],debug=True)
