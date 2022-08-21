from django.shortcuts import render
from .models import Exam

#Create your views here.

def score(request):
   
    if request.method == 'POST':
        #print(request.POST)
        questions=Exam.objects.all()
        result=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            # print(q.corrans)
            # print()
            if q.corrans ==  request.POST.get(q.question):
                result+=10
                correct+=1
            else:
                wrong+=1
        context = {
            'result' : result,
            'correct' : correct,
            'wrong' : wrong,
            'total' : total,
        }
        return render(request,'score.html',context)
    else:
        questions=Exam.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)
 
