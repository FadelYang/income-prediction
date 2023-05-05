from django.shortcuts import render

# the home page
def home(request):
    return render(request, 'index.html')

# custom method for generating predicitons
def getPredictions(umur, kelas_pekerjaan, tingkat_pendidikan, pekerjaan, relationship, jam_kerja_per_minggu):
    import pickle, numpy
    model = pickle.load(open("income_prediction_app\income_prediction_ml_model.sav", "rb"))
    scaled = pickle.load(open("income_prediction_app\scaler.sav", "rb"))
    prediciton = model.predict(scaled.transform([[
        umur, kelas_pekerjaan, tingkat_pendidikan, pekerjaan, relationship, jam_kerja_per_minggu
        ]]))

    prediction_output = numpy.array_str(prediciton)

    if prediction_output == "['<=50K']":
        return 'Your income is <-50K'
    elif prediction_output == "['>50K']":
        return 'Your income is >50K'
    else:
        return 'something error'

# result page view
def result(request):
    umur = int(request.GET['umur'])
    kelas_pekerjaan = int(request.GET['kelas_pekerjaan'])
    tingkat_pendidikan = int(request.GET['tingkat_pendidikan'])
    pekerjaan = int(request.GET['pekerjaan'])
    relationship = int(request.GET['relationship'])
    jam_kerja_per_minggu = int(request.GET['jam_kerja_per_minggu'])

    result = getPredictions(umur, kelas_pekerjaan, tingkat_pendidikan, pekerjaan, relationship, jam_kerja_per_minggu)

    return render(request, 'index.html', {'result':result})
