#Höfundur: Huginn Þór Jóhannsson
from bottle import *
from sys import argv
@error(404)
def notFound(error):
    return "404 not found :/"

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/')
@route('/index')
def index():
    return '''
    <h1>Verkefni 3</h1>
    <ul>
    <li><a href="/A?id=A">Verkefni A</a></li>
    <li><a href="/B?id=B">Verkefni B</a></li>
    </ul>
    '''
@route('/A')
def A():
    #spurn=request.query.id
    #return spurn
    gervimadur=('Geir "Gervimaðurinn" Finnsson', 1212901990)
    huginn=("Huginn Þór Jóhannsson",2111002060)
    def display(tup):
        return template("<p>{{name}}: </p><a href='/sum?id={{number}}'>{{ number }}</a>",name=tup[0],number=tup[1])
    return display(huginn), display(gervimadur)
@route('/sum')
def summa():
    num=request.query.id
    summa = 0
    for x in num:
        x=int(x)
        summa += x
    return template("<h1>Þversumma</h1><p>Summa talnanna er {{ number }}</p>",number=summa)
@route('/B')
def B():
    #spurn=request.query.id
    #return spurn
    return template("index", efni="frett.tpl")

@route('/article')
def article():
    article_id=request.query.id
    frettir=[
            {'title': 'Irma Florida', 'body': 'Það er bara helv... vesen á Irmu í Flórída. Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...', 'author': 'Geirvimaðurinn G Finnsson'},
            {'title': 'Veiðin dræm', 'body': 'Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...', 'author': 'Gervikonan G Finnsdóttir'},
            {'title': 'Ólafía', 'body': 'Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...', 'author': 'Einhver annar fréttamaður'},
            {'title': 'Ísland eitthvað', 'body': 'Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli. Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..', 'author': 'Enn annar gaur'},
            ]
    frett=frettir[int(article_id)]
    return template("efni",title=frett["title"],myndid=article_id,body=frett["body"],author=frett["author"])

#run(host="localhost",port=8080,reloader=True,debug=True)
run(host="0.0.0.0",port=argv[1],debug=False)
