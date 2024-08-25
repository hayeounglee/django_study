from django.shortcuts import render, HttpResponse

topics = [
  {'id':1, 'title': 'routing', 'body': 'Routing is ..'},
  {'id':2, 'title': 'view', 'body': 'View is ..'},
  {'id':3, 'title': 'model', 'body': 'Model is ..'}
]


def index(request):
  global topics
  ol = ''
  for topic in topics:
    ol += f'<li>{topic}</li>'
  return HttpResponse('''
  <html>
    <body>
        <h1> Django </h1>
        <ol>
          <li> routing </li>
          <li> view </li>
          <li> model </li>            
        </ol>
    </body>
  <html>
  ''')

def create(request):
  return HttpResponse("Create")

def read(request, id):
  return HttpResponse('Read!')
