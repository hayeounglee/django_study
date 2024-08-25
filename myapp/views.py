from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

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

@csrf_exempt
def create(request):
  global nextId
  if request.method == 'GET':
    article = '''
    <form action="/create/" method="post">
      <p><input type="text" name="title" placeholder="title"></input></p>
      <p><textarea name="body" placeholder="body"></textarea></p>
      <p><input type="submit"></input></p>
    </form>
    '''
    return HttpResponse(HTMLTemplate(article))
  elif request.method == 'POST':
    title = request.POST['title']
    body = request.POST['body']
    newTopic = {"id":nextId, "title":title, "body":body}
    topics.append(newTopic)
    nextId = next + 1
    url = '/read/'+str(nextId)
    return redirect(url)

def read(request, id):
  return HttpResponse('Read!'+ id)
