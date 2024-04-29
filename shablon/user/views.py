import os
from io import BytesIO

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Report
from docxtpl import DocxTemplate

class GenerateReportView(View):

    template_name = 'user/report.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        fio = self.request.user.username
        context = {'fio': fio}
        tpl = DocxTemplate("C://Users//79828//Desktop//docShablon//shablon//user//doc_shablone//fio.docx")
        tpl.render(context)
        output = BytesIO()
        tpl.save(output)
        output.seek(0)
        response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="generated_report.docx"'

        return response
