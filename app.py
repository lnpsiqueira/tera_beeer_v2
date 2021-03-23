import streamlit as st
import pandas as pd
from streamlit.hashing import _CodeHasher
from data.create_data import create_table
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import smtplib
import pyscreenshot as ImageGrab

st.set_page_config(layout="wide")
                                  

try:
    # Before Streamlit 0.65
    from streamlit.ReportThread import get_report_ctx
    from streamlit.server.Server import Server
except ModuleNotFoundError:
    # After Streamlit 0.65
    from streamlit.report_thread import get_report_ctx
    from streamlit.server.server import Server


print('1')
def main():
    state = _get_state()
    pages = {
        "Pesquisa": display_pesquisa,
        "Sugestões": display_sugestoes,
    }

    st.sidebar.title("TeraBeer :beer:")
    
    # if st.button('Iniciar Pesquisa'):
    #     global page 
    #     page = 'Pesquisa'
    #     pages[page](state)
    #     print(2)
    page = st.sidebar.selectbox("Selecione uma opção", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page](state)
    print(page)
    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()

def display_pesquisa(state):
    
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown(""" <style>div[role="radiogroup"] >  :first-child{display: none !important;}</style>""",
                unsafe_allow_html=True)
  
    st.title(':pencil: Pesquisa')
    feat_paladar = {}
    st.subheader('Qual a sua opinião sobre os alimentos abaixo?')
    st.text('Para opções com mais de um alimento, caso goste de pelo menos um, escolha a opção "Gosto".')
    feat_paladar['Alimento Chocolate amargo'] =  st.radio('Chocolate 70% cacau', ['', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Beringela'] =  st.radio('Beringela', ['', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Folhas escuras'] =  st.radio('Rúcula/escarola/espinafre', ['', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Mel'] =  st.radio('Mel', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Chocolate ao leite'] =  st.radio('Chocolate ao leite', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Oreo'] =  st.radio('Oreo/cookies', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Salgadinho'] =  st.radio('Ruffles/salgadinho', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Tomate'] =  st.radio('Tomate/ketchup', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Margherita'] =  st.radio('Margherita', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Limonada'] =  st.radio('Limonada/caipirinha', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Laranja'] =  st.radio('Suco de laranja', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Maracujá'] =  st.radio('Suco de maracujá', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Tangerina'] =  st.radio('Mexerica/tangerina', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Pimenta'] =  st.radio('Pimentas/especiarias', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Cravo'] =  st.radio('Cravo', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Banana'] =  st.radio('Banana', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Gengibre'] =  st.radio('Gengibre', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Canela'] =  st.radio('Canela', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Bacon'] =  st.radio('Bacon/lombo defumado', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Alimento Café'] =  st.radio('Café sem açúcar', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
       
    st.subheader('Qual a sua opinião sobre os seguintes estilos de cerveja?')
    feat_paladar['Cerveja Pilsen'] =  st.radio('Pilsen/Lager', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Blonde'] =  st.radio('Golden Ale/Blonde Ale', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Trigo'] =  st.radio('Trigo (Weiss)', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja APA'] =  st.radio('American Pale Ale (APA)', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja IPA'] =  st.radio('India Pale Ale (IPA)', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Session IPA'] =  st.radio('Session IPA', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja NEIPA'] =  st.radio('New England IPA/Juicy IPA', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Porter'] =  st.radio('Porter/Stout', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Malzbier'] =  st.radio('Dunkel/Malzbier', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Witbier'] =  st.radio('Witbier', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Sour'] =  st.radio('Fruit Beer/Sour', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja RIS'] =  st.radio('Russian Imperial Stout/Pastry Stout', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])
    feat_paladar['Cerveja Lambic'] =  st.radio('Lambic', [' ', 'Gosto', 'Não gosto', 'Indiferente', 'Desconheço'])

    
    if st.button('Sugestões'):
        df_paladar = pd.DataFrame([feat_paladar])
        st.dataframe(df_paladar)
        df_paladar.to_csv('./data/teste.csv')
        print(df_paladar)
    
        
        with st.spinner(text = 'Por favor aguarde, estamos analisando...'):
            time.sleep(5)
            st.success('Pronto, já pode ir para pagina de Sugestoes')
        print(1)
 

def display_sugestoes(state):
    
    st.title(':beer: Sugestões')
    
    df_cervejas = create_table()
    estilos = df_cervejas['estilo'].unique()
    
    estilo1 = st.sidebar.selectbox('Estilo 01:', estilos)
    #estilo2 = st.sidebar.selectbox('Estilo 02:', estilos, index = 5)
    #estilo3 = st.sidebar.selectbox('Estilo 03:', estilos, index = 9)
    

    df_sugestao = df_cervejas.loc[df_cervejas['estilo']==estilo1]
    df_sugestao.drop(['estilo'], axis = 1, inplace = True)
        
    # st.dataframe(df_sugestao)
    ### Opções para primeiro estilo
    tres_opcoes = df_sugestao.sample(n=3)
    tres_opcoes.reset_index(drop = True, inplace = True)
    
    st.dataframe(tres_opcoes.iloc[:,:4].style.set_precision(2))

    
    st.subheader(estilo1)
    st.text_area('',tres_opcoes.iloc[0][6])
    
    c1, c2, c3, = st.beta_columns((1, 1, 1))
    
    with c1:  ### Opçao 01
        file = './fig/' + tres_opcoes.iloc[0][7]
        st.image(file)
        st.markdown("##### Cerveja:")
        st.subheader(tres_opcoes.iloc[0][0])
        st.markdown("##### Cervejaria")
        st.subheader(tres_opcoes.iloc[0][1])
        st.markdown('##### ABV:')
        st.subheader(tres_opcoes.iloc[0][2])
        st.markdown('##### IBU:')
        st.subheader(tres_opcoes.iloc[0][3])
    
    with c2:      ### Opçao 02  
        file = './fig/' + tres_opcoes.iloc[1][7]
        st.image(file)
        st.markdown("##### Cerveja:")
        st.subheader(tres_opcoes.iloc[1][0])
        st.markdown("##### Cervejaria:")
        st.subheader(tres_opcoes.iloc[1][1])
        st.markdown('##### ABV:')
        st.subheader(tres_opcoes.iloc[1][2])
        st.markdown('##### IBU:')
        st.subheader(tres_opcoes.iloc[1][3])
    
    with c3:   ### Opçao 02
        file = './fig/' + tres_opcoes.iloc[2][7]
        st.image(file)
        st.markdown("##### Cerveja:")
        st.subheader(tres_opcoes.iloc[2][0])
        st.markdown("##### Cervejaria:")
        st.subheader(tres_opcoes.iloc[2][1])
        st.markdown('##### ABV:')
        st.subheader(tres_opcoes.iloc[2][2])
        st.markdown('##### IBU:')
        st.subheader(tres_opcoes.iloc[2][3])
        
        
    email = st.text_input('Para receber sugestoões entre com seu email:')
    if st.button('Enviar por email'):
        screenshot()
        enviar_email(email)
        
       
        
class _SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)
        
    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value
    
    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()
    
    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False
        
        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    
    return session_info.session


def _get_state(hash_funcs=None):
    session = _get_session()

    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = _SessionState(session, hash_funcs)

    return session._custom_session_state

def screenshot():
    
    sugestao = ImageGrab.grab(bbox=(390, 140, 1850, 890))
    # sugestao = pyautogui.screenshot()
    sugestao.save('D:/Downloads/screenshot/sugestao.png')
        
def enviar_email(email):
    
    # Define the source and target email address.
    strFrom = 'sugestoesterabeer@gmail.com'
    sender_pass = '******'
    strTo = email
            
           
    # Create an instance of MIMEMultipart object, pass 'related' as the constructor parameter.
    menssage = MIMEMultipart('related')
    menssage['Subject'] = 'Recomendações TeraBeer'
    menssage['From'] = strFrom
    menssage['To'] = strTo
            
    msgText = MIMEText('<b>Esta é a sua recomendação:<br><img src="cid:image1"><br>', 'html')
    # Attach the above html content MIMEText object to the menssage object.
    menssage.attach(msgText)
    fp = open('D:/Downloads/screenshot/sugestao.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
            
    msgImage.add_header('Content-ID', '<image1>')
    menssage.attach(msgImage)

            
    # Create an smtplib.SMTP object to send the email.
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls() #enable security
    smtp.login(strFrom, sender_pass)
    smtp.sendmail(strFrom, strTo, menssage.as_string())
    smtp.quit()


if __name__ == "__main__":
    main()
