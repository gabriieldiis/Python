import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Abre o PDF original para leitura
with open('Topo_branco.pdf', 'rb') as leitor_teste:
    leitor = PyPDF2.PdfReader(leitor_teste)
    primeira_pagina = leitor.pages[0]
    texto_original = primeira_pagina.extract_text()

# Cria um novo PDF com a biblioteca reportlab
c = canvas.Canvas("novo_arquivo.pdf", pagesize=letter)
c.setFont("Helvetica", 12)

# Define o novo texto
novo_texto = "Novos dados para o PDF\nLinha 2\nLinha 3"

# Desenha o texto no PDF
c.drawString(100, 600, novo_texto)

# Fecha o arquivo PDF
c.save()
