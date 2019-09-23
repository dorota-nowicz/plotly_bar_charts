import pandas as pd
import plotly
import plotly.graph_objects as go

# load rain data to dataframe
file_name = "test.xlsx"
xl_file = pd.ExcelFile(file_name)
df_rain = xl_file.parse('Hoja1')

# get timestamps
index_time = df_rain['Fecha'].tolist()

# prepare dataset for every gage in df
data_bar = []

for nombre_pluv in df_rain.columns[1:]:

    intensidad = df_rain[nombre_pluv].tolist()
    data_bar.append(go.Bar(name=nombre_pluv, x=index_time, y=intensidad,marker_color ='blue'))

# prepare a figure
fig = go.Figure(data= data_bar,)
fig.update_layout(barmode='group')

fig.update_layout(
    title_text='DANA Murcia septiembre  2019',
    autosize=False,
    width=1350,
    height=900,
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Tiempo [hora]",
            font=dict(
                size=20,
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Precipitación [mm/1 hora]",
            font=dict(
                size=20,
            ),
        )
    )
    
)


plotly.offline.plot(fig, filename='chsegura092019.html') 

# if want to see a fig in Jupyter
# fig.show()
