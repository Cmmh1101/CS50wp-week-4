from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    entry = util.get_entry(title)
    if entry is not None:
        return render(request, 'encyclopedia/entry.html', {
            'title': title.lower(),
            'entry': entry 
        })
    else:
        return render(request, "encyclopedia/error_page.html", {
            "error_message": "Entry not founddddddd"
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
        return render(request, "encyclopedia/add.html")
    else: 
       data = request.POST
       title = data.get('title')
       content = data.get('add_content')
       duplicated = util.get_entry(title)
       if duplicated is not None:
          return render(request, "encyclopedia/error_page.html", {
            "error_message": "An entry with the same title already exists"
           }) 
       else:
          util.save_entry(title, content)
          entry = util.get_entry(title)
          return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
          })


