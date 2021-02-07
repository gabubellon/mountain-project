import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class CreatePlot:
    def __init__(self, sample_df):
        self.sample_df = sample_df
