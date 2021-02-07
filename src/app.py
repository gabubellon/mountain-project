import streamlit as st

import pages.analise_1
import pages.analise_2
import pages.analise_3
import pages.doc
import pages.home
import util


def main():
    PAGES = {
        "Início": pages.home,
        "Ligações": pages.analise_1,
        "Ticket Médio": pages.analise_2,
        "Ligações Receptivas": pages.analise_3,
        "Documentação": pages.doc,
    }

    st.sidebar.write()
    st.sidebar.title("Páginas")
    selection = st.sidebar.radio("", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Carregando {selection} ..."):
        util.write_page(page)

    st.sidebar.title("Sobre")
    st.sidebar.info(
        """
        Projeto desenvolvido por:
        
        Gabriel Bellon
        """
    )


if __name__ == "__main__":
    main()
