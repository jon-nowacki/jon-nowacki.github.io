"""
Generates svg files from json file path


dictionary_structure for input params
    [{
        "name": "",
        "latex": ""
    }]
"""
from subprocess import call
import os
import shutil

script_directory = os.path.dirname(os.path.abspath(__file__))



class LatexToSvg:
    def __init__(self, input_params, output_dir ):
        self.input_params = input_params
        self.output_dir = output_dir


    def Mkdir(self):
        try:
            os.mkdir(self.output_dir)
        except:
            pass

    def Run(self):
        self.Mkdir()
        os.chdir(self.output_dir)
        for ip in self.input_params:
            file_name = ip['name']
            equation  = ip['latex']
            fpath = os.path.join(self.output_dir, file_name+'.tex')
            self.GenerateLatexTemplate(equation, fpath )

        for ip in self.input_params:
            file_name = ip['name']
            tex = os.path.join(self.output_dir, file_name+'.tex')
            dvi = os.path.join(self.output_dir, file_name+'.dvi')
            svg = os.path.join(self.output_dir, file_name+'.svg')
            self.LatexToSvgCmd(tex,dvi, svg)

    def MoveSvgFiles(self,svg_dir):
        for ip in self.input_params:
            file_name = ip['name']
            input_svg = os.path.join(self.output_dir, file_name+'.svg')
            output_svg = os.path.join(svg_dir, file_name+'.svg')
            shutil.move(input_svg, output_svg)

    def GenerateLatexTemplate( self,latex_stmt, file_output_path ):

        latex_template = self.LatexTemplate(latex_stmt)
        fout = open(file_output_path, 'w')
        fout.write(latex_template)
        fout.close()

    def LatexToSvgCmd(self, latex_file,dvi_file, svg_file_path):
        cmd = ["latex", latex_file]
        call(cmd)
        cmd =["dvisvgm", "--no-fonts", dvi_file, svg_file_path]
        call(cmd)

    def LatexTemplate(self, latex_stmt):
        pass
        if latex_stmt.strip()[0] == '$':
            latex_template = """
            \\documentclass[paper=a5,fontsize=16pt]{scrbook}
            \\usepackage[pdftex,active,tightpage]{preview}
            \\usepackage{amsmath}
            \\usepackage{amssymb}
            \\usepackage{amsfonts}
            \\usepackage{tikz}
            \\begin{document}
            \\begin{preview}
            \\begin{tikzpicture}[inner sep=0pt, outer sep=0pt]
            \\node at (0, 0) {

            texCode

            }; % <--Put your tex-code here
            \\end{tikzpicture}
            \\end{preview}
            \\end{document}
            """.replace('texCode', latex_stmt)
            return latex_template

        else:
        # elif 'align' == self.LatexStmtType(latex_stmt):
            latex_template = """
            \\documentclass[paper=a5,fontsize=16pt]{scrbook}
            \\usepackage[pdftex,active,tightpage]{preview}
            \\usepackage{amsmath}
            \\usepackage{amssymb}
            \\usepackage{amsfonts}
            \\usepackage{tikz}
            \\begin{document}
            \\begin{preview}

            texCode


            \\end{preview}
            \\end{document}
            """.replace('texCode', latex_stmt)
            return latex_template