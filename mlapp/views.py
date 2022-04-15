from django.shortcuts import render
from django.http import HttpResponse
import pickle


# Create your views here.
def index(request):
    loaded_model = pickle.load(open('final_ml_model.sav', 'rb'))
    context = {}
    if request.method == "POST":
            details = []
            mean_radius = float(request.POST['meanradius'])
            mean_texture = float(request.POST['meantexture'])
            mean_perimeter = float(request.POST['meanperimeter'])
            mean_area = float(request.POST['meanarea'])
            mean_smoothness = float(request.POST['meansmootheness'])
            mean_compactness = float(request.POST['meancompactness'])
            mean_concavepoints = float(request.POST['meanconcavepoints'])
            mean_concavity = float(request.POST['meanconcavity'])
            mean_symmetry = float(request.POST['meansymmetry'])
            mean_fractaldim = float(request.POST['meanfractaldim'])
            radius_error = float(request.POST['radiuserror'])
            texture_error = float(request.POST['textureerror'])
            perimeter_error = float(request.POST['perimetererror'])
            area_error = float(request.POST['areaerror'])
            smoothness_error = float(request.POST['smoothnesserror'])
            compactness_error = float(request.POST['compactnesserror'])
            concavity_error = float(request.POST['concavityerror'])
            concavepoint_error = float(request.POST['concavepointerror'])
            symmetry_error = float(request.POST['symmetryerror'])
            fractal_dimerror = float(request.POST['fractaldimerror'])
            worst_radius = float(request.POST['worstreadius'])
            worst_texture = float(request.POST['worsttexture'])
            worst_perimeter = float(request.POST['worstperimeter'])
            worst_area = float(request.POST['worstarea'])
            worst_smoothness = float(request.POST['worstsmoothness'])
            worst_compactness = float(request.POST['worstcompactness'])
            worst_concavity = float(request.POST['worstconcavity'])
            worst_concavepoints = float(request.POST['worstconcavepoints'])
            worst_symmetry = float(request.POST['worstsymmetry'])
            worst_fractaldim = float(request.POST['worstfractaldim'])

            details.append(mean_radius)
            details.append(mean_texture)
            details.append(mean_perimeter)
            details.append(mean_area)
            details.append(mean_smoothness)
            details.append(mean_compactness)
            details.append(mean_concavepoints)
            details.append(mean_concavity)
            details.append(mean_symmetry)
            details.append(mean_fractaldim)
            details.append(radius_error)
            details.append(texture_error)
            details.append(perimeter_error)
            details.append(area_error)
            details.append(smoothness_error)
            details.append(compactness_error)
            details.append(concavity_error)
            details.append(concavepoint_error)
            details.append(symmetry_error)
            details.append(fractal_dimerror)
            details.append(worst_radius)
            details.append(worst_texture)
            details.append(worst_perimeter)
            details.append(worst_area)
            details.append(worst_smoothness)
            details.append(worst_compactness)
            details.append(worst_concavity)
            details.append(worst_concavepoints)
            details.append(worst_symmetry)
            details.append(worst_fractaldim)

            print(details)
            context['ans'] = loaded_model.predict([details])
            print(context['ans'])
            if context['ans'] == 1:
                context['value'] = 'You are diagnosed with BREAST CANCER'
            else:
                context['value'] = 'You are not diagnosed with BREAST CANCER'
        # Printing error message
        # else:
            # context['error'] = "You do not have Breast Cancer"

    return render(request, "index.html", context)
