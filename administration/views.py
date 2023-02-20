from unittest import result 
from django.shortcuts import render, redirect , HttpResponseRedirect 
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from assessments.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from assessments.models import *
from administration.models import *
from django.urls import reverse

def staffLogin(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'stafflogin.html', context)

@staff_member_required
@login_required(login_url='login')
def dashboard(request):
	assessment =allAssessment.objects
	video = videoAns.objects.all()[:5]
	return render(request, 'dashboard.html',{'assessment':assessment, 'video':video})


@staff_member_required
@login_required(login_url='login')
def allAnswer(request):
	video = videoAns.objects.all()
	return render(request, 'allAnswer.html',{'video':video})






@staff_member_required
@login_required(login_url='login')
def searchbar(request):
	if request.method == 'GET':
		search = request.GET.get('search')
		result = videoAns.objects.all().filter(user_name = search)
	return render(request, 'searchbar.html',{'result':result})
	
@staff_member_required
@login_required(login_url='login')
def Add_assessment(request):
	if request.method == 'GET':
		ass_name = request.GET.get('ass_name')
		ass_dec = request.GET.get('ass_dec')
		new_ass = allAssessment()
		new_ass.assessmentName = ass_name
		new_ass.assessmentDes = ass_dec
		new_ass.save()
		return redirect('dashboard')
	return redirect('dashboard')

def view_assessments(request,ass_id):
	ass_id = ass_id
	assessment = allAssessment.objects.filter(assId=ass_id)
	allque = allAssessment.objects.get(assId=ass_id).question_set.all()[:5]
	return render(request, 'assview.html',{'ques':allque,'ass':assessment})

def Add_question(request):	
		if request.method == 'GET':
			que = request.GET.get('que')
			ass_name = request.GET.get('ass')
			ass = allAssessment.objects.get(assessmentName = ass_name)
			ass_id = ass.assId
			new_que = Question()
			new_que.quostion = que
			new_que.assessment = ass
			new_que.save()
			return HttpResponseRedirect(reverse("view", args=(ass_id,)))
		return HttpResponseRedirect(reverse("view", args=(ass_id,)))
## ebb5f4cc42d841d0aa7369f975d9af42
def view_analysis (request,ansId):
	result = videoAns.objects.filter(ansId=ansId)


	return render(request, "analysis.html",{"result":result})
	


def generate_tras(request,ansId):
	result = videoAns.objects.get(ansId=ansId)
	vf = result.videoAns.path
	import requests
	import time

	API_KEY="623cfea0aba24d8f981195bbc20d48e0"
	filename = vf

#Upload Module Begins

	def read_file(filename, chunk_size=5242880):
		with open(filename, 'rb') as _file:
			while True:
				data = _file.read(chunk_size)
				if not data:
					break
				yield data

	headers = {'authorization': API_KEY}
	response = requests.post('https://api.assemblyai.com/v2/upload',
                        headers=headers,
                        data=read_file(filename))

	json_str1=response.json()

	print("upload_url:\t"+json_str1["upload_url"])

#Upload Module Ends

#Submit Module Begins

	endpoint = "https://api.assemblyai.com/v2/transcript"
	json = {
    	"audio_url": json_str1["upload_url"]
	}

	response = requests.post(endpoint, json=json, headers=headers)

	json_str2=response.json()

	print("id:\t\t"+json_str2["id"])

#Submit Module Ends

#CheckStatus Module Begins

	endpoint = "https://api.assemblyai.com/v2/transcript/" + json_str2["id"]

	response = requests.get(endpoint, headers=headers)

	json_str3=response.json()

	while json_str3["status"]!="completed":
		response = requests.get(endpoint, headers=headers)
		json_str3=response.json()
		print(json_str3["status"]+"...")
		time.sleep(15)

	print("\nStatus:"+json_str3["status"])
	print("Transcript:\n\t"+json_str3["text"])
	result.trasnscript = json_str3["text"]
	result.save()

#CheckStatus Module Ends


	return render(request, "generatetras.html",{"result":result})    		