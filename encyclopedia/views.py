from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    return render(request, 'encyclopedia/entry.html', {
        'title': title.capitalize(),
        'entry': util.get_entry(title) 
    })

def search(request):
    if request.method == "POST":
        query = request.POST['q'].capitalize()
        entry = util.get_entry(query)
        if entry is not None:
            return render(request,'encyclopedia/entry.html', {
                "title": query,
                'entry': entry
            })
        
