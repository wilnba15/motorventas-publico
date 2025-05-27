from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Chatbot Motor en Ventas", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "state" not in st.session_state:
    st.session_state.state = "inicio"
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

st.title("🤖 Asistente Virtual - Motor en Ventas")

for msg in st.session_state.messages:
    st.markdown(f"**{msg['role'].capitalize()}:**<br>{msg['content']}", unsafe_allow_html=True)
<<<<<<< HEAD
=======



>>>>>>> f933db6907a8fb3fd7bb6ff6cd92839511003ba3

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Tu mensaje:")
    submitted = st.form_submit_button("Enviar")

if submitted and user_input:
    st.session_state.messages.append({"role": "usuario", "content": user_input})
    msg = user_input.strip().lower()
    estado = st.session_state.state
    user_data = st.session_state.user_data

<<<<<<< HEAD
    def show_menu():
        return (
            "¿En qué te gustaría que te apoye hoy?<br>"
            "1. Conocer nuestros servicios<br>"
            "2. Agendar asesoría gratuita<br>"
            "3. Ver promociones y precios<br>"
            "4. Descargar contenidos útiles<br>"
            "5. Hablar con un asesor humano<br>"
            "<br><strong>Digita:</strong> 1, 2, 3, 4 o 5 según lo que necesitas"
        )
=======
def show_menu():
    return (
        "¿En qué te gustaría que te apoye hoy?<br>"
        "1. Conocer nuestros servicios<br>"
        "2. Agendar asesoría gratuita<br>"
        "3. Ver promociones y precios<br>"
        "4. Descargar contenidos útiles<br>"
        "5. Hablar con un asesor humano<br>"
        "<br><strong>Digita:</strong> 1, 2, 3, 4 o 5 según lo que necesitas"
    )

>>>>>>> f933db6907a8fb3fd7bb6ff6cd92839511003ba3

    if msg in ["menu", "inicio"]:
        st.session_state.state = "inicio"
        bot_reply = show_menu()

    elif estado == "inicio":
        if msg == "1":
            st.session_state.state = "menu_servicios"
            bot_reply = (
                "Ofrecemos servicios de marketing digital especializado, incluyendo:<br>"
                "- Campañas en Meta, Google, TikTok, X<br>"
                "- Diseño web optimizado (SEO/SEM)<br>"
                "- Fotografía y video profesional<br>"
                "- Branding y posicionamiento digital<br>"
                "- COFEPRIS (salud)<br>"
                "- Consultoría comercial y ventas<br>"
                "<br>¿Te gustaría agendar una asesoría gratuita?<br>1. Sí, agendar asesoría<br>2. Volver al menú principal"
            )
        elif msg == "2":
            st.session_state.state = "esperando_nombre"
            bot_reply = "¡Perfecto! Por favor, dime tu nombre completo:"
        elif msg == "3":
            st.session_state.state = "menu_promociones"
            bot_reply = (
                "Nuestros paquetes inician desde $4,500 MXN e incluyen:<br>"
                "- 8 reels + 4 diseños de imagen<br>"
                "- Sesión de foto y video<br>"
                "- 2 campañas pagadas (Meta/Google)<br>"
                "- Optimización de plataformas (Meta, TikTok, Google)<br>"
                "<br>¿Deseas más información?<br>1. Sí, quiero más info<br>2. Volver al menú principal"
            )
        elif msg == "4":
            st.session_state.state = "menu_contenidos"
            bot_reply = (
                "Aquí tienes algunos contenidos que pueden ayudarte:<br>"
                "📘 eBook gratuito: https://drive.google.com/file/d/1VCqn50grfCdWAGcXYJmBhcIilgbrSdE4/view<br>"
                "🌐 Blog: https://www.motorenventas.com/"
            )
        elif msg == "5":
            st.session_state.state = "esperando_contacto"
            bot_reply = "Por favor, deja tu nombre y teléfono, y un asesor se comunicará contigo en breve."
        else:
            bot_reply = "No entendí tu mensaje. Escribe 'menu' para ver opciones."

    elif estado == "menu_servicios":
        if msg == "1":
            st.session_state.state = "esperando_nombre"
            bot_reply = "¡Perfecto! Por favor, dime tu nombre completo:"
        elif msg == "2":
            st.session_state.state = "inicio"
            bot_reply = show_menu()
        else:
            bot_reply = "Por favor responde con 1 para agendar o 2 para volver al menú."

    elif estado == "menu_promociones":
        if msg == "1":
            bot_reply = "¡Genial! Un asesor te brindará más información pronto. ¿Deseas volver al menú? (escribe 'menu')"
        elif msg == "2":
            st.session_state.state = "inicio"
            bot_reply = show_menu()
        else:
            bot_reply = "Por favor responde con 1 para más info o 2 para volver al menú."

    elif estado == "esperando_nombre":
        user_data["nombre"] = user_input
        st.session_state.state = "esperando_telefono"
        bot_reply = "Gracias. ¿Cuál es tu número de teléfono?"

    elif estado == "esperando_telefono":
        user_data["telefono"] = user_input
        st.session_state.state = "esperando_email"
        bot_reply = "Perfecto. ¿Cuál es tu correo electrónico?"

    elif estado == "esperando_email":
        user_data["email"] = user_input
        st.session_state.state = "esperando_giro"
        bot_reply = "¿Cuál es tu especialidad o giro comercial?"

    elif estado == "esperando_giro":
        user_data["giro"] = user_input
        st.session_state.state = "esperando_fecha"
        bot_reply = "¿Qué fecha y hora deseas para la asesoría?"

    elif estado == "esperando_fecha":
        user_data["fecha"] = user_input
        st.session_state.state = "final"
        bot_reply = (
            "✅ ¡Listo! Hemos registrado tu solicitud de asesoría:<br>"
            f"📌 Nombre: {user_data.get('nombre')}<br>"
            f"📞 Teléfono: {user_data.get('telefono')}<br>"
            f"✉️ Email: {user_data.get('email')}<br>"
            f"🏢 Giro: {user_data.get('giro')}<br>"
            f"📅 Fecha deseada: {user_data.get('fecha')}<br><br>"
            "Un asesor te contactará pronto por WhatsApp para confirmarla.<br>"
            "<br>Gracias por tu interés en Motor en Ventas. ¡Empieza hoy mismo a vender más y mejor! 🚀"
        )

    elif estado == "esperando_contacto":
        bot_reply = "Gracias. Hemos recibido tus datos. Un asesor se pondrá en contacto contigo. ¿Deseas volver al menú?"

    else:
        bot_reply = "No entendí tu mensaje. Escribe 'menu' para ver opciones."

    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    st.rerun()
