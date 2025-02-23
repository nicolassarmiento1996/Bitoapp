import streamlit as st

# ------------------------------------------------------------------
# 1. CONFIGURACIÓN BÁSICA
# ------------------------------------------------------------------
st.set_page_config(page_title="Bito App", layout="centered", initial_sidebar_state="collapsed")

CUSTOM_CSS = """
<style>
html, body {
    margin: 0; padding: 0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(45deg, #ff9f9f, #ffc6c6);
    overflow-x: hidden;
}

#MainMenu, header, footer {
    visibility: hidden;
    height: 0;
}

.main-container {
    max-width: 400px;
    margin: auto;
    background-color: #ffffffdd;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h1, h2, h3 {
    text-align: center;
    color: #333;
    margin-bottom: 16px;
}

.stButton > button {
    background: #646cff;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
    margin: 8px 0;
    font-weight: 600;
    cursor: pointer;
}
.stButton > button:hover {
    background: #7b80ff;
}

.css-1n76uvr input {
    border-radius: 8px !important;
    border: 1px solid #ccc !important;
}

.gender-container {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
}

.gender-option {
    width: 100px;
    height: 120px;
    background: #f5f5f5;
    border-radius: 12px;
    display: flex; 
    flex-direction: column; 
    align-items: center; 
    justify-content: center;
    cursor: pointer;
    margin: 8px;
    border: 2px solid transparent;
    transition: border 0.2s ease;
}
.gender-option:hover {
    border: 2px solid #646cff;
}

.priority-item {
    background-color: #f5f5f5;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 6px;
    cursor: grab;
}

.medal-img {
    width: 120px;
    margin: 20px auto;
    display: block;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Manejo de estado para la navegación
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ------------------------------------------------------------------
# 2. FUNCIONES PARA CADA PANTALLA
# ------------------------------------------------------------------
def welcome():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.image("assets/welcome_hero.jpg", use_container_width=True)
    st.markdown("<h1>Bienvenido a Bito</h1>", unsafe_allow_html=True)
    st.write("Potencia tu vida con mejores hábitos. En el cómo hacerlo ayudamos nosotros.")
    if st.button("Regístrate y empieza tu camino"):
        st.session_state.page = "login"
    st.markdown("</div>", unsafe_allow_html=True)

def login():
    st
