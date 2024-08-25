from django.shortcuts import render, HttpResponse

topics = [
  {'id':1, 'title': 'routing', 'body': 'Routing is ..'},
  {'id':2, 'title': 'view', 'body': 'View is ..'},
  {'id':3, 'title': 'model', 'body': 'Model is ..'}
]

def HTMLTemplate(articleTage):
  global topics
  ol = ''
  for topic in topics:
    ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
  return f'''
  <html>
    <body>
        <h1> Django </h1>
        <ol>
          {ol}           
        </ol>
        {articleTage}
        <ul>
          <li><a href="create/">create</a></li>
        </ul>
    </body>
  </html>
  '''

def index(request):
  article='''
  <h2>Welcome</h2>
  Hello, Django
'''
  return(HttpResponse(HTMLTemplate(article)))

def create(request):
  article = '''
  <form action="/create/">
    <p><input type="text" name="title" placeholder="title"></input></p>
    <p><textarea name="body" placeholder="body"></textarea></p>
    <p><input type="submit"></input></p>
  </form>
'''
  return HttpResponse(HTMLTemplate(article))

def read(request, id):
  return HttpResponse('Read!'+ id)
