# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:47:04 2019

@author: STEM
"""

import pandas as pd
dir(pd)
import plotly
from plotly.offline import plot
dir(plotly)
import plotly.graph_objs as go

wceodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenCEOs")


womenceos = go.Bar(x= wceodf["Year"], y=wceodf["CEOs"],
                         marker = {"color": wceodf["CEOs"], "colorscale" : "Rainbow"})

titles = go.Layout(title = "Percentage of Women Who Are CEOs",
                   
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Year",)),

                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",))
                    )

fig = go.Figure(data=[womenceos], layout = titles)

plot(fig)
