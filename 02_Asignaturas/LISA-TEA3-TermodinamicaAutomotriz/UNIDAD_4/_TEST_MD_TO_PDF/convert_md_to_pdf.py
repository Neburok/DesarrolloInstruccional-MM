import pypandoc
from pylatex import Document, Section, NoEscape, Package
import os

def create_pdf_from_markdown(markdown_filepath, output_filename):
    

    # 1. Convertir Markdown a LaTeX usando pypandoc (generar solo el cuerpo)
    try:
        latex_content = pypandoc.convert_file(
            markdown_filepath,
            'latex',
            format='md'
        )
    except Exception as e:
        print(f"Error al convertir Markdown a LaTeX con Pandoc: {e}")
        return

    # 2. Crear un documento PyLaTeX y añadir el contenido LaTeX modificado
    # Definir la clase de documento y añadir la plantilla utpdoc.sty
    doc = Document(documentclass='article') # O la clase de documento que use utpdoc.sty
    doc.packages.append(Package('utpdoc'))
    doc.packages.append(Package('tikz')) # Asegurar que tikz se cargue
    doc.preamble.append(NoEscape('\graphicspath{{./}}')) # Indicar a LaTeX que busque imágenes en el directorio actual

    # Añadir el contenido LaTeX generado por Pandoc
    doc.append(NoEscape(latex_content))

    # 3. Compilar el LaTeX a PDF
    try:
        # generate_pdf compila el .tex y crea el PDF
        # clean_tex=False para mantener los archivos .tex, .aux, .log para depuración
        doc.generate_pdf(output_filename, clean_tex=False)
        print(f"Successfully created {output_filename}.pdf")
    except Exception as e:
        print(f"Error durante la generación del PDF: {e}")
        print("Asegúrese de tener una distribución LaTeX (como MiKTeX o TeX Live) instalada y en su PATH.")
        print(f"Se guardó el archivo intermedio '{output_filename}.tex' para depuración.")
        # Si falla la compilación, al menos guardamos el .tex para revisar
        doc.generate_tex(output_filename)

if __name__ == '__main__':
    # Rutas relativas al directorio de trabajo actual (donde se ejecuta el script)
    # Asegurarse de que el script se ejecute desde el directorio _TEST_MD_TO_PDF
    md_file = 'AD.04.03.01_Test_MD_Conversion.md'
    output_name = 'AD.04.03.01_Test_MD_Conversion' # Sin extensión .pdf

    # Llamar a la función de conversión
    create_pdf_from_markdown(md_file, output_name)
