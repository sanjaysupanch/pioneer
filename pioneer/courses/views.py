from django.shortcuts import render


def course(request):
    return render(request, "courses/course_list.html", {})

def b_to_adv(request):
    return render(request, "courses/b_to_adv.html", {})

def speaking(request):
    return render(request, "courses/course_speaking.html", {})

def expository(request):
    return render(request, "courses/course_expository.html", {})

def vocabulary(request):
    return render(request, "courses/course_vocabulary.html", {})

def c_segment(request):
    return render(request, "courses/course_segment.html", {})

def grammar(request):
    return render(request, "courses/course_grammar.html", {})

def about_us(request):
    return render(request, "courses/about_us.html", {})
