from django.shortcuts import render
from django.views.generic import View
from .functions import scrapper
from django.http import JsonResponse


# Create your views here.

class VerifyDocView(View):
	"""a view that renders the verify page and and also performs the verification"""
	template_name = 'verify.html'
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)
	def get(self, request):
		return render(request, self.template_name)
	def post(self, request):
		print(request.POST)
		doc_reg = request.POST['doc_num']
		try:
			result = scrapper(doc_reg)
			if result == "found":
				res = {'msg': "found", 'doc_no': doc_reg }
			else:
				res = {'msg': "not found", 'doc_no': doc_reg }
		except Exception as e:
			print(e)
			res = {'msg': "error"}
		return JsonResponse({'res': res})

		


	

