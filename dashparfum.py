#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output, State
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[2]:


data_mens = pd.read_csv("C:/Users/Ayoub/Desktop/ebay_mens_perfume.csv")
data_womens = pd.read_csv("C:/Users/Ayoub/Desktop/ebay_womens_perfume.csv")


# In[3]:


data_mens_net = data_mens.dropna()
data_womens_net = data_womens.dropna()
data_mens_net.loc[: , 'Category'] = 'Parfum For Men'
data_womens_net.loc[: ,'Category'] = 'Parfum For Women'

# Combinaison des deux DataFrames
data = pd.concat([data_mens_net, data_womens_net])


# In[4]:


dic_brand = {
 'AS  SHOWN': 'AS SHOW',
 'Al Rehab': 'Al-Rehab',
 'As Picture Shown': 'As Show',
 'As Show':'As Show',
 'As Shown':'As Show',
 'As picture show':'As Show',
 'As shown':'As Show',
 'Bharara': 'BHARARA',
'CHRISTIAN DIOR':'DIOR',
'Chloé': 'Chloe',
'Christian Dior':'DIOR',
'Coty Inc.': 'Coty',
'Dior': 'DIOR',
 'Dolce & Gabbana':'D&G',
 'Dolce Gabbana':'D&G',
 'Dolce&Gabbana':'D&G',
'Elizabeth And James Nirvana': 'Elizabeth & James',
'Estée Lauder': 'Estee Lauder',
 'Gianni Versace': 'Versace',
 'Giorgi^o Armani' :'Armani',
 'Giorgio Arm.ani':'Armani',
 'Giorgio Armani':'Armani',
 'Giorgio² Armani':'Armani',
 'Heaven Scents': 'Have A Scent',
 'Hugo Boss': 'HUGO BOSS',
'Juliette Has a Gun': 'Juliette Has A Gun',
 'Juliette has a gun':'Juliette Has A Gun',
'Kate Spade New York': 'Kate Spade',
 'Kenneth Cole Reaction': 'Kenneth Cole',
'Lancome': 'LANCOME',
 'Lancôme': 'LANCOME',
'Lattafa Perfumes': 'Lattafa',
 'Lauren Ralph Lauren': 'Polo Ralph Lauren',
 'Maison Alhambra' : 'MAISON ALHAMBRA',
'Mercedes-Benz': 'Mercedes Benz',
'Michael Malul Gents Scents': 'Michael Malul',
 'Michael Malul London':'Michael Malul',
'MontBlanc' : 'Mont Blanc',
 'Montblanc' : 'Mont Blanc',
 'Parfums': 'Parfum',
 'Parfums Grès' : 'Parfums Gres',
 'Perfume' : 'Parfum',
'Polo': 'Polo Ralph Lauren',
 'Prada': 'PRADA',
 'Ralph Lauren': 'Polo Ralph Lauren',
'Roja': 'Roja Dove',
 'Roja Parfums': 'Roja Dove',
'Tiffany & Co.': 'Tiffany',
'Viktor & Rolf': 'Victor & Rolf',
'al hambra': 'MAISON ALHAMBRA',
 'as showed' :'As Show','MAISON FRANCIS KURKDJIAN':'F KURKDJIAN',
 '~ DOLCE & GABBANA ~': 'D&G'}

# Appliquer les corrections
data.loc[:,'brand'] = data['brand'].replace(dic_brand )
data.loc[:,'brand']= data['brand'].str.upper()
# brand en majuscule


# In[5]:


dic_brand = {
 'AS  SHOWN': 'AS SHOW',
 'Al Rehab': 'Al-Rehab',
 'As Picture Shown': 'As Show',
 'As Show':'As Show',
 'As Shown':'As Show',
 'As picture show':'As Show',
 'As shown':'As Show',
 'Bharara': 'BHARARA',
'CHRISTIAN DIOR':'DIOR',
'Chloé': 'Chloe',
'Christian Dior':'DIOR',
'Coty Inc.': 'Coty',
'Dior': 'DIOR',
 'Dolce & Gabbana':'D&G',
 'Dolce Gabbana':'D&G',
 'Dolce&Gabbana':'D&G',
'Elizabeth And James Nirvana': 'Elizabeth & James',
'Estée Lauder': 'Estee Lauder',
 'Gianni Versace': 'Versace',
 'Giorgi^o Armani' :'Armani',
 'Giorgio Arm.ani':'Armani',
 'Giorgio Armani':'Armani',
 'Giorgio² Armani':'Armani',
 'Heaven Scents': 'Have A Scent',
 'Hugo Boss': 'HUGO BOSS',
'Juliette Has a Gun': 'Juliette Has A Gun',
 'Juliette has a gun':'Juliette Has A Gun',
'Kate Spade New York': 'Kate Spade',
 'Kenneth Cole Reaction': 'Kenneth Cole',
'Lancome': 'LANCOME',
 'Lancôme': 'LANCOME',
'Lattafa Perfumes': 'Lattafa',
 'Lauren Ralph Lauren': 'Polo Ralph Lauren',
 'Maison Alhambra' : 'MAISON ALHAMBRA',
'Mercedes-Benz': 'Mercedes Benz',
'Michael Malul Gents Scents': 'Michael Malul',
 'Michael Malul London':'Michael Malul',
'MontBlanc' : 'Mont Blanc',
 'Montblanc' : 'Mont Blanc',
 'Parfums': 'Parfum',
 'Parfums Grès' : 'Parfums Gres',
 'Perfume' : 'Parfum',
'Polo': 'Polo Ralph Lauren',
 'Prada': 'PRADA',
 'Ralph Lauren': 'Polo Ralph Lauren',
'Roja': 'Roja Dove',
 'Roja Parfums': 'Roja Dove',
'Tiffany & Co.': 'Tiffany',
'Viktor & Rolf': 'Victor & Rolf',
'al hambra': 'MAISON ALHAMBRA',
 'as showed' :'As Show','MAISON FRANCIS KURKDJIAN':'F.KURKDJIAN',
 '~ DOLCE & GABBANA ~': 'D&G'}

# Appliquer les corrections
data.loc[:,'brand'] = data['brand'].replace(dic_brand )
data.loc[:,'brand']= data['brand'].str.upper()
# brand en majuscule


# In[6]:


abr_dict = {
    'DIOR': 'DIOR',
    'AS SHOW': 'A. SHOW',
    'UNBRANDED': 'UNBRND',
    'ARMANI': 'ARMNI',
    'MULTIPLE BRANDS': 'MULT BRND',
    'MAISON ALHAMBRA': 'MAISON ALH',
    'GUCCI': 'GUCCI',
    'POLO RALPH LAUREN': 'POLO RL',
    'D&G': 'D&G',
    'SECERTMU': 'SECRTMU',
    'VERSACE': 'VERSC',
    'PACO RABANNE': 'PACO RAB',
    'GRANDEUR': 'GRANDR',
    'ARMAF': 'ARMAF',
    'CAROLINA HERRERA': 'CARO HERR',
    'CLINIQUE': 'CLNIQ',
    'DUMONT': 'DUMNT',
    'AFNAN': 'AFNAN',
    'AZZARO': 'AZZRO',
    'BHARARA': 'BHARA',
    'VALENTINO': 'VALNTN',
    'GUY LAROCHE': 'GUY LROC',
    'MONT BLANC': 'MONT BLC',
    'GIVENCHY': 'GVNCY',
    'LATTAFA': 'LATFA',
    'JOHN VARVATOS': 'J. VARV',
    'NAUTICA': 'NAUTCA',
    'AS PICTURE SHOW': 'A. PICTURE SH',
    'TOMMY HILFIGER': 'T. HILF',
    '2ND TO NONE': '2ND NONE',
    'YVES SAINT LAURENT': 'YVES SAINT L',
    'CALVIN KLEIN': 'CAL KLEIN',
    'RASASI': 'RASASI',
    'COLOGNE': 'COLG',
    'ROJA DOVE': 'ROJA DVE',
    'METAHERBAL LABS': 'META LABS',
    'MIRAGE BRANDS': 'MIRAGE BRND',
    'ABERCROMBIE & FITCH': 'ABERC & FITCH',
    'MOSCHINO': 'MOSCHN',
    'SUPERZ BUDAPEST': 'SUPERZ BUD',
    'AS SHOWN': 'A. SHOWN',
    'DIESEL': 'DIESEL',
    'LACOSTE': 'LACOST',
    'BURBERRY': 'BURBRY',
    'MICHAEL MALUL': 'MICHAEL ML',
    'ARAMIS': 'ARAMIS',
    'JEAN PAUL GAULTIER': 'J. PAUL GAUL',
    'DAVIDOFF': 'DAVIDF',
    'BVLGARI': 'BVLGARI',
    'PARFUMS DE MARLY': 'PARFUMS MARLY',
    'ARD AL ZAAFARAN': 'ARD ZAAF',
    'KARL LAGERFELD': 'KARL LAGER',
    'J. DEL POZO': 'J. DEL POZO',
    'SEAN JOHN': 'SEAN J',
    'YSL': 'YSL',
    'JAGUAR': 'JAGUAR',
    'EBC': 'EBC',
    'ISSEY MIYAKE': 'ISSEY MIY',
    'HUGO BOSS': 'HUGO BSS',
    'DOSSIER': 'DOSIER',
    'TOMMY BAHAMA': 'T. BAHAMA',
    'PAUL SEBASTIAN': 'PAUL SEB',
    'HALLOWEEN': 'HALLOWEEN',
    'BOUCHERON': 'BOUCHR',
    'THIERRY MUGLER': 'THIERRY MUG',
    'JO MALONE': 'J. MALONE',
    'KHADLAJ': 'KHADLAJ',
    'HERMÈS': 'HERMES',
    'LOUIS VUITTON': 'L. VUITTON',
    'CREED': 'CREED',
    'MFK': 'MFK',
    'HERMES': 'HERMES',
    'FRAGRANCE': 'FRAGRNC',
    'CHANEL': 'CHNL',
    'LALIQUE': 'LALIQ',
    "PENHALIGON'S": 'PENHAL',
    'LIZ CLAIBORNE': 'LIZ CLAIB',
    'BY AL HAMBRA': 'BY AL HAM',
    'JOOP': 'JOOP',
    'TED LAPIDUS': 'TED LAP',
    'AXE': 'AXE',
    'LOMANI': 'LOMANI',
    'KING OF KINGS': 'KING KINGS',
    'RUE21': 'RUE21',
    'AL WATANIAH': 'AL WAT',
    'MACARENA': 'MACARENA',
    'COACH': 'COACH',
    'COTY': 'COTY',
    'LANVIN': 'LANVIN',
    'SALVATORE FERRAGAMO': 'SALVATORE FERR',
    'NIKOS': 'NIKOS',
    'LUCIANNO': 'LUCIAN',
    'VICTOR & ROLF': 'VICTOR ROLF',
    'ROCHAS': 'ROCHAS',
    'CLASSIC BRANDS': 'CLSSC BRND',
    'REYANE TRADITION': 'REYANE TRAD',
    'GIORGIO BEVERLY HILLS': 'GIORG BEV HLS',
    'MYRURGIA': 'MYRURG',
    'JOVAN': 'JOVAN',
    'EMPORIO ARMANI': 'EMPORIO ARM',
    'BENTLEY': 'BENTLEY',
    'F.KURKDJIAN': 'F.KURKDJ',
    'FRAGRANCE WORLD': 'FRAGRNC WRLD',
    'ALLSAINTS': 'ALLSINTS',
    'AVON': 'AVON',
    'YVES DE SISTELLE': 'YVES SIST',
    'LIMITED EDITION': 'LIMIT EDIT',
    'KENNETH COLE': 'KENNETH CL',
    'BOND NO. 9': 'BOND 9',
    'ACQUA DI PARMA': 'ACQUA PARMA',
    'GUERLAIN PARIS': 'GUERLAIN PRS',
    'AL HARAMAIN': 'AL HAR',
    'NARCISO RODRIGUEZ': 'NARCISO ROD',
    'TOPSHELF': 'TOPSHELF',
    'BRUT': 'BRUT',
    'ED HARDY': 'ED HARDY',
    'FM': 'FM',
    'PARIS HILTON': 'PARIS HLT',
    'HAVE A SCENT': 'HAVE SCENT',
    'ZARA': 'ZARA',
    'KENZO': 'KENZO',
    'MERCEDES BENZ': 'MERCEDES BZ',
    'FRANCK OLIVIER': 'FRANCK OLI',
    'MISSONI': 'MISSONI',
    'HALSTON': 'HALSTON',
    'PRADA': 'PRADA',
    'BARON': 'BARON',
    'GUERLAIN': 'GUERLAIN',
    'ACQUA DI GIO': 'ACQUA GIO',
    'OLD SPICE': 'OLD SPICE',
    'BATH & BODY WORKS': 'BATH BODY WKS',
    'CLIVE CHRISTIAN': 'CLIVE CHRIS',
    'TOM FORD': 'TOM FORD',
    'ROBERTO CAVALLI': 'ROBERTO CAV',
    'EMANUELLE UNGARO': 'EMANUEL UNG',
    'CURVE': 'CURVE',
    'ESTEE LAUDER': 'ESTEE LAUD',
    'PIERRE CARDIN': 'PIERRE CARD',
    'RAWCHEMISTRY': 'RAWCHEM',
    'STERLING': 'STERLING',
    'TERRITOIRE': 'TERRITOIR',
    'JIMMY CHOO': 'JIMMY CHOO',
    'LAPIDUS': 'LAPIDUS',
    'MARY KAY': 'MARY KAY',
    'L’OCCITANE': 'L’OCCIT',
    'MANCERA': 'MANCERA',
    'LLURE SX': 'LLURE SX',
    'JACQUES BOGART': 'JACQUES BOG',
    'FC': 'FC',
    'PHEROMONES': 'PHEROMN',
    'CARTIER': 'CARTIER',
    'HINODE': 'HINODE',
    'MICHAEL JORDAN': 'MICHAEL JORD',
    'DESIGNER SERIES': 'DESIGNER SR',
    'ALEXANDRIA FRAGRANCES': 'ALEX FRAGR',
    'EL GANSO': 'EL GANSO',
    'VICTOR MANUELLE': 'VICTOR MAN',
    'ENGLISH LAUNDRY': 'ENGL LAUND',
    'LUXURY': 'LUXRY',
    'HYBRID & COMPANY': 'HYBRID CMP',
    'PERRY ELLIS': 'PERRY ELLIS',
    'FRAGANCE ONE': 'FR ONE'
    
}
data.loc[:,'brand'] = data['brand'].replace(abr_dict )


# In[7]:


# Assurez-vous que priceWithCurrency est une colonne de type chaîne (string)
data.loc[:,'priceWithCurrency'] = data['priceWithCurrency'].astype(str)
# Diviser en colonnes Currency et Amount
split_values = data['priceWithCurrency'].str.split(' ', n=1, expand=True)
# Affecter les valeurs
data.loc[:,'Currency'] = split_values[0]  # Première partie après la division

data.loc[data['Currency'] == 'C', 'price'] *= 0.73


# In[8]:


## En-TETE : 

Titre = html.H1('FRAGRANCE INSIGHTS: UNVEILING THE SCENT MARKET',
                style={'color': '#4e3663','font-family': 'Garamond, serif','font-size': '30px','margin-left': '5%'})

barr_navig = html.Div(
        [
            dcc.Link('HOME', href='/', style={'color': '#4e3663', 'margin-right': '14px','margin-left': '3%','margin-right': '3%',
                                                  'font-family': 'Garamond, serif','font-weight': 'bold','text-decoration': 'none'}),
            
            dcc.Link("GLOBAL INDICATORS", href='/GLOBAL', style = {'color': '#4e3663', 'margin-right': '14px','margin-left': '3%','margin-right': '3%',
                                                  'font-family': 'Garamond, serif','font-weight': 'bold','text-decoration': 'none'}),
            
            dcc.Link("BRAND ANALYSIS", href='/brand-analysis', style={'color': '#4e3663', 'margin-right': '14px','margin-left': '3%','margin-right': '3%',
                                                  'font-family': 'Garamond, serif','font-weight': 'bold','text-decoration': 'none'}),
            
            dcc.Link("TYPE PARFUM ANALYSIS", href='/type-analysis', style={'color': '#4e3663', 'margin-right': '14px','margin-left': '3%','margin-right': '3%',
                                                  'font-family': 'Garamond, serif','font-weight': 'bold','text-decoration': 'none'}),
        ],
        style={'display': 'flex','margin-left': '5%','margin-top': '1%',
               'width': "55%",'height': '40px','align-items': 'center',
               'border-top': '1px solid black','border-bottom': '1px solid black'})


# In[9]:


# style second page !: 

style_KPI_TItre = {'color': 'white', 'font-family': 'Garamond, serif', 'font-size': '24px', 'justify-content': 'center'}

style_KPI = {'color': '#4e3663', 'font-family': 'Garamond, serif', 'font-size': '36px', 'justify-content': 'center'}

style_KPI_Titre_block = {'vertical-align': 'middle','margin-left': '5%','margin-bottom': '3%','background-color': '#4e3663',
    'text-align': 'center','height': '60px','width': '15%','display': 'flex', 'align-items': 'center', 
                         'justify-content': 'center'}

style_KPI_block = {'vertical-align': 'middle','margin-bottom': '2%','text-align': 'center','height': '60px','width': '11%',
    'display': 'flex','align-items': 'center','justify-content': 'center', 'background-color': 'white'}
style_button = {'color': '#4e3663','display': 'inline-block','font-family': 'Garamond, serif', 'font-size': '10px',
                'margin-left': '15%', 'margin-top': '1%','background-color': 'white','height': '5%', 'width': "15%"}
style_bloq = {'align-items': 'end','flex-direction': 'row', 'margin-left': '10%', 'margin-top': '1%', 'height': '30px',
              'width': "25%", 'display': 'inline-block'}
backround = {'position': 'absolute', 'top': 0, 'bottom': 0, 'color': '#','margin': '0px', 'background_attachment': 'fixed',
          'background-image': f'url({"https://i.ibb.co/cLdmy1G/pnd.png"})','background-size': "100% 100%", 
             'height': '100vh', 'width': '100vw'}

#Elements filtres :

Type = [{'label': el, 'value': el} for el in sorted(data['type'].unique())]
brand = [{'label': el, 'value': el} for el in sorted(data['brand'].astype(str).unique())]
category = [{'label': 'Parfum For Women', 'value': 'Parfum For Women'},
            {'label': 'Parfum For Men', 'value': 'Parfum For Men'}]

#Filtres ! 
filtre_brand  = html.Div(children=[
    dcc.Dropdown(id='filtre_brand', options=brand, placeholder="Select a brand...",
                     style={'font-size': '12px', 'justify-content': 'center',
                            'border-radius': '10px', 'background-color': '#f9f9f8'})
], style={'margin-left': '5%', 'height': '20px',
              'width': '210px', 'margin-top': '2%', 'display': 'inline-block'})
filtre_type = html.Div(children=[
        dcc.Dropdown(id='filtre_type', options=Type, placeholder="Select a Type...",
                     style={'font-size': '12px', 'justify-content': 'center',
                            'border-radius': '10px', 'background-color': '#f9f9f8'})
    ], style={'margin-left': '5%', 'height': '20px',
              'width': '210px', 'margin-top': '2%', 'display': 'inline-block'})
filtre_category = html.Div(children=[
        dcc.Dropdown(id='filtre_category', options=category, placeholder="Select a category...",value='Parfum For Men',
                     style={'font-size': '12px', 'justify-content': 'center',
                            'border-radius': '10px', 'background-color': '#f9f9f8'})
    ], style={'margin-left': '5%', 'height': '20px',
              'width': '210px', 'margin-top': '2%', 'display': 'inline-block'})

Top_flop_1 = html.Div(children=[
    html.Div(children=[
        dcc.RadioItems(id='radio-filter_1',
            options=[{'label': 'TOP : ', 'value': 'TOP'}, {'label': 'FLOP : ', 'value': 'FLOP'}
            ],value='TOP',labelStyle={'display': 'block'}  
        )], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin-right': '10px'}),
    html.Div(children=[
        html.Div(children=[
            dcc.Input(id='value_input_flop_1',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'})
        ], style={'margin-bottom': '1px'}),  # Espacement entre les champs de saisie

        html.Div(children=[
            dcc.Input(id='value_input_top_1',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'}
            )])
    ], style={'display': 'inline-block', 'vertical-align': 'middle'})],
                      style={'display': 'flex', 'flex-direction': 'row','justify-content': 'end','margin-top':"2%",
                            'margin-right':'3%'}
                    )

Top_flop_2 = html.Div(children=[
    html.Div(children=[
        dcc.RadioItems(id='radio-filter_2',
            options=[{'label': 'TOP : ', 'value': 'TOP'}, {'label': 'FLOP : ', 'value': 'FLOP'}
            ],value='TOP',labelStyle={'display': 'block'}  
        )], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin-right': '10px'}),
    html.Div(children=[
        html.Div(children=[
            dcc.Input(id='value_input_flop_2',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'})
        ], style={'margin-bottom': '1px'}),  # Espacement entre les champs de saisie

        html.Div(children=[
            dcc.Input(id='value_input_top_2',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'}
            )])
    ], style={'display': 'inline-block', 'vertical-align': 'middle'})],
                      style={'display': 'flex', 'flex-direction': 'row','justify-content': 'end','margin-top':"2%",
                            'margin-right':'3%'})

Top_flop_3 = html.Div(children=[
    html.Div(children=[
        dcc.RadioItems(id='radio-filter_3',
            options=[{'label': 'TOP : ', 'value': 'TOP'}, {'label': 'FLOP : ', 'value': 'FLOP'}
            ],value='TOP',labelStyle={'display': 'block'}  
        )], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin-right': '10px'}),
    html.Div(children=[
        html.Div(children=[
            dcc.Input(id='value_input_flop_3',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'})
        ], style={'margin-bottom': '1px'}),  # Espacement entre les champs de saisie

        html.Div(children=[
            dcc.Input(id='value_input_top_3',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'}
            )])
    ], style={'display': 'inline-block', 'vertical-align': 'middle'})],
                      style={'display': 'flex', 'flex-direction': 'row','justify-content': 'end','margin-top':"2%",
                            'margin-right':'3%'})
Top_flop_4 = html.Div(children=[
    html.Div(children=[
        dcc.RadioItems(id='radio-filter_4',
            options=[{'label': 'TOP : ', 'value': 'TOP'}, {'label': 'FLOP : ', 'value': 'FLOP'}
            ],value='TOP',labelStyle={'display': 'block'}  
        )], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin-right': '10px'}),
    html.Div(children=[
        html.Div(children=[
            dcc.Input(id='value_input_flop_4',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'})
        ], style={'margin-bottom': '1px'}),  # Espacement entre les champs de saisie

        html.Div(children=[
            dcc.Input(id='value_input_top_4',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'}
            )])
    ], style={'display': 'inline-block', 'vertical-align': 'middle'})],
                      style={'display': 'flex', 'flex-direction': 'row','justify-content': 'end','margin-top':"2%",
                            'margin-right':'3%'})

Top_flop_5 = html.Div(children=[
    html.Div(children=[
        dcc.RadioItems(id='radio-filter_5',
            options=[{'label': 'TOP : ', 'value': 'TOP'}, {'label': 'FLOP : ', 'value': 'FLOP'}
            ],value='TOP',labelStyle={'display': 'block'}  
        )], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin-right': '10px'}),
    html.Div(children=[
        html.Div(children=[
            dcc.Input(id='value_input_flop_5',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'})
        ], style={'margin-bottom': '1px'}),  # Espacement entre les champs de saisie

        html.Div(children=[
            dcc.Input(id='value_input_top_5',type='number',value=10,step=5,min=5,max=300,style={'width': '50px'}
            )])
    ], style={'display': 'inline-block', 'vertical-align': 'middle'})],
                      style={'display': 'flex', 'flex-direction': 'row','justify-content': 'end','margin-top':"2%",
                            'margin-right':'3%'})


top_flop_filtre = dcc.RadioItems(
        id='radio-filter',
        options=[
            {'label': 'TOP', 'value': 'TOP'},
            {'label': 'FLOP', 'value': 'FLOP'}
        ],
        value='TOP',
        labelStyle={'display': 'inline-block'}
    )
# Composant Input pour le choix TOP ou FLOP



#Style graph : 
style_fig = {'margin-top': '1%', 'display': 'flex', 'flex-direction': 'row','display': 'inline-block','margin-right':'5%'
                  ,'background-color': '#f4c2ae','border-radius': '20px','width': 700,'height': 500,
                   'box-shadow': '0px 0px 2px rgba(0, 0, 0, 0.5)'}


# In[10]:


index_page = html.Div([
    # Graphs
   Titre,
    barr_navig,
    
   html.Div(children=[
       html.H1('Welcome to our Perfume Analysis Dashboard, dedicated to exploring market trends and product performance in the fragrance industry. This dashboard provides a comprehensive view of key KPIs, including total number of brands and types of perfumes, average product prices, stock availability, and total sales volume. Our goal is to offer insightful analysis that helps understand the impact of various factors on sales and identify strategic opportunities in this dynamic and diverse market.',
            style={'text-align': 'justify','color': '#4e3663', 'font-family': 'Garamond', 'font-size': '22px','margin-left': '5%', 'margin-top': '3%'}),
   ],
            style={ 'margin-left': '5%', 'margin-top': '5%', 'height': 'auto', 'width': '50%'}),
    

], style=backround)


# In[11]:


second_page = html.Div([
    # Graphs
    Titre,
    barr_navig,
    filtre_brand,
    filtre_type,
    filtre_category,
    
    html.Div(children=[
        # Ligne 1: Bloq 1 et Bloq 2
        html.Div(children=[
            # Bloq 1
            html.Div(children=[
                html.H1('Brand Count: ',
                        style=style_KPI_TItre)
            ], style=style_KPI_Titre_block),
            html.Div(children=[
                html.Div(data['brand'].nunique(),
                         style=style_KPI)
            ], style=style_KPI_block),
            # Bloq 2
            html.Div(children=[
                html.H1('Type Count: ',
                        style=style_KPI_TItre)
            ], style=style_KPI_Titre_block),
            html.Div(children=[
                html.Div(data['type'].nunique(),
                         style=style_KPI)
            ], style=style_KPI_block)
        ], style={'margin-top': '2%', 'display': 'flex', 'flex-direction': 'row'}),

        # Ligne 2: Bloq 3 et Bloq 4
        html.Div(children=[
            # Bloq 3
            html.Div(children=[
                html.H1('Average Price: ',
                        style=style_KPI_TItre)
            ], style=style_KPI_Titre_block),
            html.Div(children=[
                html.Div(data.loc[:, 'price'].mean().round(1),
                         style=style_KPI)
            ], style=style_KPI_block),
            # Bloq 4
            html.Div(children=[
                html.H1('Total Available: ',
                        style=style_KPI_TItre)
            ], style=style_KPI_Titre_block),
            html.Div(children=[
                html.Div(data.loc[:, 'available'].astype(int).sum(),
                         style=style_KPI)
            ], style=style_KPI_block)
        ], style={'display': 'flex', 'flex-direction': 'row'}),

        # Ligne 3: Bloq 5 et Bloq 6
        html.Div(children=[
            # Bloq 5
            html.Div(children=[
                html.H1('Total Sold: ',
                        style=style_KPI_TItre)
            ], style=style_KPI_Titre_block),
            html.Div(children=[
                html.Div(data.loc[:, 'sold'].astype(int).sum(),
                         style=style_KPI)
            ], style=style_KPI_block),
            # Bloq 6
            html.Div(children=[
                html.H1('Total Revenue: ',
                        style=style_KPI_TItre)
            ], style=style_KPI_Titre_block),
            html.Div(children=[
                html.Div((data['sold'] * data['price']).sum().round(1),
                         style=style_KPI)
            ], style=style_KPI_block)
        ], style={'display': 'flex', 'flex-direction': 'row'})
    ], style={'display': 'flex', 'flex-direction': 'column', 'margin-top': '2%'}),
], style=backround)


# In[13]:


third_page = html.Div(
    children=[
       
            Titre,
            barr_navig,
        filtre_category,
        html.Div(children=[
            html.Div(
                children=[
                    Top_flop_1,
                    html.Div(id='Sold_brand')
                ],
                style=style_fig  
            ),
            
            html.Div(
                children=[
                    Top_flop_2,
                    html.Div(id='price_mean_brand')
                ],
                style=style_fig  # Ajoutez le style ici pour ce Div
            )],
                 style={'display': 'flex', 'flex-direction': 'row','justify-content': 'center','margin-top':"2%"}),
        html.Div(children=[
        html.Div(
                children=[
                    Top_flop_4,
                    html.Div(id='graph-container')
                ],
                style=style_fig  # Ajoutez le style ici pour ce Div
            ),
        html.Div(
            children=[
                Top_flop_3,
                html.Div(id='disp_brand')
            ],
            style=style_fig  # Ajoutez le style ici pour ce Div
        )],
                 style={'display': 'flex', 'flex-direction': 'row','justify-content': 'center','margin-top':"2%"}),
        html.Div(children=[
        html.Div(
            children=[
                Top_flop_5,
                html.Div(id='CA_brand')
            ],
            style={'margin-top': '1%', 'display': 'flex', 'flex-direction': 'row','display': 'inline-block','margin-right':'5%'
                  ,'background-color': '#f4c2ae','border-radius': '20px','width': 1000,'height': 550,
                   'box-shadow': '0px 0px 2px rgba(0, 0, 0, 0.5)'} 
        )],
                 style={'display': 'flex', 'flex-direction': 'row','justify-content': 'center','margin-top':"2%"}),
    ],
    style= {'background-color': '#fbd5c6','position': 'absolute', 'top': 0, 'bottom': 0,'margin': '0px', 'background_attachment': 'fixed',
          'background-size': "140% 100%", 
             'height': '2000px', 'width': '100vw'} )
#######################

fourth_page = html.Div(
    children=[
       
            Titre,
            barr_navig,
        filtre_category,
        html.Div(children=[
            html.Div(
                children=[
                    Top_flop_1,
                    html.Div(id='Sold_brand_2')
                ],
                style=style_fig  
            ),
            
            html.Div(
                children=[
                    Top_flop_2,
                    html.Div(id='price_mean_brand_2')
                ],
                style=style_fig  # Ajoutez le style ici pour ce Div
            )],
                 style={'display': 'flex', 'flex-direction': 'row','justify-content': 'center','margin-top':"2%"}),
        html.Div(children=[
        html.Div(
                children=[
                    Top_flop_4,
                    html.Div(id='graph-container_2')
                ],
                style=style_fig  # Ajoutez le style ici pour ce Div
            ),
        html.Div(
            children=[
                Top_flop_3,
                html.Div(id='disp_brand_2')
            ],
            style=style_fig  # Ajoutez le style ici pour ce Div
        )],
                 style={'display': 'flex', 'flex-direction': 'row','justify-content': 'center','margin-top':"2%"}),
        html.Div(children=[
        html.Div(
            children=[
                Top_flop_5,
                html.Div(id='CA_brand_2')
            ],
            style={'margin-top': '1%', 'display': 'flex', 'flex-direction': 'row','display': 'inline-block','margin-right':'5%'
                  ,'background-color': '#f4c2ae','border-radius': '20px','width': 1000,'height': 550,
                   'box-shadow': '0px 0px 2px rgba(0, 0, 0, 0.5)'} 
        )],
                 style={'display': 'flex', 'flex-direction': 'row','justify-content': 'center','margin-top':"2%"}),
    ],
    style= {'background-color': '#fbd5c6','position': 'absolute', 'top': 0, 'bottom': 0,'margin': '0px', 'background_attachment': 'fixed',
          'background-size': "140% 100%", 
             'height': '2000px', 'width': '100vw'} )

    
app =JupyterDash(__name__, suppress_callback_exceptions=True)
app.title = 'Perfume Sales Analysis'

background_image_url = 'https://i.ibb.co/fqksTCQ/Nouveau-projet-3.png'  # Remplacez par l'URL de votre image

#######################################################################################################

########################################################################################################
#######################################################################################################




app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/GLOBAL':
        return second_page
    if pathname == '/brand-analysis':
        return third_page 
    if pathname == '/type-analysis':
        return fourth_page
    else:
        return index_page



########################################################################

def apply_layout(fig, title):
    fig.update_layout(
        title=title,
        title_font_color='#4a4a4a',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        width=700,  # Largeur personnalisée
        height=450,  # Hauteur personnalisée
    )
    fig.update_xaxes(
        showgrid=False, 
        linecolor='#4a4a4a',
        tickangle=-45,  # Rotation des labels pour éviter le chevauchement
        tickmode='array',  # Utilisation d'un mode de tick fixe pour un espacement contrôlé
        tickvals=None  # Ajuster automatiquement les valeurs des ticks
    )
    fig.update_yaxes(showgrid=False)
    return fig




@app.callback(
    Output('Sold_brand', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_1', 'value'),
     Input('value_input_top_1', 'value'),
     Input('value_input_flop_1', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")

    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data = filtered_data.groupby('brand')['sold'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
        
    elif top_or_flop == 'FLOP':
        top_data = filtered_data.groupby('brand')['sold'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()

    else:
        return [html.Div("Sélectionnez TOP ou FLOP"), html.Div("Sélectionnez TOP ou FLOP")]

    fig1 = px.bar(top_data , x='brand', y='sold', color_discrete_sequence=['#4e3663'],
                  labels={'brand': 'Brand', 'sold': 'Quantity'})
    fig1 = apply_layout(fig1, 'QUANTITIES SOLD BY BRAND')
    
 

    return dcc.Graph(figure=fig1)

###########################################################
@app.callback(
    Output('Sold_brand_2', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_1', 'value'),
     Input('value_input_top_1', 'value'),
     Input('value_input_flop_1', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")

    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data = filtered_data.groupby('type')['sold'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
        
    elif top_or_flop == 'FLOP':
        top_data = filtered_data.groupby('type')['sold'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()

    else:
        return html.Div("Sélectionnez TOP ou FLOP")

    fig21 = px.bar(top_data , x='type', y='sold', color_discrete_sequence=['#4e3663'],
                  labels={'brand': 'Type', 'sold': 'Quantity'})
    fig21 = apply_layout(fig21, 'QUANTITIES SOLD BY TYPE')
    
 

    return dcc.Graph(figure=fig21)

###########################################################
@app.callback(
    Output('price_mean_brand', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_2', 'value'),
     Input('value_input_top_2', 'value'),
     Input('value_input_flop_2', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")

    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data_price = filtered_data.groupby('brand')['price'].mean().sort_values(ascending=False).head(value_input_top).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_price = filtered_data.groupby('brand')['price'].mean().sort_values(ascending=False).tail(value_input_flop).reset_index()
    else:
        return [html.Div("Sélectionnez TOP ou FLOP"), html.Div("Sélectionnez TOP ou FLOP")]



    fig2 = px.bar(top_data_price, x='brand', y='price', color_discrete_sequence=['#4e3663'],
                  labels={'brand': 'Brand', 'price': 'price'})

    fig2 = apply_layout(fig2, 'AVERAGE PRICE BY BRAND')

    return dcc.Graph(figure=fig2)
####################################################
@app.callback(
    Output('price_mean_brand_2', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_2', 'value'),
     Input('value_input_top_2', 'value'),
     Input('value_input_flop_2', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")

    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data_price = filtered_data.groupby('type')['price'].mean().sort_values(ascending=False).head(value_input_top).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_price = filtered_data.groupby('type')['price'].mean().sort_values(ascending=False).tail(value_input_flop).reset_index()
    else:
        return [html.Div("Sélectionnez TOP ou FLOP"), html.Div("Sélectionnez TOP ou FLOP")]



    fig22 = px.bar(top_data_price, x='type', y='price', color_discrete_sequence=['#4e3663'],
                  labels={'brand': 'Type', 'price': 'price'})

    fig22 = apply_layout(fig22, 'AVERAGE PRICE BY TYPE')

    return dcc.Graph(figure=fig22)
####################################################
@app.callback(
    Output('disp_brand', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_3', 'value'),
     Input('value_input_top_3', 'value'),
     Input('value_input_flop_3', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")

    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data_disp = filtered_data.groupby('brand')['available'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_disp = filtered_data.groupby('brand')['available'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()
    else:
        return html.Div("Sélectionnez TOP ou FLOP")



    fig3 = px.bar(top_data_disp, x='brand', y='available', color_discrete_sequence=['#4e3663'],
                  labels={'brand': 'Brand', 'price': 'available'})

    fig3 = apply_layout(fig3, 'AVAILABLE QUANTITIES BY BRAND')

    return dcc.Graph(figure=fig3)

#######################################################
@app.callback(
    Output('disp_brand_2', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_3', 'value'),
     Input('value_input_top_3', 'value'),
     Input('value_input_flop_3', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")

    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data_disp = filtered_data.groupby('type')['available'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_disp = filtered_data.groupby('type')['available'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()
    else:
        return html.Div("Sélectionnez TOP ou FLOP")



    fig23 = px.bar(top_data_disp, x='type',y='available', color_discrete_sequence=['#4e3663'],
                  labels={'x': 'Type', 'y': 'Available'})

    fig23 = apply_layout(fig23, 'AVAILABLE QUANTITIES BY TYPE')

    return dcc.Graph(figure=fig23)

#######################################################

@app.callback(
    Output('graph-container', 'children'),
      [
     Input('radio-filter_4', 'value'),
     Input('value_input_top_4', 'value'),
     Input('value_input_flop_4', 'value')]
)
def update_graph( top_or_flop, value_input_flop, value_input_top):
    
    
    if top_or_flop == 'TOP':
        top_data_sold_men = data[data['Category']== "Parfum For Men"].groupby('brand')['sold'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
        top_data_sold_women = data[data['Category']== "Parfum For Women"].groupby('brand')['sold'].sum().reindex(top_data_sold_men['brand']).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_sold_men = data[data['Category']== "Parfum For Men"].groupby('brand')['sold'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()
        top_data_sold_women = data[data['Category']== "Parfum For Women"].groupby('brand')['sold'].sum().reindex(top_data_sold_men['brand']).reset_index()
    else:
        return html.Div("Sélectionnez TOP ou FLOP")

    fig4 = go.Figure(data=[
    go.Bar(name='Men\'s Fragrances', x=top_data_sold_men['brand'], y=top_data_sold_men['sold'], marker_color='#4e3663'),
    go.Bar(name='Women\'s Fragrances', x=top_data_sold_women['brand'], y=top_data_sold_women['sold'], marker_color='#7f8c8d')
])

    fig1 = apply_layout(fig4, 'COMPARISON OF QUANTITIES SOLD FOR MEN’S / WOMEN’S FRAGRANCES')
    return dcc.Graph(figure=fig4)
#######################################################

@app.callback(
    Output('graph-container_2', 'children'),
      [
     Input('radio-filter_4', 'value'),
     Input('value_input_top_4', 'value'),
     Input('value_input_flop_4', 'value')]
)
def update_graph( top_or_flop, value_input_flop, value_input_top):
    
    
    if top_or_flop == 'TOP':
        top_data_sold_men = data[data['Category']== "Parfum For Men"].groupby('type')['sold'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
        top_data_sold_women = data[data['Category']== "Parfum For Women"].groupby('type')['sold'].sum().reindex(top_data_sold_men['type']).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_sold_men = data[data['Category']== "Parfum For Men"].groupby('type')['sold'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()
        top_data_sold_women = data[data['Category']== "Parfum For Women"].groupby('type')['sold'].sum().reindex(top_data_sold_men['type']).reset_index()
    else:
        return html.Div("Sélectionnez TOP ou FLOP")

    fig24 = go.Figure(data=[
    go.Bar(name='Men\'s Fragrances', x=top_data_sold_men['type'], y=top_data_sold_men['sold'], marker_color='#4e3663'),
    go.Bar(name='Women\'s Fragrances', x=top_data_sold_women['type'], y=top_data_sold_women['sold'], marker_color='#7f8c8d')
])

    fig24 = apply_layout(fig24, 'COMPARISON OF QUANTITIES SOLD FOR MEN’S / WOMEN’S FRAGRANCES')
    return dcc.Graph(figure=fig24)

@app.callback(
    Output('CA_brand', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_5', 'value'),
     Input('value_input_top_5', 'value'),
     Input('value_input_flop_5', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")
    data['CA']= data['price']*data['sold']
    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data_disp = filtered_data.groupby('brand')['CA'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_disp = filtered_data.groupby('brand')['CA'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()
    else:
        return html.Div("Sélectionnez TOP ou FLOP")

    fig5 = px.bar(top_data_disp, x='brand', y='CA', color_discrete_sequence=['#4e3663'],
                  labels={'brand': 'Brand', 'price': 'available'})

    fig5.update_layout(
        title='REVENUE BY BRAND',
        title_font_color='#4a4a4a',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        width=1000,  # Largeur personnalisée
        height=450,  # Hauteur personnalisée
    )
    fig5.update_xaxes(
        showgrid=False, 
        linecolor='#4a4a4a',
        tickangle=-45,  # Rotation des labels pour éviter le chevauchement
        tickmode='array',  # Utilisation d'un mode de tick fixe pour un espacement contrôlé
        tickvals=None  # Ajuster automatiquement les valeurs des ticks
    )
    fig5.update_yaxes(showgrid=False)

    return dcc.Graph(figure=fig5)

@app.callback(
    Output('CA_brand_2', 'children'),
    [Input('filtre_category', 'value'),
     Input('radio-filter_5', 'value'),
     Input('value_input_top_5', 'value'),
     Input('value_input_flop_5', 'value')]
)
def update_graphs(category_value, top_or_flop, value_input_flop, value_input_top):
    if not category_value:
        return html.Div("Sélectionnez une catégorie")
    data['CA']= data['price']*data['sold']
    filtered_data = data[data['Category'] == category_value]
    
    if top_or_flop == 'TOP':
        top_data_disp = filtered_data.groupby('type')['CA'].sum().sort_values(ascending=False).head(value_input_top).reset_index()
    elif top_or_flop == 'FLOP':
        top_data_disp = filtered_data.groupby('type')['CA'].sum().sort_values(ascending=False).tail(value_input_flop).reset_index()
    else:
        return html.Div("Sélectionnez TOP ou FLOP")

    fig25 = px.bar(top_data_disp, x='type', y='CA', color_discrete_sequence=['#4e3663'],
                  labels={'x': 'Type', 'y': 'CA'})

    fig25.update_layout(
        title='REVENUE BY TYPE',
        title_font_color='#4a4a4a',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        width=1000,  # Largeur personnalisée
        height=450,  # Hauteur personnalisée
    )
    fig25.update_xaxes(
        showgrid=False, 
        linecolor='#4a4a4a',
        tickangle=-45,  # Rotation des labels pour éviter le chevauchement
        tickmode='array',  # Utilisation d'un mode de tick fixe pour un espacement contrôlé
        tickvals=None  # Ajuster automatiquement les valeurs des ticks
    )
    fig25.update_yaxes(showgrid=False)

    return dcc.Graph(figure=fig25)






if __name__ == '__main__':
    app.run_server(debug=True, port=2261)


# In[ ]:




