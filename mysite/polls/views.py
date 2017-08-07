# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('/polls/ndex.html')
	context={
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context,request))

'''OR
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context={'latest_question_list': latest_question_list,}
	return render(request,/polls.index.html',context)
'''
def detail(request,question_id):
	try:
		question = Question.objects.get(question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request,'polls/detail.html',{'question': question})
'''OR
def detail(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request,'plss/detail.html',{'question':question})
'''

def results(request,question_id):
	return HttpResponse("You're lookng at the results of the question %s." %question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." %question_id)

	