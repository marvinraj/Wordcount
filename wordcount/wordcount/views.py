from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'wordcount/home.html')

def action(request):
    return render(request, 'wordcount/action.html')    

def count(request):
    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            #increase
            wordDictionary[word] += 1
        else:
            #add to dictionary
            wordDictionary[word] = 1

    sortedwords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    
    return render(request, 'wordcount/count.html', {'fulltext':fulltext, 'countwords':len(wordList), 'sortedwords':sortedwords})