from django.shortcuts import render
from django.http import HttpResponse
import pickle


# Create your views here.
def index(request):
    loaded_model = pickle.load(open('final_ml_model.sav', 'rb'))
    context = {}
    if request.method == "POST":
        try:
            pass
        except:
            details = []
            mean_radius = float(request.POST['meanradius'])
            mean_texture = float(request.GET['meantexture'])
            mean_perimeter = float(request.GET['meanperimeter'])
            mean_area = float(request.GET['meanarea'])
            mean_smoothness = float(request.GET['meansmoothness'])
            details.append(mean_radius)
            details.append(mean_texture)
            details.append(mean_perimeter)
            details.append(mean_area)
            details.append(mean_smoothness)
            print("Pranjal")
            print(details)
            # context['ans'] = lr.predict([details])
            context['ans'] = loaded_model.predict([details])
            print(context['ans'])
            #context['success'] = "You are predicted to have Breast Cancer"
        # Printing error message
        # else:
            # context['error'] = "You do not have Breast Cancer"

    return render(request, "index.html", context)
