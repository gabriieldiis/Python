from reportlab.pdfgen import canvas

# Define os novos dados
novo_nome_produto = "Novo Produto"
novo_preco_antigo = "R$ 219,00"
novo_preco_atual = "R$ 1499,90"
novo_sku = "123456"
novo_codigo_barras = "123456789012"

# Cria um novo PDF com a biblioteca reportlab
c = canvas.Canvas("novo_arquivo.pdf")

# Define a fonte e o tamanho do texto
c.setFont("Helvetica", 12)

# Adiciona os novos dados no PDF
c.drawString(100, 700, novo_nome_produto)
c.drawString(100, 680, f"De {novo_preco_antigo} por")
c.drawString(100, 660, novo_preco_atual)
c.drawString(100, 640, f"SKU {novo_sku}")

# Adiciona um QR code (se você tiver uma imagem do QR code, pode inseri-la em vez de desenhá-la)
# from reportlab.graphics import barcode
# qr_code = barcode.createBarcodeDrawing('qrcode', value=novo_qrcode, width=150, height=150)
# qr_code.drawOn(c, 100, 580)

# Adiciona um código de barras (da mesma forma que o QR code)
# barcode = barcode.createBarcodeDrawing('code128', value=novo_codigo_barras, width=250, height=50)
# barcode.drawOn(c, 100, 500)

# Fecha o arquivo PDF
c.save()
