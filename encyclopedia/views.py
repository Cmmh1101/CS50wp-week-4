import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from . import util

def get_html_entry(title):
    entry_to_conver = util.get_entry(title)
    markdowner = Markdown()
    if entry_to_conver == None:
        return None
    else:
        return markdowner.convert(entry_to_conver)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    entry = get_html_entry(title)
    if entry is not None:
        return render(request, 'encyclopedia/entry.html', {
            'title': title.lower(),
            'entry': entry 
        })
    else:
        return render(request, "encyclopedia/error_page.html", {
            "error_message": "Entry not found"
        })

def search(request):
    if request.method == "POST":
        query = request.POST['q'].lower()
        entry = get_html_entry(query)
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
       duplicated = get_html_entry(title)
       if duplicated is not None:
          return render(request, "encyclopedia/error_page.html", {
            "error_message": "An entry with the same title already exists"
           }) 
       else:
          util.save_entry(title, content)
          entry = get_html_entry(title)
          return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
          })

def edit_entry(request):
    if request.method == "POST":
        title = request.POST["entry_title"]
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit_entry.html", {
            "title": title,
            "entry": entry 
        })

def save_entry(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        content = data.get('edit_content')
        util.save_entry(title, content)
        entry = get_html_entry(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
          })

def random_entry(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    entry = get_html_entry(random_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": random_entry,
        "entry": entry 
    })
