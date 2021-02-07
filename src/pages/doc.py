import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import util


def write():
    util.write_title("- Documentação")
    st.markdown("---")
    st.markdown(
        """
        Esse documento apresenta um pequeno relatório dinâmico dos dados de Junho de 2020, tendo as seguintes análises:
        * Ligações: Informações das ligações por dia e alguns detalhes por hora e dia da semana;
        * Ticket Médio: Informações sobre o Ticket Médio das ligações e Vendas;
        * Ligações Receptivas: Informações das ligações receptivas;
    """
    )
