from django.shortcuts import render

from .forms import UserForm

def create(request):

  #if request.method == 'GET':
    form = UserForm()

    context = {
      'form': form,
    }
    form = UserForm(request.POST)
    if form.is_valid():
      a = form.cleaned_data['a']
      b = form.cleaned_data['b']
      c = form.cleaned_data['c']
      delta = (b ** 2) + (- 4 * a * c)
      print(delta)
      raiz1 = (-b + delta**0.5) / (2 * a)
      raiz2 = (-b - delta**0.5) / (2 * a) 
      context = {
        'form': form,
        'raiz1': raiz1,
        'raiz2': raiz2,
      }
      print(raiz1)
    return render(request, 'User/index.html', context=context)


  #else:
  #  form = UserForm(request.POST)
  #  if form.is_valid():
  #    context = {
  #      'a': form.cleaned_data['a'],
  #      'b': form.cleaned_data['b'],
  #      'c': form.cleaned_data['c'],
  #    }
  #  return render(request, 'User/index.html', context=context)
#  elif request.method == 'POST':
 #   return render(request, 'User/criar.html')
