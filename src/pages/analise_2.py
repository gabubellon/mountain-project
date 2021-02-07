import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import util


def write():
    util.write_title("- Ticket Médio de Julho/2020")

    st.markdown("---")

    st.markdown("# Por Campanha")

    df_ligacoes = get_ticket_medio_ligacoes()
    fig = go.Figure(
        data=[
            go.Bar(
                name="Ligações",
                x=df_ligacoes["avg_ticket"],
                y=df_ligacoes["midia"],
                orientation="h",
            ),
        ]
    )

    fig.update_layout(
        title="Ticket Médio das ligações por mídia (Julho 2020)",
        yaxis_title="Mídia",
        xaxis_title="Ticket Médio",
    )
    fig.update_yaxes(
        tickangle=0, title_font={"size": 20}, tickformat="%d-%a", tickmode="linear"
    )
    st.plotly_chart(fig, use_container_width=False)

    df_vendas = get_ticket_medio_vendas()
    fig = go.Figure(
        data=[
            go.Bar(
                name="Ligações",
                x=df_vendas["avg_ticket"],
                y=df_vendas["midia"],
                orientation="h",
            ),
        ]
    )

    fig.update_layout(
        title="Ticket Médio das vendas por mídia (Julho 2020)",
        yaxis_title="Mídia",
        xaxis_title="Ticket Médio",
    )
    fig.update_yaxes(
        tickangle=0, title_font={"size": 20}, tickformat="%d-%a", tickmode="linear"
    )
    st.plotly_chart(fig, use_container_width=False)


def get_ticket_medio_vendas():
    query = """
        select 
            midia,
            COUNT(*) as total,
            SUM(monthly_value) as value,
            SUM(monthly_value)/COUNT(*) as avg_ticket
        from public.attendances a  
            join attendances_calls ac on ac.attendance_id = a.id 
            join call_history_queue chq on chq."token" = ac."token" 
            join lines_mkt_final lmf on lmf.line_id = ac.line_id::text
        where a.type_id=1  --VENDA
        group by midia 
        """
    return util.query_df(query)


def get_ticket_medio_ligacoes():
    query = """
        select 
            midia,
            COUNT(*) as total,
            SUM(monthly_value) as value,
            SUM(monthly_value)/COUNT(*) as avg_ticket
        from public.attendances a  
            join attendances_calls ac on ac.attendance_id = a.id 
            join call_history_queue chq on chq."token" = ac."token" 
            join lines_mkt_final lmf on lmf.line_id = ac.line_id::text
        where a.type_id=1  --VENDA
        group by midia 

        """
    return util.query_df(query)
