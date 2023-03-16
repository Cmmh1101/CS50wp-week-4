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
        'title': title.lower(),
        'entry': util.get_entry(title) 
    })

def search(request):
    if request.method == "POST":
        query = request.POST['q'].lower()
        entry = util.get_entry(query)
        if entry is not None:
            return render(request,'encyclopedia/entry.html', {
                "title": query,
                'entry': entry
            })
        else:
            entries = util.list_entries()
            resultList = []
            for entry in entries:
                if query in entry.lower():
                    resultList.append(entry)
            return render(request, 'encyclopedia/search.html', {
                'resultList': resultList
            })

def add_entry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/add.html", {

    })

