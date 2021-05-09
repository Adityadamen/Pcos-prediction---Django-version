from django.shortcuts import render ,redirect, get_object_or_404, HttpResponse
import pickle
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

def predict(request):
    return render(request, 'index.html')

def practice(request):
    return render(request, 'practice.html')



def result(request):
    if request.method == 'POST':
        l = []
        x = int(request.POST['Age (yrs)'])
        y = float(request.POST['BMI'])
        Cycle = int(request.POST['Cycle (R/I)'])
        gr = int(request.POST['Weight Gain (Y/N)'])
        hwh = int(request.POST['Hair Growth (Y/N)'])
        mr = int(request.POST['Skin Darkening (Y/N)'])
        ac = int(request.POST['Hair Loss (Y/N)'])
        pa = int(request.POST['Pimples (Y/N)'])
        a = int(request.POST['Fast food (Y/N)'])
        p = int(request.POST['Regular Exercise (Y/N)'])

        data = [x,y,Cycle, gr, hwh,mr, ac, pa,a,p]
        pickle_in = open('model.pkl', 'rb')

        model = pickle.load(pickle_in)
        res = model.predict([data])
        if res == [1]:
            test = "Yes"
        else:
            test = "No"
        return render(request, 'practice.html',{"r":test})




# Create your views here.
