from django.http import HttpResponse
from django.shortcuts import render

import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'count': len(word_list),
                                          'char': len(fulltext),
                                          'sorted_words': sorted_words})


def about(request):
    return render(request, 'about.html', {'name': 'Sujay', 'designation': 'CEO', 'mobile': 8123235678})


