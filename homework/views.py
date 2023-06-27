from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .Optimal import optimal
from .allSolutions_Final import findall

from .form import TextFileForm
from .optimal_final import run
global file_name,file_name_links
def upload_text_file(request):
    global file_name
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['text_file']
            file_contents = uploaded_file.read()
            file_name = uploaded_file.name
            print(file_name)
            
            with open('homework/'+file_name, 'wb') as destination_file:
                for chunk in uploaded_file.chunks():
                    destination_file.write(chunk)
         
            # Do something with file_contents
            return render(request, 'file_upload_success.html')
    else:
        form = TextFileForm()
    return render(request, 'upload_text_file.html', {'form': form})
def upload_text_file1(request):
    print(request.method)
    if request.method == 'POST':
        print("Aaa")
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        filename=file1.name
        filename2=file2.name
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        print(name2)
        with open(filename, 'wb') as destination_file:
                for chunk in file1.chunks():
                    destination_file.write(chunk)
        with open(filename2, 'wb') as destination_file:
                for chunk in file2.chunks():
                    destination_file.write(chunk)
         
            # Do something with file_contents
       # return render(request, 'file_upload_success.html')
        action = request.POST.get('action')
        print(action)
        if action == 'optimal':
          run(int(name1),int(name2),filename,filename2)
          with open('Optimal.txt', 'r') as source:
                  contents = source.read()

    # Create HttpResponse object with the appropriate MIME type.
          response = HttpResponse(content_type='text/plain')
    
    # Set the Content-Disposition response header to open the file.
          response['Content-Disposition'] = 'attachment; filename="Optimal.txt"'
    
    # Write the data to the response.
          response.write(contents)
        
          return response

        if action == 'allsol':
          findall(int(name1),int(name2),filename,filename2)
          with open('allsol.txt', 'r') as source:
                  contents = source.read()

    # Create HttpResponse object with the appropriate MIME type.
          response = HttpResponse(content_type='text/plain')
    
    # Set the Content-Disposition response header to open the file.
          response['Content-Disposition'] = 'attachment; filename="allsol.txt"'
    
    # Write the data to the response.
          response.write(contents)
        
          return response
    else:
        form = TextFileForm()
    return render(request, 'upload_text_file.html', {'form': form})
def upload_text_allsol(request):
    global file_name_links
    if request.method == 'POST':
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        filename=file1.name
        filename2=file2.name
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        print(name2)
        with open(filename, 'wb') as destination_file:
                for chunk in file1.chunks():
                    destination_file.write(chunk)
        with open(filename2, 'wb') as destination_file:
                for chunk in file2.chunks():
                    destination_file.write(chunk)
         
            # Do something with file_contents
       # return render(request, 'file_upload_success.html')
        findall(int(name1),int(name2),filename,filename2)
        with open('allsol.txt', 'r') as source:
                contents = source.read()

    # Create HttpResponse object with the appropriate MIME type.
        response = HttpResponse(content_type='text/plain')
    
    # Set the Content-Disposition response header to open the file.
        response['Content-Disposition'] = 'attachment; filename="allsol.txt"'
    
    # Write the data to the response.
        response.write(contents)
        
        return response
    else:
        form = TextFileForm()
    return render(request, 'upload_text_file.html', {'form': form})
def generate_txt(request):
    global file_name,file_name_links
    # Create text data
    print( request.POST)
    num1 = request.POST['start']
    num2 = request.POST['end']
    print(num1)
    text = "This is some text data."
    run(file_name,file_name_links)
    # Create HttpResponse object with the appropriate MIME type.
    response = HttpResponse(content_type='text/plain')
    
    # Set the Content-Disposition response header to open the file.
    response['Content-Disposition'] = 'attachment; filename="text.txt"'
    
    # Write the data to the response.
    response.write(text)
    return response

def index(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())
def addition(request):

    print( request.POST)
    num1 = request.POST['start']
    num2 = request.POST['end']
    print(num1)
    
    
    return render(request, "result.html", {"result":aa})
  
