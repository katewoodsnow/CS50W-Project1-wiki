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

# Displays the contents of the subject/title searched for
def entry(request, title):
    content = util.get_entry(title)
    if not content:
        return render(request, "encyclopedia/error.html", {
            "message": "Sorry, this entry does not exist"
        })
        
    else:
        return render(request, "encyclopedia/entry.html", {
            "content": content,
            "title": title,
        })




