import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import util


def write():
    util.write_title("- Receptivas de Junho/2020")
    st.markdown("---")

    df_qtd_finalizadas = get_qtd_finalizadas()
    st.markdown("# Por Status Final")
    fig = px.sunburst(
        df_qtd_finalizadas,
        path=["status_final", "midia", "campanha"],
        values="total",
        color="total",
        color_continuous_scale="RdBu",
        width=1400,
        height=700,  # Tamanho do grafico
        title="Ligações Receptivas por Status Final, Mídia e Campanha",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("# Por Mídia")
    fig = px.sunburst(
        df_qtd_finalizadas,
        path=["midia", "campanha", "status_final"],
        values="total",
        color="total",
        color_continuous_scale="RdBu",
        width=1400,
        height=700,  # Tamanho do grafico
        title="Ligações Receptivas por Mídia,Campanha e Status Final",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("# Por Campanha")
    fig = px.sunburst(
        df_qtd_finalizadas,
        path=["campanha", "status_final", "midia"],
        values="total",
        color="total",
        color_continuous_scale="RdBu",
        width=1400,
        height=700,  # Tamanho do grafico
        title="Ligações Receptivas por Campanha, Status Final e Mídia",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("# Pontos de destaque")
    st.markdown(
        """
        * Campanha **ESC_SEOB_telefone** é a com mais destaque nas ligações receptivas
        * Mídia **ORGANIC** tem mais de 75% de todas as ligações
        * Os statua de finalização (Cliente/Atendente) tem equilibrio dentro das ligações receptivas
    """
    )


def get_qtd_finalizadas():
    query = """
        select 
            tt.description as status_final,
            lmf.campanha,
            lmf.midia,
            COUNT(*) as total
        from call_history_queue chq 
            join telephony_types tt on tt.id  = chq.queue_log_verb_types_id 
            join telephony_types tt2 on tt2.id  = chq.queue_log_modality_types_id 
            join attendances_calls ac on ac."token" = chq."token" 
            join lines_mkt_final lmf on lmf.line_id = ac.line_id::text
        where tt2.description ='Entrada'
        group by 1,2,3
        """
    return util.query_df(query)
