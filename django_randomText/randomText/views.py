from django.shortcuts import render
from django.views.generic import TemplateView

from random import randint

#Some values that will be used
#in views

#HTML text
messageInHTML = " Stay at home "
break_line = " </br> "
p_begin = "<p>"
p_end = "</p>"

#number of times phrase will appear
cicle_times = 10000
compare_number = 100

class IndexView(TemplateView):
	"""
	Index view of webserver
	"""

	template_name = "randomText/index.html"

	
	def get(self,request,*args,**kwargs):
		"""
		Method to add new context data, this will
		put the phrase in variable messageInHTML
		random times before to put a break line
		"""
		context = self.get_context_data(**kwargs)
		context["message_title"] = messageInHTML

		message_output = ""
		new_message = ""
		is_end = False
		for time in range(0,cicle_times):
			is_end = False
			new_message = new_message + messageInHTML

			#Generate a pseudo-random integer and looking 
			#this number be divisible by a number (compare_number),
			#in case of yes, this will add a break line in html
			if randint(0,cicle_times) % compare_number == 0:
				message_output = message_output + p_begin + new_message + p_end + break_line
				new_message = ""
				is_end = True
				
		if not is_end:
			message_output = message_output + p_begin + new_message + p_end + break_line

		context["message"] = message_output 
		return self.render_to_response(context)

