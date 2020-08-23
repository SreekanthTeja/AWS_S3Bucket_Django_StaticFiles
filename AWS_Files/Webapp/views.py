from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
def home(request):
    if request.method=='POST':
        myfile=request.FILES['myfile']
        print(myfile.name)
        print(myfile.size)
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        return render(request,'home.html',{'uploaded_file_url':uploaded_file_url})
    return render(request,'home.html')




#     