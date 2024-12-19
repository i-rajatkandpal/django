from django.http import HttpResponse

def index(request):
    html = """
    <h1>Welcome to the Home Page</h1>
    <ul>
        <li><a href="removepunc">Remove Punctuation</a></li>
        <li><a href="capfirst">Capitalize First</a></li>
        <li><a href="newlineremove">Newline Remover</a></li>
        <li><a href="spaceremove">Space Remover</a></li>
        <li><a href="charcount">Character Count</a></li>
    </ul>
    """
    return HttpResponse(html)

def removepunc(request):
    return HttpResponse('''Remove punctuation <br> <a href = "/"> back </a>''')

def capfirst(request):
    return HttpResponse('''Capitalize first <br> <a href = "/"> back </a>''')

def newlineremove(request):
    return HttpResponse('''Remove newlines <br> <a href = "/"> back </a>''')

def spaceremove(request):
    return HttpResponse('''Remove spaces <br> <a href = "/"> back </a>''')

def charcount(request):
    return HttpResponse('''Character count <br> <a href = "/"> back </a>''')
