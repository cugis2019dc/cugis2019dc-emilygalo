# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:50:14 2019

@author: STEM
"""

Darkchocolate = 5
Milk = 6
White = 8
print(White)
White

CadburyType1 = 6
CadburyType2= 5
CadburyType3= 8
print("There are", CadburyType1,"Milk choclolates,", CadburyType2,"Dark chocolates, and", CadburyType3,"White chocolates in the Cadbury Box.")

Chocolate1 ={"Cadburymilk":5} 
Chocolate2 ={"Cadburydark":8}
Chocolate3 ={"Cadburywhite":3}
print(Chocolate1,Chocolate2,Chocolate3)

Steve ={"Steve":32}
Lia ={"Lia":28}
Vin ={"Vin":45}
Katie ={"Katie":38}
print(Steve, Lia, Vin, Katie)

studentage ={"Steve":32,"Lia":28,"Vin":45,"Katie":38}
studentage

studentgender ={"Steve":"M","Lia":"F","Vin":"M","Katie":"F"}
studentgender

student =[studentage,studentgender]
student


studentlist = [['Steve',32,"M"],["Lia",28,"F"],["Vin",45,"M"],["Katie",38,"F"]]
studentlist

import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentlist, columns=("Name","Age","Gender"))
studentdf

chocolates = [["Milk", 5], ["Dark", 6], ["White", 8],]
chocodf = pandas.DataFrame(chocolates, columns=("Chocolate", "Quantity"))
print(chocodf)

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

chocobar = go.Bar(x=chocodf["Chocolate"],y=chocodf["Quantity"])
plot([chocobar])

titles = go.Layout(title = "Number of Chocolates by Type")

chocobar=go.Bar(x=chocodf["Chocolate"],y=chocodf["Quantity"])

fig = go.Figure(data=[chocobar], layout=titles)
plot(fig)



students = [["Steve", 32],["Lia", 28],["Vin", 45],["Katie", 38]]
studentdf = pandas.DataFrame(students, columns=("Name", "Age"))
print(studentdf)


studentdf2 = pandas.DataFrame(studentlist,columns=("Name","Age","Gender"),index=["1","2","3","4"])
studentdf2

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf["Name"],y=studentdf["Age"])
plot([studentbar])



