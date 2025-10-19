from django.shortcuts import render

def prof_test(req):
    return render(req, 'prof_tests/prof_test.html')
