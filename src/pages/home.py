import streamlit as st

import util


def write():
    util.write_title("- Página Inicial")

    st.markdown(
        """
        # Relatório Dinâmico - Mês Referência Junho/2020 

        ## Dados Disponíveis:

        * Ligações
        * Ticket Médio
        * Ligações Receptivas

        Escolha uma das opções para visualizar as informações pertinestes, caso tenha alguma dúvida acesse a opção *Documentação*
    """
    )
