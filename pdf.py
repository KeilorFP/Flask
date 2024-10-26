from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_pdf():
    c = canvas.Canvas("implementacion.pdf", pagesize=letter)
    c.drawString(100, 750, "Nombre: Implementacion del modelo Iris")
    c.drawString(100, 730, "Código de lote: 001")
    c.drawString(100, 710, f"Fecha de envío: {datetime.now().strftime('%d/%m/%Y')}")
    c.drawString(100, 690, "Enviado a: Repositorio de GitHub")

    
    x = 100  
    width = 400 
    height = 200  
    y_positions = [500, 280, 60]  

   
    c.drawImage("modelo.png", x, y_positions[0], width, height)
    c.drawImage("main.png", x, y_positions[1], width, height)
    c.drawImage("pdf.png", x, y_positions[2], width, height)

  
    c.save()

create_pdf()