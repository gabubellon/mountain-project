import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import util


def write():
    util.write_title("- Ligações de Julho/2020")
    df_ligacoes = get_qtd_ligacoes_dias()
    st.markdown("---")

    st.markdown("# Por dia do mês")
    fig = go.Figure(
        data=[
            go.Bar(
                name="Ligações",
                x=df_ligacoes["total_ligacoes"],
                y=df_ligacoes["data"],
                orientation="h",
            ),
        ]
    )

    fig.update_layout(
        title="Quantidade de ligações por dia (Julho 2020)",
        yaxis_title="Dias",
        xaxis_title="Quantidade",
        barmode="group",
    )
    fig.update_yaxes(
        tickangle=0, title_font={"size": 20}, tickformat="%d-%a", tickmode="linear"
    )
    st.plotly_chart(fig, use_container_width=False)
    df_diass = get_qtd_ligacoes_dias_s()

    st.markdown("# Por dia da semana")
    fig = go.Figure(
        data=[
            go.Bar(
                name="Ligações",
                x=df_diass["total_ligacoes"],
                y=df_diass["dia_semana"],
                orientation="h",
            ),
        ]
    )

    fig.update_layout(
        title="Quantidade de ligações por dia da semana (Julho 2020)",
        yaxis_title="Dia da Semana",
        xaxis_title="Quantidade",
        barmode="group",
    )
    fig.update_yaxes(tickangle=0, title_font={"size": 20}, tickmode="linear")
    st.plotly_chart(fig, use_container_width=False)

    st.markdown("# Por dia da semana e hora")
    df_hora_s = get_qtd_ligacoes_hora_s()
    fig = px.area(
        df_hora_s, facet_col="dia_semana", facet_col_wrap=1, x="hora", y="total"
    )
    fig.update_layout(
        title="Quantidade de ligações por dia da semana e hora (Julho 2020)",
        xaxis_title="Quantidade",
    )
    fig.update_xaxes(tickangle=0, title_font={"size": 20}, tickmode="linear")

    st.plotly_chart(fig, use_container_width=False)

    st.markdown("# Tabela")
    st.dataframe(df_ligacoes, width=1200)

    st.markdown("# Pontos de destaque")
    st.markdown(
        """
        * Durante o mês de Julho tivemos um crescimento de acentuado das ligações ao decorrer do mês;
        * O pico atendimento ocorre do **dia 18**, todavia, nos final do mês tivemos um atendimento similar;
        * A concentração das ligações se deu em sua maioria entre as **11h as 13hs**;
        * E fora do período de pico, mantemos uma margem de **6k de ligações por hora**.
    """
    )


def get_qtd_ligacoes_dias():
    query = """
            SELECT 
            date_trunc('day',created_at)::date as data,
            COUNT(id) as total_ligacoes
        FROM public.call_history_queue
        group by 1
        order by 1 desc;
        """
    return util.query_df(query)


def get_qtd_ligacoes_dias_s():
    query = """
            SELECT 
            concat(
            		to_char(created_at, 'd'),
            		'-',
            		to_char(created_at, 'dy')
            	 ) as dia_semana,
            COUNT(id) as total_ligacoes
        FROM public.call_history_queue
        group by 1
        order by 1
        """
    return util.query_df(query)


def get_qtd_ligacoes_hora_s():
    query = """
        SELECT 
            concat(to_char(created_at, 'd'),'-',to_char(created_at, 'dy')) as dia_semana,
            date_part('hour',date_trunc('hour',created_at)) as hora,
            COUNT(id) as total
        FROM public.call_history_queue
        group by 1,2;

        """
    return util.query_df(query)
