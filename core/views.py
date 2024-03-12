from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import pickle
import sklearn
import numpy as np
from django.urls import reverse

from .forms import *
from .models import Wine

# def login(request):
#     return render(request, 'login.html')

# Create your views here.
global check, username_global
check = 0


def register(request):
    return render(request, 'login/register.html')


def registerDB(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    people = request.POST.get('people')
    user = User()
    print(username)
    print(password)
    if username is '':
        msg = 'DO NOT USE EMPTY Username!'
        return render(request, 'login/register.html', {'msg': msg})
    elif password is '':
        msg = 'DO NOT USE EMPTY Password!'
        return render(request, 'login/register.html', {'msg': msg})
    else:
        global check
        check = 0
        user.username = username
        user.password = password
        user.people = people
        user.save()
        return render(request, 'login/register_success.html', {'username': username})


def login(request):
    if check == 0:
        return render(request, 'login/login.html')
    else:
        return render(request, 'login/login_success.html')


def know_more(request):
    return render(request, 'home.html')


def logout(request):
    global check
    if check == 1:
        check = 0
        msg = 'You have successfully Logged Out! '
        return render(request, 'login/login.html', {'msg': msg})
    else:
        msg = 'You are NOT Logged In'
        return render(request, 'login/login.html', {'msg': msg})


def login_check(request):
    username1 = request.POST.get('username')
    password1 = request.POST.get('password')
    people = request.POST.get('people')
    print(username1)
    global username_global
    username_global = username1

    try:
        user = User.objects.get(username=username1)
        password2 = user.password
    except Exception as e:
        msg = "Please input CORRECT information!"
        return render(request, 'login/login.html', {'msg': msg})

    if password1 == password2:
        global check
        check = 1
        # return render(request, 'predict.html')
        return render(request, 'login/login_success.html', {'username': username_global})
    else:
        msg = "Please input CORRECT information!"
        return render(request, 'login/login.html', {'msg': msg})


def databases(request):
    if check == 0:
        msg = 'Please LOGIN before you access the databases'
        return render(request, 'login/login.html', {'msg': msg})
    user = User.objects.get(username=username_global)
    if user.people == 1:
        db = Wine.objects.all()
        return render(request, 'databases.html', {"data": db})
    else:
        return render(request, 'error.html', {'username': username_global})


def index(request):
    return render(request, 'index.html')


def WinePredict(request):
    if check == 0:
        msg = 'Please LOGIN before you predict!'
        return render(request, 'login/login.html', {'msg': msg})
    if request.method == "POST":
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cp = request.POST.get('cp')
        rbp = request.POST.get('rbp')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        rest = request.POST.get('rest')
        mhr = request.POST.get('mhr')
        eia = request.POST.get('eia')
        st = request.POST.get('st')
        slope = request.POST.get('slope')

        major = request.POST.get('major')
        thala = request.POST.get('thala')

        # save to database

        try:

            with open('ml_models/model.obj', "rb") as f:
                model = pickle.load(f)

            with open('ml_models/lr.obj', "rb") as g:
                lr = pickle.load(g)

            with open('ml_models/dt.obj', "rb") as h:
                dt = pickle.load(h)

            with open('ml_models/rf.obj', "rb") as j:
                rf = pickle.load(j)

            with open('ml_models/svc.obj', "rb") as k:
                svc = pickle.load(k)

            with open('ml_models/knn.obj', "rb") as l:
                knn = pickle.load(l)

            with open('ml_models/gb.obj', "rb") as t:
                gb = pickle.load(t)

                print(int(age), int(gender), int(cp), float(rbp), float(chol), int(fbs), int(
                    rest), float(mhr), int(eia), float(st), int(slope), int(major), int(thala))

                x = np.array([int(age), int(gender), int(cp), float(rbp), float(chol), int(fbs), int(
                    rest), float(mhr), float(eia), float(st), float(slope), float(major), int(thala)])

                # x = np.array([58,1,2,132.0,224.0,0,2,173.0,0,3.2,0,2.0,7])
                x = x.reshape(1, -1)

                # x = sc.fit_transform(x)
                print(x)
                output_model = model.predict(x)
                output_lr = lr.predict(x)
                output_dt = dt.predict(x)
                output_rf = rf.predict(x)
                output_svc = svc.predict(x)
                output_knn = knn.predict(x)
                output_gb = gb.predict(x)

                print(output_model)
                print(output_lr)
                print(output_dt)
                print(output_rf)
                print(output_svc)
                print(output_knn)
                print(output_gb)


        except Exception as e:
            print(e)
            print("something went wrong")

        wine = Wine()
        wine.username = username_global
        print(wine.username)
        wine.age = age
        wine.sex = gender
        wine.cp = cp
        wine.trestbps = rbp
        wine.chol = chol
        wine.fbs = fbs
        wine.restecg = rest
        wine.thalach = mhr
        wine.exang = eia
        wine.oldpeak = st
        wine.slope = slope
        wine.ca = major
        wine.thal = thala
        wine.target = output_model[0]
        wine.save()

        res = ''
        if output_model[0] == 0:
            res = 'No Disease'
            print(res)
            context = {
                'data': output_model[0],
                'q': res,
                'lr': output_lr[0],
                'rf': output_rf[0],
                'knn': output_knn[0],
                'svc': output_svc[0],
                'dt': output_dt[0],
                'gb': output_gb[0],

            }
            return render(request, 'output.html', context)
        else:
            res = 'You Have Disease'
            print(res)
            context = {
                'data': output_model[0],
                'q': res,
                'lr': output_lr[0],
                'rf': output_rf[0],
                'knn': output_knn[0],
                'svc': output_svc[0],
                'dt': output_dt[0],
                'gb': output_gb[0],
            }
            return render(request, 'output_2.html', context)

    # else:
    #     return render(request, 'login/login.html')

    return render(request, 'predict.html')


def Output(request):
    return render(request, 'output.html')


def Report(request):
    return render(request, 'report.html')


def visual(request):
    return render(request, 'age.html')


def gender(request):
    return render(request, 'gender.html')


def chest(request):
    return render(request, 'chest.html')


def blood(request):
    return render(request, 'blood.html')


def cholestoral(request):
    return render(request, 'cholestoral.html')


def fasting(request):
    return render(request, 'fasting.html')


def electrocardiographic(request):
    return render(request, 'electrocardiographic.html')


def heartRate(request):
    return render(request, 'heartRate.html')


def exercise(request):
    return render(request, 'exercise.html')


def st(request):
    return render(request, 'st.html')


def vessels(request):
    return render(request, 'vessels.html')


def thalassemia(request):
    return render(request, 'thalassemia.html')


def age(request):
    return render(request, 'age.html')


def healthy(request):
    return render(request, 'results/suggestion_healthy.html')


def unhealthy(request):
    return render(request, 'results/suggestion_unhealthy.html')


def data_proc_report(request):
    return render(request, 'data_proc_report.html')


def about(request):
    return render(request, 'about.html')


def delete(request, id):
    print(id)
    id_database = Wine.objects.get(id=id)
    id_database.delete()
    return HttpResponseRedirect(reverse('databases'))


# def page_not_found(request):
#     return render(request, '404.html', {}, status=404)
