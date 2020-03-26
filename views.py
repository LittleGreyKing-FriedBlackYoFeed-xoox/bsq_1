from django.shortcuts import render,render_to_response

def demo(request):
    return render_to_response("user/demo.html")