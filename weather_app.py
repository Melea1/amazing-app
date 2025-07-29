import streamlit as st
import requests

API_KEY = "e8eaffccec0b4a8ab58184840252907"  # Remplace ici par ta vraie clé

st.title("🌤️ Application Météo")
st.write("Obtiens la météo actuelle d'une ville 🌍")

ville = st.text_input("Entre le nom de la ville", "Paris")

if st.button("Afficher la météo"):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": ville,
            "appid": API_KEY,
            "units": "metric",
            "lang": "fr"
        }
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            st.subheader(f"Météo à {ville.capitalize()}")
            st.write(f"🌡️ Température : {data['main']['temp']}°C")
            st.write(f"💧 Humidité : {data['main']['humidity']}%")
            st.write(f"🌬️ Vent : {data['wind']['speed']} m/s")
            st.write(f"📖 Description : {data['weather'][0]['description'].capitalize()}")
        else:
            st.error(f"Erreur : {data['message'].capitalize()}")
    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")
