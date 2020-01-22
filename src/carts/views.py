from django.shortcuts import render



def cart_home(request):
	# print (request.session) # on the request
	# print(dir(request.session))
	# request.session.set_expiry(300) # 5 minutes
	# key = request.session.session_key
	# print(key)
	request.session['first_name'] = "Justin"
	return render(request, "carts/home.html", {})
	
