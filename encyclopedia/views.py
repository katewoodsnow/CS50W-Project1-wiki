from django.shortcuts import render

from . import util

# views file decides what the user sees when they visit a particular route
# functions are used for the view. Request is the http request made by the user in order to access the web server
# tell the app what url the user is going to visit in order to return the response in the function
# tell Django when the url is visited then this function should be run in able to return the list of entries in the
# encyclopedia
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "contents": util. get_entry(title)
    })




