from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    if request.method == "POST":
        Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
        # print Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
        # print Course.objects.all().values()
        # print "if statement"
        return redirect('/courses')
    else:
        context = {
            "all_courses": Course.objects.all()
        }
        print context, "hi"
        return render(request,'courses_app/index.html', context)
    # return render(request, 'courses_app/index.html')

def delete_conf(request, course_id):
    current_course = Course.objects.get(id=course_id)
    context = {
        'course': current_course
    }
    return render(request, 'courses_app/delete.html', context)
def delete(request, course_id):
    current_course = Course.objects.get(id=course_id)
    current_course.delete()
    return redirect('/courses')
# def new_course(request):
#     if request.method == "POST":
#         Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
#         # print Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
#         # print Course.objects.all().values()
#         # print "if statement"
#         return redirect('/courses')
#     else:
#         context = {
#             "all_courses": Course.objects.all()
#         }
#         print context, "hi"
#         return render(request,'courses_app/index.html', context)
