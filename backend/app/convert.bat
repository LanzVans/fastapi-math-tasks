@echo off
setlocal

if not exist output mkdir output

if "%~1"=="" (
  echo Uzycie: build.bat plik.py
  exit /b 1
)

set FILE=%~n1

REM === Makra stylu (uzyj przekierowania > zamiast -o, bo bywa pewniejsze na Windows) ===
pygmentize -f latex -S monokai >output\style.tex

REM === Kod z Pythona jako fragment LaTeX ===
pygmentize -f latex -o output\code.tex "%~1"

pushd output

REM === Zbuduj dokument ===
(
echo \documentclass{article}
echo \usepackage{fancyvrb}
echo \usepackage{color}
echo \usepackage{xcolor}
echo \pagecolor{gray!20!black}
echo \input{style.tex}
echo \begin{document}
echo \input{code.tex}
echo \end{document}
) >"%FILE%.tex"


pdflatex "%FILE%.tex"

REM === Sprzątanie ===
del /q style.tex
del /q code.tex
del /q %FILE%.aux
del /q %FILE%.log
del /q %FILE%.tex

endlocal
