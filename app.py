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
        # Simplemente cambiamos la página y dejamos que Streamlit refresque
        st.session_state.page = "login"
    
    st.markdown("</div>", unsafe_allow_html=True)

def login():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Inicia tu camino</h2>", unsafe_allow_html=True)
    
    email = st.text_input("Correo")
    password = st.text_input("Contraseña", type="password")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Continuar con Google", key="google"):
            pass
    with c2:
        if st.button("Continuar con Facebook", key="facebook"):
            pass

    st.write("Al registrarte, aceptas nuestros T&C.")
    
    if st.button("Siguiente"):
        st.session_state.page = "register"
    
    st.markdown("</div>", unsafe_allow_html=True)

def register():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Crear una cuenta</h2>", unsafe_allow_html=True)
    
    st.text_input("Tu nombre")
    st.text_input("Tu número de teléfono")
    st.text_input("¿Cuándo naciste?", placeholder="dd/mm/aaaa")
    
    if st.button("Siguiente"):
        st.session_state.page = "gender"
    
    st.markdown("</div>", unsafe_allow_html=True)

def gender():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Escoge tu género</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='gender-container'>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Hombre"):
            st.session_state.page = "questions"
    with col2:
        if st.button("Mujer"):
            st.session_state.page = "questions"
    with col3:
        if st.button("No binario"):
            st.session_state.page = "questions"
    with col4:
        if st.button("Prefiero no decirlo"):
            st.session_state.page = "questions"
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def questions():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Queremos conocerte un poco mejor</h2>", unsafe_allow_html=True)
    
    st.checkbox("Salud Física (3 preguntas por completar)")
    st.checkbox("Salud Mental (3 preguntas por completar)")
    st.checkbox("Propósito (4 preguntas por completar)")
    
    if st.button("Siguiente"):
        st.session_state.page = "priorities"
    
    st.markdown("</div>", unsafe_allow_html=True)

def priorities():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Ordena tus prioridades para Bito</h2>", unsafe_allow_html=True)
    st.write("Arrastra y suelta para ordenar tus prioridades (simulado)")
    
    st.markdown("<div class='priority-item'>Salud Física</div>", unsafe_allow_html=True)
    st.markdown("<div class='priority-item'>Vinculación emocional</div>", unsafe_allow_html=True)
    st.markdown("<div class='priority-item'>Balance espiritual</div>", unsafe_allow_html=True)
    st.markdown("<div class='priority-item'>Crecimiento profesional</div>", unsafe_allow_html=True)
    
    if st.button("Siguiente"):
        st.session_state.page = "achievement"
    
    st.markdown("</div>", unsafe_allow_html=True)

def achievement():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2>¡Excelente!</h2>", unsafe_allow_html=True)
    st.write("Ya has completado el primer reto.")
    
    st.image("assets/medal.png", use_container_width=False, caption="Tu medalla de logro", output_format="PNG", width=120)
    st.write("Dar el primer paso es difícil, pero lo lograste. ¡Continúa con más retos!")
    
    if st.button("Reclamar medalla"):
        st.session_state.page = "bito_info"
    
    st.markdown("</div>", unsafe_allow_html=True)

def bito_info():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2>¿Qué es Bito?</h2>", unsafe_allow_html=True)
    st.write("Bito es una plataforma de bienestar que te ayuda a conquistar tu destino a través de hábitos y el poder de una comunidad real de apoyo.")
    
    if st.button("Ir a tu Santuario"):
        st.write("Redirigiendo al Dashboard...")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------
# 3. FLUJO PRINCIPAL
# ------------------------------------------------------------------
def main():
    page = st.session_state.page
    
    if page == "welcome":
        welcome()
    elif page == "login":
        login()
    elif page == "register":
        register()
    elif page == "gender":
        gender()
    elif page == "questions":
        questions()
    elif page == "priorities":
        priorities()
    elif page == "achievement":
        achievement()
    elif page == "bito_info":
        bito_info()

if __name__ == "__main__":
    main()
