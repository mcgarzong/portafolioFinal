import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portafolio Apps IA", page_icon="💌", layout="wide")

# --- 🌊 Estilos personalizados ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #B3E5FC; /* Fondo azul claro */
    }
    .stButton>button {
        background-color: #0277BD; /* Azul fuerte */
        color: white;
        border-radius: 12px;
        border: none;
        font-size: 16px;
        padding: 0.5em 1em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #03A9F4;
        color: #fff;
        transform: scale(1.05);
    }
    h1, h2, h3, h4, h5, h6, p, div, label, span {
        color: #002147 !important; /* Azul oscuro */
    }
    .title {
        color: #001F3F;
        text-align: center;
        font-size: 42px;
        font-weight: 800;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #002147;
        font-weight: 600;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 🌟 Título principal ---
st.markdown('<div class="title">💫🫧🌟 Portafolio de Aplicaciones con Inteligencia Artificial 🌟🫧💫</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Maria Camila Garzón 💌</div>', unsafe_allow_html=True)

# --- 📚 Sidebar ---
with st.sidebar:
    st.subheader("📖 Portafolio")
    st.write("""
    💭 Este portafolio recopila las aplicaciones creadas durante el curso,
    explorando el poder de la inteligencia artificial y la creatividad. 🌟🫧
    """)

st.divider()

# --- 🧠 Lista de aplicaciones ---
apps = [
    (" Introducción", "Presentación general del portafolio.", "1.jpeg", "https://miprimeraappcami.streamlit.app/"),
    (" Interfaz texto a voz", "cuento", "2.jpeg", "https://laestrellaperdida.streamlit.app/"),
    (" Interfaz Traductor", "Convierte voz en texto (traductor).", "3.jpeg", "https://traductordecami.streamlit.app/"),
    (" Interfaz imagen texto", "Reconocimiento de imagenes", "4.jpeg", "https://ocrdecami.streamlit.app/"),
    (" Análisis de Sentimiento", "Detecta emociones en texto.", "5.jpeg", "https://sentimientotexto.streamlit.app/"),
    (" Análisis de Texto (Inglés)", "analisis ingles.", "6.jpeg", "https://textoeningles.streamlit.app/"),
    (" Análisis de Texto (Español)", "Procesamiento de lenguaje natural.", "7.jpeg", "https://textoenespanol.streamlit.app/"),
    (" Reconocimiento de Objetos", "Detección de objetos en imágenes (YOLO).", "8.jpeg", "https://visordelmundoinvisible.streamlit.app/"),
    (" Reconocimiento de Gestos", "Interpreta movimientos usando visión computacional.", "9.jpeg", "https://espejopulgar.streamlit.app/"),
    (" Chatbot (Sistema Experto)", "Sistema de conversación LLM.", "10.jpeg", "https://postresdelimon.streamlit.app/"),
    (" Interpretación de Imagen", "Análisis avanzado de imágenes con IA.", "11.jpeg", "https://exploradorvisuall.streamlit.app/"),
    (" Interfaz Táctil", "Tablero interactivo personalizado.", "12.jpeg","https://canvasvivo.streamlit.app/"),
    (" Generador de Historias", "Crea historias con inteligencia artificial.", "13.jpeg", "https://historiascreativas.streamlit.app/"),
    (" Control MQTT (Botones)", "Control de dispositivos mediante MQTT y botones.", "14.jpeg", "https://botonexplosivo.streamlit.app/"),
    (" Control MQTT (Voz)", "Control de dispositivos mediante comandos de voz.", "15.jpeg", "https://vozenescena.streamlit.app/")
]

# --- 💫 Diseño con columnas ---
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(apps):
            titulo, desc, img_url, link = apps[i + j]
            with col:
                st.image(img_url, use_container_width=True)
                st.markdown(f"### {titulo}")
                st.write(desc)
                if link:
                    st.markdown(
                        f'<a href="{link}" target="_blank"><button class="css-1q8dd3e edgvbvh1">💌 Ir a la aplicación</button></a>',
                        unsafe_allow_html=True
                    )
                st.divider()

# --- 🌈 Final ---
st.snow()
st.success("✨ ¡Gracias por explorar mi portafolio! 💙🌟🫧💫")
