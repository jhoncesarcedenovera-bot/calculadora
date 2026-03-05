import streamlit as st

st.set_page_config(page_title="Calculadora de Rebajas", page_icon="💸")

st.title("💸 Calculadora de Rebajas")
st.write("Calcula el precio final y descubre qué tan bueno es el descuento.")

# Entradas
precio_original = st.number_input("Precio original (€)", min_value=0.0, step=1.0)
descuento = st.slider("Porcentaje de descuento (%)", 0, 100, 10)

# Cálculo
precio_final = precio_original * (1 - descuento / 100)

# Evaluación del descuento con colores
def evaluar_descuento(d):
    if d < 10:
        return "😐 Descuento bajo", "gray"
    elif d < 25:
        return "🙂 Descuento aceptable", "blue"
    elif d < 50:
        return "🔥 Buen descuento", "green"
    elif d < 70:
        return "💥 Gran oferta", "orange"
    else:
        return "🤑 Descuento increíble", "red"

if precio_original > 0:

    texto, color = evaluar_descuento(descuento)

    st.subheader("Resultado")
