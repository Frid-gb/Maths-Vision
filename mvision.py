import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sympy.calculus.util import continuous_domain

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Maths Vision",
    page_icon="📈",
    layout="wide"
)

# Application d'un style seaborn pour de beaux graphiques
sns.set_theme(style="whitegrid")

# Initialisation de la variable de session pour la formule
if "formula" not in st.session_state:
    st.session_state.formula = "x**3 - 3*x"

# Fonction de rappel (callback) appelée lors du clic sur un bouton de symbole
def add_to_formula(val):
    st.session_state.formula += val


def parse_expression(expr_str: str):
    """Convertit une chaîne de caractères en expression SymPy avec la variable 'x'."""
    if not expr_str or not expr_str.strip():
        return None, None
    
    x = sp.Symbol('x')
    expr_str = expr_str.replace('^', '**')
    try:
        local_dict = {
            'x': x, 'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 
            'exp': sp.exp, 'log': sp.log, 'sqrt': sp.sqrt,
            'pi': sp.pi, 'oo': sp.oo, 'Abs': sp.Abs
        }
        expr = sp.sympify(expr_str, locals=local_dict)
        return x, expr
    except Exception:
        return None, None


def compute_calculus(x, expr):
    """Calcule la dérivée, l'intégrale indéfinie, les limites et le domaine de définition."""
    derivative = sp.diff(expr, x)
    integral = sp.integrate(expr, x)
    limit_inf = sp.limit(expr, x, -sp.oo)
    limit_sup = sp.limit(expr, x, sp.oo)
    
    try:
        domain = continuous_domain(expr, x, sp.S.Reals)
    except Exception:
        domain = "Non calculable automatiquement"
    
    return derivative, integral, limit_inf, limit_sup, domain


def generate_plot(x, expr, x_min, x_max, num_points=400):
    """Génère un graphique Matplotlib/Seaborn de la fonction."""
    f_num = sp.lambdify(x, expr, modules=['numpy'])
    X = np.linspace(x_min, x_max, num_points)
    
    try:
        Y = f_num(X)
    except Exception:
        Y = []
        for val in X:
            try:
                Y.append(float(expr.subs(x, val)))
            except Exception:
                Y.append(np.nan)
        Y = np.array(Y)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=X, y=Y, ax=ax, color='b', linewidth=2.5, label=f"f(x) = {expr}")
    
    ax.set_title("Représentation Graphique", fontsize=14, fontweight='bold')
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("f(x)", fontsize=12)
    ax.axhline(0, color='black', linewidth=1, linestyle='--')
    ax.axvline(0, color='black', linewidth=1, linestyle='--')
    ax.legend(loc="upper right")
    
    return fig


def main():
    st.title("Maths Vision")

    st.sidebar.header("Paramètres & Symboles")
    
    # Champ de texte lié directement à l'état de session via la clé "formula"
    st.sidebar.text_input(
        "Entrez une fonction f(x) :", 
        key="formula"
    )
    
    # Barre d'outils interactive
    st.sidebar.subheader("🔣 Insérer des symboles")
    
    symbols_grid = [
        [("+", "+"), ("-", "-"), ("*", "*"), ("/", "/")],
        [("puissance (^)", "**"), ("racine (sqrt)", "sqrt("), ("exponentielle", "exp("), ("logarithme", "log(")],
        [("sinus", "sin("), ("cosinus", "cos("), ("tangente", "tan("), ("valeur abs", "Abs(")],
        [("Pi (π)", "pi"), ("Infini (∞)", "oo"), ("variable x", "x"), ("parenthèse )", ")")]
    ]
    
    for row_idx, row in enumerate(symbols_grid):
        cols = st.sidebar.columns(len(row))
        for col_idx, (label, val) in enumerate(row):
            cols[col_idx].button(
                label, 
                use_container_width=True, 
                key=f"btn_{row_idx}_{col_idx}",
                on_click=add_to_formula,
                args=(val,)
            )

    st.sidebar.subheader("Plage d'affichage (Graphe)")
    x_min = st.sidebar.number_input("X min", value=-5.0)
    x_max = st.sidebar.number_input("X max", value=5.0)

    if x_min >= x_max:
        st.sidebar.error("X min doit être inférieur à X max.")
        return

    # Analyse de l'expression courante
    x, expr = parse_expression(st.session_state.formula)

    if expr is not None:
        st.subheader("1. Analyse Mathématique")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Fonction analysée :**")
            st.latex(f"f(x) = {sp.latex(expr)}")

        derivative, integral, limit_inf, limit_sup, domain = compute_calculus(x, expr)

        with col2:
            st.markdown("**Résultats formels :**")
            st.latex(f"f'(x) = {sp.latex(derivative)}")
            st.latex(f"\\int f(x) \\, dx = {sp.latex(integral)} + C")

        # Affichage du domaine de définition
        st.markdown(f"**Domaine de définition :**")
        st.latex(f"D_f = {sp.latex(domain)}")

        st.info(f"**Limites :** En $-\\infty$ : `{limit_inf}` | En $+\\infty$ : `{limit_sup}`")

        st.subheader("2. Visualisation Graphique")
        fig = generate_plot(x, expr, x_min, x_max)
        st.pyplot(fig)
    else:
        st.info("💡 Saisissez ou composez une expression mathématique valide dans la barre latérale pour voir l'analyse et le graphique.")


if __name__ == "__main__":
    main()