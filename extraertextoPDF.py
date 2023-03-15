# Importamos PdfReader de la librería PyPDF2
from PyPDF2 import PdfReader

reader = PdfReader("archivo1.pdf") # indicamos el nombre del archivo PDF
page = reader.pages[0] # indicamos la posición de la página de la que extraeremos el texto

print(page.extract_text()) # Usamos la funcion extract_text() para obtener los datos
