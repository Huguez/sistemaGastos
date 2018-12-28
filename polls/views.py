from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Gasto #,  Question, Choice


class IndexView( generic.ListView ):
	template_name = 'polls/index.html'
	context_object_name = 'lista_Gastos'

	def get_queryset(self):
		return Gasto.objects.order_by()[:]
		#return Question.objects.filter( pub_date__lte = timezone.now()).order_by( '-pub_date' )[:]



"""
detail
try:
	question = Question.objects.get( pk = question_id )
	return render( request, 'polls/detail.html',{'question':question} )
except Question.DoesNotExist:
	raise Http404("Question no existe.")


class DetailView( generic.DetailView ):
	model = Question
	template_name = 'polls/detail.html'
	
	def get_queryset(self):
		return Question.objects.filter( pub_date__lte = timezone.now() )


class ResultView(generic.DetailView):
	model = Question
	template_name = 'polls/result.html'


def index(request):
	latest_question = Question.objects.order_by('-pub_date')[:]
	template = loader.get_template('polls/index.html')
	context = { 'latest_question': latest_question }
	return HttpResponse( template.render( context, request ) )


def detail( request, question_id ):
	question = get_object_or_404( Question, pk = question_id)
	return render( request, 'polls/detail.html',{'question':question} )


def result( request, question_id ):
	question = get_object_or_404( Question, pk = question_id )
	return render( request, 'polls/result.html', { 'question': question } )


def vote( request, question_id ):
	question = get_object_or_404( Question, pk = question_id )
	selected_choice = None
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except ( KeyError, Choice.DoesNotExist ):
		return render( request, 'polls/detail.html',{ 'question':question, 'error_message':"tu no selecionaste nada hacker" } )
	else:
		selected_choice.votes += 1
		selected_choice.save()
		
		_url = reverse( 'polls:result', args = (question.id,) )

		return HttpResponseRedirect( _url )

"""