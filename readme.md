# 📈 Maths Vision

**Maths Vision** est une application web interactive conçue pour l'exploration mathématique. Développée avec **Python**, elle combine la puissance du calcul formel de **SymPy** avec l'élégance visuelle de **Matplotlib** et **Seaborn**, le tout orchestré via une interface intuitive propulsée par **Streamlit**.

---

## 🚀 Fonctionnalités

- **Saisie interactive & Barre d'outils mathématique** : Insérez rapidement des fonctions usuelles (racines, exponentielles, logarithmes, trigonométrie), des constantes ($\pi$) et des symboles ($\infty$) sans avoir à tout taper à la main.
- **Analyse mathématique formelle** :
  - Calcul de la dérivée $f'(x)$
  - Calcul de l'intégrale indéfinie $\int f(x) \, dx$
  - Détermination automatique du domaine de définition ($D_f$)
  - Calcul des limites en $-\infty$ et $+\infty$
- **Visualisation graphique dynamique** : Tracé haute résolution des courbes avec des options de personnalisation de la plage d'affichage ($X_{\min}$ / $X_{\max}$).

---

## 🛠️ Installation et Utilisation Locale

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/ton-nom-utilisateur/maths-vision.git
   cd maths-vision
   ```

2. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application Streamlit :**
   ```bash
   streamlit run app.py
   ```

---

## 📦 Dépendances principales

- `streamlit` : Interface web interactive
- `sympy` : Calcul formel et symbolique
- `numpy` : Calcul numérique rapide
- `matplotlib` & `seaborn` : Génération et stylisation des graphiques

---

## 📄 Licence

Ce projet est libre d'utilisation et open-source. N'hésite pas à contribuer ou à l'adapter selon tes besoins !