from django.shortcuts import render,redirect


def home(request):
    return render(request,'home.html')

def list(request):
    alunos = Aluno.objects.all()
    return render(request, 'tt/list.html',{'alunos':alunos})