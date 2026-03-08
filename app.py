import streamlit as st

st.title("🛍️ Calculadora de Rebajas")

st.write("Calcula el precio final después de aplicar un descuento.")

# Inputs
precio_original = st.number_input("Precio original (€)", min_value=0.0, step=0.5)
descuento = st.slider("Porcentaje de descuento (%)", 0, 100, 10)

# Mostrar fórmula
st.subheader("📐 Fórmula utilizada")
st.latex(r"Precio\ final = Precio\ original \times (1 - \frac{Descuento}{100})")

# Cálculo
precio_final = precio_original * (1 - descuento / 100)
ahorro = precio_original - precio_final

# Botón
if st.button("Calcular rebaja"):
    
    st.subheader("Resultado")

    st.write(f"💰 Precio original: **{precio_original:.2f} €**")
    st.write(f"🏷️ Descuento: **{descuento}%**")
    st.write(f"💸 Ahorras: **{ahorro:.2f} €**")

    st.success(f"✅ Precio final: **{precio_final:.2f} €**")

    # Feedback
    if descuento == 0:
        st.info("No hay descuento aplicado.")
    elif descuento < 30:
        st.warning("Descuento pequeño, quizá haya mejores ofertas.")
    elif descuento < 60:
        st.info("Buen descuento 👍")
    else:
        st.success("¡Gran oferta! 🔥")
