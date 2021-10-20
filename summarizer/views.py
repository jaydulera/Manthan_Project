from django.shortcuts import render
from django.http import HttpResponse
from . import my_code
def home(request):
    # return HttpResponse('<h1>Sommaire Home</h1>')
    return render(request,'summarizer/home3.html')

def about(request):
    # return HttpResponse('<h1>Sommaire About Page</h1>')
    return render(request,'summarizer/about.html')

# def output(request):
#     if request.is_ajax():
#         py_obj = my_code.test_code(10)
#         return render(request, 'summarizer/output.html', {'output': py_obj})

# Create your views here.
def output(request):
    if request.method == 'GET':
        txtInput = request.GET.get('txtInput')
        # inputVal = request.POST['inputVal']
        # from simplet5 import SimpleT5
        # model = SimpleT5()
        # # model.from_pretrained(model_type="t5", model_name="t5-base")
        # model.load_model("t5","/content/mydrive/MyDrive/Summarization/outputs/simplet5-epoch-2-train-loss-1.4634")
        # summaryContent = model.predict(inputVal)
        context = {'summaryContent' : txtInput, 'originalText' : txtInput}
        summaryContent = txtInput
        return render(request,'summarizer/home3.html',context)