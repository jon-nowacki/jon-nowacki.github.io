generates latex files into dvi then svg
apt get install latex dvisvgm

latex file.tex
dvisvgm --no-fonts file.dvi file.svg

```latex

\documentclass[paper=a5,fontsize=12pt]{scrbook}
\usepackage[pdftex,active,tightpage]{preview}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{tikz}
\begin{document}
\begin{preview}
\begin{tikzpicture}[inner sep=0pt, outer sep=0pt]
\node at (0, 0) {texCode}; % <--Put your tex-code here
\end{tikzpicture}
\end{preview}
\end{document}

```