import sys
import subprocess
import streamlit as st
import asyncio
from dotenv import load_dotenv

from core.scripts.browser_use_example import run_browser_use_example
from core.scripts.debug_gif import main as run_debug_gif

load_dotenv()

st.set_page_config(page_title="MenTest", page_icon="👋", layout="wide")

st.title("MenTest: automatisation de tests")

st.sidebar.success("Sélectionne une option:")

if "playwright_installed" not in st.session_state:
    with st.spinner("Installation des navigateurs Playwright... "):
        try:
            result = subprocess.run(
                [sys.executable, "-m", "playwright", "install"],
                capture_output=True,
                text=False,
                check=True,
            )
            st.success("Navigateurs Playwright installés. ")
            st.code(result.stdout)
            st.session_state.playwright_installed = True
        except subprocess.CalledProcessError as e:
            st.error(f"Échec de l'installation des navigateurs Playwright : {e}")
            st.code(e.stderr)
        except FileNotFoundError:
            st.error(
                "Commande Playwright introuvable. Assurez-vous qu'elle est installée dans votre environnement."
            )

# Streamlit UI

if st.button(
    "Lancer la démo",
    key="run_example_button",
    help="Se connecte sur OrangeHRM, ajoute une personne en tant que contact d'urgence, puis se déconnecte.",
):
    with st.spinner("Exécution de l'exemple d'utilisation du navigateur..."):
        result = asyncio.run(
            run_debug_gif(
                # task="Connecte-toi sur https://opensource-demo.orangehrmlive.com, ajoute ma femme: Lucy en tant que contact d'urgence, puis déconnecte.",
                # use_vision=True,
            )
        )
        if result:
            st.success("Exécution terminée !")
            st.write("Résultat :")
            st.code(result, language="text", wrap_lines=True)
        else:
            st.error("Une erreur s'est produite ou aucun résultat n'a été retourné.")
