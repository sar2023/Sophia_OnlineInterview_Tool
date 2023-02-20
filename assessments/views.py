from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from assessments.models import videoAns
from administration.models import allAssessment, userFeedback , Question
from django.contrib.auth import authenticate

# Create your views here.


@login_required(login_url='login')
def welcomeScreen(request,ass_name):
    global slug 
    slug = ass_name
    return render(request, 'welcomscreen.html')


@login_required(login_url='login')
def questionScreen(request):
    return render(request, 'question.html')


@login_required(login_url='login')
def answer(request):
    ass_name = slug
    assname = ass_name
    allque = allAssessment.objects.get(assessmentName=ass_name).question_set.all()
    return render(request, 'answer.html', {'question':allque , 'assname':assname} )


@login_required(login_url='login')
def fileUpload(request):

    if request.method == 'POST':
        
        fileName = request.POST.get('fileName')
        video = request.FILES.get('data')
        assname = request.POST.get('assessmentName')
        videoAns.objects.create(
            user_name=fileName,
            videoAns=video,
            assessment_name=assname)

        return redirect('login')


@login_required(login_url='login')
def feedback(request):
    if request.method == 'POST':


        feedback =request.POST.get('value', False)

        userFeedback.objects.create(
            feedback = feedback)

        return redirect('thankyou')
    return render(request,'feedback.html')

@login_required(login_url='login')
def thankyou(request):
    return render(request,'thankyou.html')




