from django.shortcuts import render
from django.utils.crypto import get_random_string



counter=0
def index(request):
    randomString=get_random_string(length=14)
    context={
        'random': randomString
    }
    
    if request.session['counter']==0:
        request.session['counter']=1
    else:
        request.session['counter']+=1
    return render(request,'myapp/index.html', context)
    

# def ('/count', methods=['POST'])
# def count():
#     if request.form['booten'] == '+2':
#         session['count'] +=1
#     elif request.form['booten'] == 'reset':
#         session['count'] = 0

#     return redirect("/")








# @app.route('/count', methods=['POST'])
# def count():
#     if request.form['booten'] == '+2':
#         session['count'] +=1
#     elif request.form['booten'] == 'reset':
#         session['count'] = 0

#     return redirect("/")
