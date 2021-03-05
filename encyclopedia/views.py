from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2, random

from . import util, forms

md = markdown2.Markdown()
all_entries = util.list_entries()
content = 0
title = 0

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()  
    })

def Entry(request,title):
    
    entryPage = util.get_entry(title)

    if entryPage is None:
        return render(request, "encyclopedia/error.html",{
            "error": title
        })
    return render(request,"encyclopedia/entry.html",{
        "title": title,
        'entryPage': md.convert(util.get_entry(title))
    })

def SearchPage(request):
    if request.method == "GET":
        search = request.GET.get("q")
       

    possibleList = []

    if search is not None and search != "":
        search = search.strip()
        for filename in all_entries:
            if search.lower() == filename.lower():
                return render(request, "encyclopedia/search.html", {
                    "title": filename,
                    "entryPage": md.convert(util.get_entry(filename))
                })
            elif search.lower() in filename.lower():
                possibleList.append(filename)
    
    if len(possibleList) < 1:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()  
        })
    return render(request, "encyclopedia/search.html", {
        "entries": possibleList
    })

title = "Create a page"
def CreatNewPage(request):
    
    if request.method == "POST":
        form = forms.NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].lower()
            content = form.cleaned_data["content"]

            for filename in all_entries:
                if title == filename.lower():
                    return render(request, "encyclopedia/ExistingPageErro.html", {
                        "title": filename.capitalize()
                    })

            util.save_entry(title.capitalize(), content)
            return HttpResponseRedirect(reverse("Entry", args=(title.capitalize())))
		  

    return render(request, "encyclopedia/newpage.html", {
        "title": forms.NewPageForm()
    })

def edit(request):


    title = request.POST.get("edit")
    content = util.get_entry(title)
    
    edit_form = forms.EditPageForm(initial={'pagename': title, 'body':content})
    if edit_form.is_valid():
        return render (request, "encyclopedia/edit.html",{
                "title": title,
                "EntryPage":edit_form,

            })
    else:
        return render (request, "encyclopedia/edit.html",{
                "title": title,
                "EntryPage":edit_form,
        })

def savePage(request):
	
	form = forms.EditPageForm(request.POST)
	if form.is_valid():
		title = form.cleaned_data["pagename"]
		content = form.cleaned_data["body"]
		util.save_entry(title, content)
		return Entry(request, title)
	return render(request, "encyclopedia/edit.html", {
	
	"EntryPage": forms.EditPageForm()
	})

def	randomPage(request):
	
	return Entry(request, random.choice(all_entries))
