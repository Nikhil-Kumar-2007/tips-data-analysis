import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, callback, dcc, Input, Output


df = pd.read_csv('tip.csv')
df.rename(columns = {'sex' : 'gender'}, inplace = True)
df['gender_size'] = df['gender'].map({'Male' : 8, 'Female' : 10})
df['smoker_color'] = df['smoker'].map({'Yes' : 'blue', 'No' : 'red'})
total_customers = df.shape[0]
total_bill = int(df['total_bill'].sum())
total_tip = int(df['tip'].sum())
smoker = int(df['smoker'].value_counts()['Yes'])

sizeTip = df.groupby('size').agg({'tip' : 'sum'}).reset_index()

option = [
    {'label' : 'Without Filters', 'value' : 'without_filter'},
    {'label' : 'smoker', 'value' : 'smoker'},
    {'label' : 'gender', 'value' : 'gender'},
    {'label' : 'day', 'value' : 'day'},
    {'label' : 'All Filters', 'value' : 'All'}
]

symbol_map = {
            'Sun' : 'triangle-up',
            'Mon' : 'star',''
            'Tue' : 'hourglass',
            'Wed' : 'diamond',
            'Thur' : 'circle',
            'Fri' : 'square',
            'Sat' : 'x'
        }

all_data_traces = []        
        
for category in sorted(df['day'].unique()):
    subset_df = df[df['day'] == category]
    marker_shape = symbol_map.get(category)
    label = df[df['day'] == category].apply(lambda row : f"Gender : {row['gender']}, Day : {row['day']}, Smoker : {row['smoker']}", axis = 1)
    all_data_traces.append(go.Scatter(x = subset_df['total_bill'], y = subset_df['tip'], mode = 'markers', marker = dict(symbol = marker_shape, size = subset_df['gender_size'], color = subset_df['smoker_color']), name = f'{category}', text = label, hoverinfo = 'text + x + y'))   
    
margin_graph = dict(t=50, b=8)

title_graph = {
                'text' : 'tip v/s total bill',
                'x' : 0.5,
                'xanchor' : 'center',
                'font' : dict(size = 22, family = 'Arial', color = 'darkblue')
            }

legend_layout = dict(
        orientation='v',
        x=1.02,
        y=0.5,
        xanchor='left',
        yanchor='middle'
    )    
    
x_axis = {'title' : 'total bill', 'showline' : True, 'linecolor' : 'black', 'linewidth' :  2}
y_axis = {'title' : 'tip', 'showline' : True, 'linecolor' : 'black', 'linewidth' : 2}

all_graph_layout = go.Layout(title = title_graph, xaxis = x_axis, yaxis = y_axis, template = 'plotly', margin = margin_graph, legend = dict(legend_layout, title = 'all'), paper_bgcolor = '#cbcca0'
    )
    
    
title_6 = dict(x = 0.5, xanchor = 'center', font = dict(size = 18, family = 'Arial', color = 'darkblue'))
x_62 = {'showline' : True, 'linecolor' : 'black', 'linewidth' : 2}    
y_62 = {'showline' : True, 'linecolor' : 'black', 'linewidth' : 2} 
style_6 = {
    'height' : '300px'
}
margin_6 = dict(t=50, b=5, r=5, l=5)

fig_sun = px.sunburst(df, path = ['time', 'day'], values = 'tip', title = 'contribution of time with day')
fig_sun.update_layout(title = title_6, paper_bgcolor = '#cbcca0', margin = margin_6)

fig_bar = px.bar(sizeTip, x = 'size', y = 'tip', title = 'tip v/s size', text_auto = True)
fig_bar.update_layout(title = title_6, xaxis = x_62, yaxis = y_62, paper_bgcolor = '#cbcca0', margin = margin_6)    

# bootstrap load from CDA
external_stylesheet = [
    {
        'href' : 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel' : 'stylesheet',
        'integrity' : 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin' : 'anonymous'
    }
]


app = Dash(__name__, external_stylesheets = external_stylesheet)
server = app.server

app.layout = html.Div(children = [
    html.H1("Tips data of waiters", style = {'color' : '#ffffff', 'text-align' : 'center', 'font-weight' : 'bold', 'margin' : '10px'}),
    html.Div(children = [
        html.Div(children = [
            html.Div(children = [
                html.Div(children = [
                    html.H4("Total Customers", className = 'text-light'),
                    html.H5(total_customers, className = 'text-light')
                ], className = 'card-body', style = {'text-align' : 'center'})
            ], className = 'card bg-danger')
        ], className = 'col-md-3 h-100 d-flex flex-column flex-grow-1'),
        html.Div(children = [
            html.Div(children = [
                html.Div(children = [
                    html.H4("Total bill", className = 'text-light'),
                    html.H5(f"{total_bill} rs", className = 'text-light')
                ], className = 'card-body', style = {'text-align' : 'center'})
            ], className = 'card bg-info')
        ], className = 'col-md-3 h-100 d-flex flex-column flex-grow-1'),
        html.Div(children = [
            html.Div(children = [
                html.Div(children = [
                    html.H4("Tip", className = 'text-light'),
                    html.H5(f"{total_tip} rs", className = 'text-light')
                ], className = 'card-body', style = {'text-align' : 'center'})
            ], className = 'card bg-warning')
        ], className = 'col-md-3 h-100 d-flex flex-column flex-grow-1'),
        html.Div(children = [
            html.Div(children = [
                html.Div(children = [
                    html.H4("Smokers", className = 'text-light'),
                    html.H5(smoker, className = 'text-light')
                ], className = 'card-body', style = {'text-align' : 'center'})
            ], className = 'card bg-success')
        ], className = 'col-md-3 h-100 d-flex flex-column flex-grow-1')
    ], className = 'row'),
    html.Div(children = [
        html.Div(children = [
            html.Div(children = [
                html.Div(children = [
                    dcc.Graph(id = 'sunburst', figure = fig_sun, style = style_6)         
                ], className = 'card-body')
            ], className = 'card')
        ], className = 'col-md-5'),
        html.Div(children = [
            html.Div(children = [
                html.Div(children = [
                    dcc.Graph(id = 'bar', figure = fig_bar, style = style_6)
                ], className = 'card-body')
            ], className = 'card')
        ], className = 'col-md-7')
    ], className = 'row'),
    html.Div(children = [
        html.Div(children = [
            html.Div(children = [
                html.Div(children = [
                    dcc.Dropdown(id = 'picker', options = option,value = "without_filter"),
                    dcc.Graph(id = 'scatter', style = {
                        'padding' : '3px',
                        'border' : '2px solid #ccc',
                        'backgroundColor' : '#f9f9f9',
                        'width' : '90%', 
                        'margin' : '15px'
                    })
                ], className = 'card-body')
            ], className = 'card')
        ], className = 'col-md-12')
    ], className = 'row')
], className = 'container')


@app.callback(Output('scatter', 'figure'), [Input('picker', 'value')])
def update_graph(type):
    if type == 'without_filter':
        return {'data' : [go.Scatter(x = df['total_bill'], y = df['tip'], mode = 'markers')], 'layout' : all_graph_layout}
    elif type == 'All':
        return {'data' : all_data_traces, 'layout' : all_graph_layout}
    else:
        fig = px.scatter(df, x = 'total_bill', y = 'tip', color = type)
        fig.update_layout(title = title_graph, margin = margin_graph, legend = legend_layout, xaxis = x_axis, yaxis = y_axis, paper_bgcolor = '#cbcca0')
        return fig
            
    
if __name__ ==  "__main__":
    app.run(debug = True)
