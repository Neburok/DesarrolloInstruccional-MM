@echo off
echo Convirtiendo Markdown a Word...
cd /d "C:\Repositorios\DesarrolloInstruccional-MM\02_Asignaturas\LISA-TEA3-TermodinamicaAutomotriz\UNIDAD_4\AD"

REM Convertir Ciclo de Carnot
pandoc -s "AD.04.01.01_Lectura_Ciclo_Carnot_Eficiencia_Maxima.md" -o "AD.04.01.01_Lectura_Ciclo_Carnot_Eficiencia_Maxima.docx" --mathml --wrap=none

REM Convertir Otto y Diesel
pandoc -s "AD.04.02.01_Lectura_Comparativa_Otto_Diesel.md" -o "AD.04.02.01_Lectura_Comparativa_Otto_Diesel.docx" --mathml --wrap=none

echo Conversión completada!
echo Los archivos .docx están listos.
pause