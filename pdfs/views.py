from django.shortcuts import render
from django.shortcuts import render
from .forms import UploadPDFForm
from .models import PDF
from django.http import HttpResponse

# class UploadPDFFormView(FormView):
#     form_class = UploadPDFForm
#     template_name = 'upload.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 file_instance = File(file=f)
#                 file_instance.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


def home(request):
    return HttpResponse("Hello, Django!")


def upload_pdf(request):
    if request.method == 'POST' :
        form = UploadPDFForm(request.POST, request.FILES)
        uploaded_pdfs = request.FILES.getlist('files')
        for f in uploaded_pdfs:
            print("File: ", f)
            file_instance = PDF(files=f)
            file_instance.save()
    else:
        form = UploadPDFForm()
    return render(request, 'upload.html', {'form': form})
