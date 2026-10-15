# -*- coding: utf-8 -*-
"""
conversor de meri
"""
import streamlit as st

st.title("Conversor de euros a pesos colombianos :)")

valor = st.number_input("introduce la cantidad:", value = 0.00)
unidad_origen = st.selectbox("De: ", ["euros", "pesos colomb."])
unidad_destino = st.selectbox("A: ", ["euros", "pesos colomb."])

def convertir (val, origen, destino):
    if origen == "euros" and destino == "pesos colomb.":
        return val *3569.9
    elif origen == "pesos colomb." and destino == "euros":
        return val / 3569.9
    else:
        return val
      
if st.button("convertir"):
        resultado = convertir(valor, unidad_origen, unidad_destino)
        st.success(f"vienen siendo {resultado: .2f}")
        