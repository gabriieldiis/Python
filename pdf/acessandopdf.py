import PyPDF2

with open('Topo_branco.pdf', 'rb') as leitor_teste:
    leitor = PyPDF2.PdfReader(leitor_teste)

    for pagina_num in range(len(leitor.pages)):
        pagina = leitor.pages[pagina_num]
        texto = pagina.extract_text()
        print(texto)
