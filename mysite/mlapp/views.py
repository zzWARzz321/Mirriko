from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ModelForm, ModelForm1
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nasos_one = form.cleaned_data['nasos_one']
            nasos_two = form.cleaned_data['nasos_two']
            nasos_three = form.cleaned_data['nasos_three']
            nasos_four = form.cleaned_data['nasos_four']
            dry_ptp = form.cleaned_data['dry_ptp']
            liquid_ptp = form.cleaned_data['liquid_ptp']

            # give prediction response
            model_features = [
                [nasos_one, nasos_two, nasos_three, nasos_four, dry_ptp, liquid_ptp]]
            loaded_model = pickle.load(
                open("C:/Users/bogda/OneDrive/Документы/oilmir/obavar.pkl", 'rb'))
            prediction = loaded_model.predict(model_features)

            all_pomp = [nasos_one, nasos_two, nasos_three, nasos_four]

            if all(v == 0 for v in all_pomp) == True:
                return render(request, 'home.html', {'form': form, 'prediction1': 'Нет данных',
                                                     'prediction2': 'Нет данных'})
            elif dry_ptp == 0 and liquid_ptp == 0:
                return render(request, 'home.html', {'form': form, 'prediction1': 'Нет данных',
                                                     'prediction2': 'Нет данных'})
            else:
                #prediction = "MyPrediction"
                return render(request, 'home.html', {'form': form, 'prediction1': round(prediction[0][0],2),
                                                     'prediction2': round(prediction[0][1],2)})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'home.html', {'form': form})

def predict_model1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm1(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nasos_one = form.cleaned_data['nasos_one']
            nasos_two = form.cleaned_data['nasos_two']
            nasos_three = form.cleaned_data['nasos_three']
            nasos_four = form.cleaned_data['nasos_four']
            tonn = form.cleaned_data['tonn']
            press = form.cleaned_data['press']

            # give prediction response
            model_features = [
                [nasos_one, nasos_two, nasos_three, nasos_four, tonn, press]]
            loaded_model = pickle.load(
                open("C:/Users/bogda/OneDrive/Документы/oilmir/inverse.pkl", 'rb'))
            prediction = loaded_model.predict(model_features)

            all_pomp = [nasos_one, nasos_two, nasos_three, nasos_four]

            if all(v == 0 for v in all_pomp) == True:
                return render(request, 'home.html', {'form': form, 'prediction1': 'Нет данных',
                                                     'prediction2': 'Нет данных'})
            else:
                #prediction = "MyPrediction"
                return render(request, 'home1.html', {'form': form, 'prediction1': round(prediction[0][0],2),
                                                     'prediction2': round(prediction[0][1],2)})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm1()

    return render(request, 'home1.html', {'form': form})
