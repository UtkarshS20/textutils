# I created this file
from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("<h1>hello bitta</h1>")

def about(request):
    return HttpResponse("about bitta")
'''
'''     #check later
def textfile(request):
    f=open("1.txt","r")
    text = f.read()
    f.close()
    return HttpResponse(text)
'''
def index(request):
    return HttpResponse("Home "
                        "<br><button><a href='http://127.0.0.1:8000/removepunc'>Remove punc</a></button>"
                        " <br><button><a href='http://127.0.0.1:8000/capitalizefirst'>Capitalize First</a></button> "
                        "<br><button><a href='http://127.0.0.1:8000/newlineremove'>Remove NewLine</a></button> "
                        "<br><button><a href='http://127.0.0.1:8000/spaceremove'>Space Remover</a></button> "
                        "<br><button><a href='http://127.0.0.1:8000/charcount'>Charcount</a></button>")
def removepunc(request):
    return HttpResponse("Remove punc <br><button><a href='/'>Prev</a></button>")
def capfirst(request):
    return HttpResponse("Capitalize First <br><button><a href='/'>Prev</a></button>")
def newlineremove(request):
    return HttpResponse("Remove NewLine <br><button><a href='/'>Prev</a></button>")
def spaceremove(request):
    return HttpResponse("Space Remover <br><button><a href='/'>Prev</a></button>")
def charcount(request):
    return HttpResponse("Charcount <br><button><a href='/'>Prev</a></button>")
