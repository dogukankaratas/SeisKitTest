import dash_mantine_components as dmc
from dash import html, callback, Input, Output, State
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

def get_icon(icon, url):
    return dmc.Anchor(href=url, children=[
        DashIconify(icon=icon, width=24, height=24)
    ], className="m-2", target='_blank')
asdasd
navbarComponent = dmc.Header(
    id="navbarComponent",
    height=70,
    p="md",
    className="bg-dark border-bottom border-secondary",
    children=[
        dbc.Container(fluid=True, children=[
            dbc.Row(
                dbc.Col(
                    html.Div(
                        className="d-flex flex-wrap align-items-center justify-content-between",
                        style={"width": "100%", "textAlign": "center"},
                        children=[
                            dmc.Anchor(href="/home", children=[html.Img(src='assets/static/lightLogo.png', height='20px', style={'marginBottom': '5px'}, id="logo")]),
                            html.Div(
                                className="d-none d-md-flex justify-content-between align-items-center", 
                                children=[
                                    dmc.Anchor(href="/apps", children=["Applications"], className="text-white fs-6 me-4", id="appsLabel"),
                                    dmc.Anchor(href="/blog", children=["Blog"], className="text-white fs-6 mx-4", id="blogLabel"),
                                    dmc.Anchor(href="/eqmap", children=["Earthquake Map"], className="text-white fs-6 ms-4", id="eqMapLabel"),
                                ],
                            ),
                            html.Div(
                                className="d-flex align-items-center",
                                children=[
                                    get_icon("mdi:github", "https://github.com/dogukankaratas/SeisKit"),
                                    get_icon("mdi:slack", "https://join.slack.com/t/seiskit/shared_invite/zt-2bb7zi6f4-d6E~TJ9QmBfNutV6bEmNHA"),
                                    html.Div(
                                        className="d-none d-md-flex align-items-center ms-2 me-4",
                                        children=[
                                            dmc.Switch(
                                                offLabel=DashIconify(icon="radix-icons:moon", width=20),
                                                onLabel=DashIconify(icon="radix-icons:sun", width=20),
                                                size="md",
                                                id='themeSwitch',
                                                className='mt-2'
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            html.Link(rel='stylesheet', href= dbc.themes.BOOTSTRAP, id='themeStylesheet'),
                            
                        ]
                    ), width=12
                )
            )
        ])
    ]
)

footerComponent = dmc.Footer(
    id = 'footerComponent',
    height=75,
    fixed=True,
    children=[
        dmc.Group(
    [
        dmc.Anchor(
                    href="https://www.linkedin.com/in/dogukankaratas/",
                    target='_blank',
                    children=[ 
                       dmc.ActionIcon(DashIconify(icon="icomoon-free:linkedin"), color="gray")
                    ]
                ),
        dmc.Anchor(
                    href="https://github.com/dogukankaratas/SeisKit",
                    target='_blank',
                    children=[ 
                       dmc.ActionIcon(DashIconify(icon="fa6-brands:github"), color="gray")
                    ]
                ),
        dmc.Anchor(
                    href="https://join.slack.com/t/seiskit/shared_invite/zt-2bb7zi6f4-d6E~TJ9QmBfNutV6bEmNHA",
                    target='_blank',
                    children=[ 
                       dmc.ActionIcon(DashIconify(icon="fa6-brands:slack"), color="gray")
                    ]
                )
    ], style={"display": "flex", "justify-content": "center", "margin": "10px"}
    ),
    dmc.Text("SeisKit © 2024", color="gray", align="center"),
    ],
    style={"backgroundColor": "#222222", "border-color": "#333333"},
)

@callback(
    Output('themeStore', 'data'),
    [Input('themeSwitch', 'checked')],
)
def toggle_theme(is_dark):
    return is_dark

@callback(
    Output('themeSwitch', 'checked'),
    [Input('url', 'pathname')],
    State('themeStore', 'data')
)
def updateSwitchOnLoad(pathname, stored_theme):
    if stored_theme is not None:
        return stored_theme
    return False
        
@callback(
    [
        Output('navbarComponent', 'className'),
        Output('appsLabel', 'className'),
        Output('blogLabel', 'className'),
        Output('eqMapLabel', 'className'),
        Output('themeStylesheet', 'href'),
        Output('logo', 'src'),
    ],
    [
        Input('url', 'pathname'),
        Input('themeSwitch', 'checked')
    ],
    State('themeStore', 'data')
)
def initialize_theme(_, is_dark, storedTheme):
    if is_dark is None and storedTheme is not None:
        is_dark = storedTheme
    
    if is_dark:
        return [
            "bg-litera border-bottom border-secondary",
            "text-black small me-4",
            "text-black small mx-4",
            "text-black small ms-4",
            dbc.themes.SANDSTONE,
            'assets/static/lightLogo.png',
        ]
    else:
        return [
            "bg-dark border-bottom border-secondary",
            "text-white fs-6 me-4",
            "text-white fs-6 mx-4",
            "text-white fs-6 ms-4",
            dbc.themes.DARKLY,
            'assets/static/darkLogo.png',
        ]
        

@callback(
    Output('footerComponent', 'style'),
    Input('url', 'pathname'),
    Input('themeSwitch', 'checked'),
    State('themeStore', 'data'),
)
def theme_store(_,is_dark, storedTheme):
    if is_dark is None and storedTheme is not None:
        is_dark = storedTheme
        
    if is_dark:
        return {"backgroundColor": "white", "border-color": "lightGray"}
    else:
        return {"backgroundColor": "#222222", "border-color": "#333333"}

