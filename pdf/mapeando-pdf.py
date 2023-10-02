import fitz  # Importa a biblioteca PyMuPDF

# Abre o arquivo PDF
pdf = fitz.open('v1topo_branco.pdf')

# Itera sobre as páginas
for pagina_num in range(pdf.page_count):
    pagina = pdf.load_page(pagina_num)
    
    # Obtém a lista de blocos de texto
    blocos = pagina.get_text('blocks')
    
    # Itera sobre os blocos de texto
    for bloco in blocos:
        for linha in bloco: # Cada bloco pode conter várias linhas de texto
            caixa, texto, _, _ = linha  # Extrai as informações relevantes
            
            # Imprime as informações do bloco
            print(f'Texto: "{texto.strip()}"')
            print(f'Bounding Box: {caixa}')
            print('\n')

# Fecha o arquivo PDF
pdf.close()
