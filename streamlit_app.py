
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
    st.markdown(f"**{msg['role'].capitalize()}:**\n\n{msg['content']}")

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Tu mensaje:")
    submitted = st.form_submit_button("Enviar")

if submitted and user_input:
    st.session_state.messages.append({"role": "usuario", "content": user_input})
    msg = user_input.strip().lower()
    estado = st.session_state.state
    user_data = st.session_state.user_data

    def show_menu():
        return (
            "¿En qué te gustaría que te apoye hoy?\n"
            "1. Conocer nuestros servicios\n"
            "2. Agendar asesoría gratuita\n"
            "3. Ver promociones y precios\n"
            "4. Descargar contenidos útiles\n"
            "5. Hablar con un asesor humano\n"
            "5. Hablar con un asesor humano\n"
            "Digita: 1,2,3,4 o 5 segun lo que necesitas"
        )

    if msg in ["menu", "inicio"]:
        st.session_state.state = "inicio"
        bot_reply = show_menu()

    elif estado == "inicio":
        if msg == "1":
            st.session_state.state = "menu_servicios"
            bot_reply = (
                "Ofrecemos servicios de marketing digital especializado, incluyendo:\n"
                "- Campañas en Meta, Google, TikTok, X\n"
                "- Diseño web optimizado (SEO/SEM)\n"
                "- Fotografía y video profesional\n"
                "- Branding y posicionamiento digital\n"
                "- COFEPRIS (salud)\n"
                "- Consultoría comercial y ventas\n"
                "\n¿Te gustaría agendar una asesoría gratuita?\n1. Sí, agendar asesoría\n2. Volver al menú principal"
            )
        elif msg == "2":
            st.session_state.state = "esperando_nombre"
            bot_reply = "¡Perfecto! Por favor, dime tu nombre completo:"
        elif msg == "3":
            st.session_state.state = "menu_promociones"
            bot_reply = (
                "Nuestros paquetes inician desde $4,500 MXN e incluyen:\n"
                "- 8 reels + 4 diseños de imagen\n"
                "- Sesión de foto y video\n"
                "- 2 campañas pagadas (Meta/Google)\n"
                "- Optimización de plataformas (Meta, TikTok, Google)\n"
                "\n¿Deseas más información?\n1. Sí, quiero más info\n2. Volver al menú principal"
            )
        elif msg == "4":
            st.session_state.state = "menu_contenidos"
            bot_reply = (
                "Aquí tienes algunos contenidos que pueden ayudarte:\n"
                "📘 eBook gratuito: https://drive.google.com/file/d/1VCqn50grfCdWAGcXYJmBhcIilgbrSdE4/view\n"
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
            "✅ ¡Listo! Hemos registrado tu solicitud de asesoría:\n"
            f"📌 Nombre: {user_data.get('nombre')}\n"
            f"📞 Teléfono: {user_data.get('telefono')}\n"
            f"✉️ Email: {user_data.get('email')}\n"
            f"🏢 Giro: {user_data.get('giro')}\n"
            f"📅 Fecha deseada: {user_data.get('fecha')}\n\n"
            "Un asesor te contactará pronto por WhatsApp para confirmarla.\n"
            "\nGracias por tu interés en Motor en Ventas. ¡Empieza hoy mismo a vender más y mejor! 🚀"
        )

    elif estado == "esperando_contacto":
        bot_reply = "Gracias. Hemos recibido tus datos. Un asesor se pondrá en contacto contigo. ¿Deseas volver al menú?"

    else:
        bot_reply = "No entendí tu mensaje. Escribe 'menu' para ver opciones."

    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    st.rerun()
