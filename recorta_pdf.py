import fitz  # PyMuPDF
from PIL import Image
import io

pdf_path = "pdf_files/mnt/achao/Downloads/ccpdf_zip/4000-4999/4027/4027862.pdf"
page_number = 74 # começa em 0 no PyMuPDF
coords = (0.11, 0.23, 0.87, 0.75)

# Abre o PDF e seleciona a página
doc = fitz.open(pdf_path)
page = doc[page_number - 1]

# Dimensões da página
width, height = page.rect.width, page.rect.height

# Converte coordenadas normalizadas em pontos
x0, y0, x1, y1 = [coords[0]*width, coords[1]*height, coords[2]*width, coords[3]*height]
rect = fitz.Rect(x0, y0, x1, y1)

# Renderiza só a área selecionada
pix = page.get_pixmap(clip=rect, dpi=150)  # aumenta o dpi se quiser mais qualidade

# Converte o pixmap em imagem Pillow (sem salvar)
img = Image.open(io.BytesIO(pix.tobytes("png")))

# Exibe a imagem diretamente
img.show()
