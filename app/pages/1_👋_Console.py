from contextlib import contextmanager
from io import StringIO
import streamlit as st
import sys

import subprocess
import asyncio
from dotenv import load_dotenv

from core.scripts.browser_use_example import run_browser_use_example
from core.scripts.debug_gif import main as run_debug_gif


@contextmanager
def st_redirect(src, dst):
    placeholder = st.empty()
    output_func = getattr(placeholder, dst)

    with StringIO() as buffer:
        old_write = src.write

        def new_write(b):
            buffer.write(b)
            output_func(buffer.getvalue())

        try:
            src.write = new_write
            yield
        finally:
            src.write = old_write

@contextmanager
def st_stdout(dst):
    with st_redirect(sys.stdout, dst):
        yield

@contextmanager
def st_stderr(dst):
    with st_redirect(sys.stderr, dst):
        yield


if st.button(
    "Lancer la démo",
    key="run_example_button",
    help="Se connecte sur OrangeHRM, ajoute une personne en tant que contact d'urgence, puis se déconnecte.",
):
    with st_stdout("success"), st_stderr("error"):
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
