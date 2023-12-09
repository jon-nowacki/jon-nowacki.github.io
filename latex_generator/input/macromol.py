import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_directory)
output_dir = os.path.join(root_dir, 'output', 'macromolecular')
sys.path.append(root_dir)

from latexToSvg import LatexToSvg
x = [
    #superposition 
    {
        "name":  "rmsd",
        "latex": "$\\text{RMSD} = \\sqrt{\\sum_{i=1}^{n} \\left( x_i - y_i \\right)^2}$"
    },
    {
        "name": "rmsd_expanded",
        "latex": "$\\text{RMSD} = \\sum (x_i^2 + y_i^2) - 2 \\sum (x_i \\cdot U \\cdot y_i)$"
    }
    ,
    {
        "name": "min_rmsd",
        "latex": "$2 \\sum (x_i \\cdot U \\cdot y_i)$"
    },
    {
        "name": "min_trace",
        "latex": "$L = \\text{Trace}(X \\cdot U \\cdot Y^T)$"
    },
    {
        "name": "cyclic",
        "latex": """
        \\begin{align*}
            L &= \\text{Trace}(X \\cdot U \\cdot Y^T) \\\\
            &= \\text{Trace}(U \\cdot Y^T \\cdot X) \\\\
            &= \\text{Trace}(U \\cdot R)
        \\end{align*}
        """
    },
    {
        "name": "svd",
        "latex": """
            \\begin{align*}
            \\text{Trace}(U \\cdot R) &= \\text{Trace}(U \\cdot V \\cdot S \\cdot W^T) \\\\
                                    &= \\text{Trace}(S \\cdot W^T \\cdot U \\cdot V)
            \\end{align*}        
        """
    },
    {
        "name": "maximize",
        "latex": "$\\text{Trace}(S \\cdot T) = S_{11} \\cdot T_{11} + S_{22} \\cdot T_{22} + S_{33} \\cdot T_{33}$"
    },
    {
        "name": "identity",
        "latex": "$T = W^T \\cdot U \\cdot V = I$"
    },
    {
        "name": "tmscore",
        "latex": "${\\text{TMscore}} = 1 + \\frac{1}{L_T} \\sum_{i=1}^{L_{Ali}} \\frac{1}{1 + \\left(\\frac{d_i}{d_0}\\right)}$"
    },
    {
        "name": "physical",
        "latex":
            """
            $\\sum_{bonds} k_b (b - b_0)^2 + \\sum_{angles} \\theta_k (\\theta - \\theta_0)^2 + \\sum_{vw} \\ \\epsilon(  (\\frac{R_{\\text{min},ij}}{r_{ij}})^{12} - (\\frac{R_{\\text{min},ij}}{r_{ij}})^5 \\\\
            \\sum_{Elect} \\frac{q_i q_j}{\\varepsilon_{\\text{r}} r_{ij}} + \\sum_{improp} w_k (w - w_0)^2 + \\sum_{UB} u_k (u - u_0)^2$
            """
    },
    {
        "name": "physical_energy",
        "latex":
            """
            \\begin{align*}
            E = &\\sum_{bonds} k_b (b - b_0)^2 + \\sum_{angles} \\theta_k (\\theta - \\theta_0)^2 + \\\\
            & \\sum_{vw} \\epsilon(  (\\frac{R_{\\text{min},ij}}{r_{ij}})^{12} - (\\frac{R_{\\text{min},ij}}{r_{ij}})^5) + \\\\
            & \\sum_{Elect} \\frac{q_i q_j}{\\varepsilon_{\\text{r}} r_{ij}} + \\sum_{improp} w_k (w - w_0)^2 + \\\\
            & \\sum_{UB} u_k (u - u_0)^2
            \\end{align*}
            """
    }
    ,


    {
        "name": "amino_preference",
        "latex": 
            """
            \\begin{align*}
            E_{\\text{respref}} &= -w \\sum_{i}^{L_{\\text{ch1}}} \\sum_{j}^{L_{\\text{ch2}}} P(A_i, A_j) \\\\
            P(A_i, A_j) &=
            \\begin{cases}
                \\frac{f(A_i, A_j)}{\\sum_{i=1}^{20} f(A_i, A_j)} \\cdot \\frac{t(A)}{\\sum_{i=1}^{20} t(A_i)} & \\text{if } c_{i,j} \\leq 6 \\\\
                0 & \\text{otherwise}
            \\end{cases}
            \\end{align*}
            """
    },
    {
        "name": "orientation",
        "latex": """
        \\begin{align*}        
            &E_{\\text{oricontact}} = -w \\sum_{i} \\sum_{j} E_{i,j}(s_{i,j}) \\\\
            &E_{i,j}(s_{i,j}) = e(A_i,Aj, \gamma_(i,j) ) = \\frac{ f(A_i,Aj,\gamma_{ij}) } { f(A_i, A_j)}
        \\end{align*}        
        """
    },
    {
        "name": "dfire",
        "latex": 
        """
            $D(i,j,r) =-wln \\frac{N_{obs}} { \\left(\\frac{r}{r_{cut}}\\right)^\\alpha \\left(\\frac{\\Delta r}{\\Delta r_{cut}}\\right) N_{obs} \\left(i,j,r_{cut} \\right)}$
        """
    },
    {
        "name": "dist_map",
        "latex": "$E_{\\text{distmap}} = w \\sum_{i} \\sum_{j} (r_{ij} - d_{ij} - \\delta_{ij})$"
    }
]

y = LatexToSvg(x, output_dir)
y.Run()