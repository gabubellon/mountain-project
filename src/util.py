import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import streamlit as st

import config as cfg


def get_conn():
    return psycopg2.connect(
        dbname=cfg.SQL_DB,
        user=cfg.SQL_USER,
        password=cfg.SQL_PASS,
        port=cfg.SQL_PORT,
        host=cfg.SQL_HOST,
    )


def query_df(query, cache_file=None):
    return sqlio.read_sql_query(query, get_conn())


def write_page(page):
    page.write()


def write_header():
    st.write("**Relatório Dinâmico - Escale**")


def write_title(body: str):
    st.write(f"# Relatório Dinâmico {body}")
