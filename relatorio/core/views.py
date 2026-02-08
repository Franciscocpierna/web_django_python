# import io
# from django.http import FileResponse
# from django.views.generic import View
# from xhtml2pdf import pisa 

# from reportlab.pdfgen import canvas

# # #####

# from django.core.files.storage import FileSystemStorage
# from django.template.loader import render_to_string
# from django.http import HttpResponse

# from weasyprint import HTML


# class IndexView(View):

#     def get(self, request, *args, **kwargs):

#         # Cria um arquivo para receber os dados e gerar o PDF
#         buffer = io.BytesIO()

#         # Criar o arquivo pdf
#         pdf = canvas.Canvas(buffer)

#         # Insere 'coisas' no PDF
#         pdf.drawString(100, 100, "Geek University")

#         # Quando acabamos de inserir coisas no PDF
#         pdf.showPage()
#         pdf.save()

#         # Por fim, retornamos o buffer para o início do arquivo
#         buffer.seek(0)

#         # Faz o download do arquivo em PDF gerado
#         # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

#         # Abre o PDF direto no navegador
#         return FileResponse(buffer, filename='relatorio1.pdf')


# class Index2View(View):

#     def get(self, request, *args, **kwargs):
#         texto = ['Geek University', 'Evolua seu lado geek', 'Programação Web com Python e Django']

#         html_string = render_to_string('relatorio.html', {'texto': texto})

#         html = HTML(string=html_string)
#         html.write_pdf(target='/tmp/relatorio2.pdf')

#         fs = FileSystemStorage('/tmp')

#         with fs.open('relatorio2.pdf') as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             # Faz o download do arquivo PDF
#             # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'

#             # Abre o PDF direto no navegador
#             response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
#         return response

import io
from django.http import FileResponse, HttpResponse
from django.views.generic import View
from django.template.loader import render_to_string
from xhtml2pdf import pisa 
from reportlab.pdfgen import canvas

# --- INSTRUÇÕES ---
# 1. Instale as dependências: pip install reportlab xhtml2pdf
# 2. Remova 'weasyprint' do seu arquivo views.py para evitar erros de inicialização.
# ------------------

class IndexView(View):
    """
    Gera um PDF desenhando manualmente com a biblioteca ReportLab.
    """
    def get(self, request, *args, **kwargs):
        # Cria um buffer na memória RAM (não precisa de gravar ficheiros no disco)
        buffer = io.BytesIO()

        # Cria o objeto canvas para desenhar o PDF no buffer
        pdf = canvas.Canvas(buffer)

        # Insere texto numa posição específica (x, y)
        pdf.drawString(100, 100, "Geek University - Relatório Manual (ReportLab)")

        # Finaliza a página e guarda o conteúdo
        pdf.showPage()
        pdf.save()

        # Reposiciona o ponteiro para o início do buffer para leitura
        buffer.seek(0)

        # Retorna o ficheiro para visualização no navegador
        return FileResponse(buffer, filename='relatorio_reportlab.pdf')


class Index2View(View):
    """
    mudança por IA gemini
    Gera um PDF a partir de um template HTML usando xhtml2pdf.
    Substitui o WeasyPrint e funciona corretamente no Windows.
    """
    def get(self, request, *args, **kwargs):
        # Dados de exemplo enviados para o template
        texto = [
            'Geek University', 
            'Evolua seu lado geek', 
            'Programação Web com Python e Django'
        ]

        # 1. Renderiza o template 'relatorio.html' para uma string de texto
        # O Django procura este ficheiro na sua pasta de templates configurada
        html_string = render_to_string('relatorio.html', {'texto': texto})

        # 2. Cria o buffer de memória (evita erros de caminho /tmp/ no Windows)
        buffer = io.BytesIO()

        # 3. Converte o HTML em PDF usando o motor pisa (xhtml2pdf)
        # Codificamos em UTF-8 para garantir a compatibilidade com acentos
        pisa_status = pisa.pisaDocument(
            io.BytesIO(html_string.encode("UTF-8")), 
            dest=buffer
        )

        # 4. Verifica se ocorreu algum erro durante a geração do documento
        if pisa_status.err:
            return HttpResponse('Erro ao gerar PDF: Verifique a sintaxe do template HTML.', status=500)

        # 5. Prepara o buffer para ser enviado na resposta
        buffer.seek(0)

        # 6. Retorna o PDF gerado diretamente para o navegador
        return FileResponse(buffer, filename='relatorio_html.pdf')