import streamlit as st
import pandas as pd


# Configuración inicial
st.set_page_config(page_title="Cálculo de Calibre de Conductores", layout="wide")
st.title("Cálculo de Calibre de Conductores según Nom-sede-2012")

# Tablas estáticas
#tabla_temp = pd.DataFrame({
tabla_310_15_b_3_c = pd.DataFrame({
    "D_suelo_mm_T": [13, 90, 300, 900],
    "Sum_Temp": [33, 22, 17, 14]
})

#tabla_temp_corr = pd.DataFrame({
tabla_310_15_b_2_a = pd.DataFrame({
    "T_amb_corr_T": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    "60C": [1.29, 1.22, 1.15, 1.08, 1, 0.91, 0.82, 0.71, 0.58, 0.41, 0, 0, 0, 0, 0, 0],
    "75C": [1.2, 1.15, 1.11, 1.05, 1, 0.94, 0.88, 0.82, 0.75, 0.67, 0.58, 0.47, 0.33, 0, 0, 0],
    "90C": [1.15, 1.12, 1.08, 1.04, 1, 0.96, 0.91, 0.87, 0.82, 0.76, 0.71, 0.65, 0.58, 0.5, 0.41, 0.29]
})

 #tabla_can = pd.DataFrame({
tabla_310_15_b_3_a = pd.DataFrame({
    "n_cond_can_T": [3, 6, 9, 20, 30, 40, 41],
    "FC_Can": [1, 0.8, 0.7, 0.5, 0.45, 0.4, 0.35]
})

#tabla_cobre = pd.DataFrame({
tabla_310_15_b_16_cobre = pd.DataFrame({
    "mm2": [0.824, 1.31, 2.08, 3.31, 5.26, 8.37, 13.3, 21.2, 26.7, 33.6, 42.4, 53.49,
            67.43, 85.01, 107.2, 127, 152, 177, 203, 253, 304, 355, 380, 405, 456,
            507, 633, 760, 887, 1013],
    "60C": [0, 0, 15, 20, 30, 40, 55, 70, 85, 95, 110, 125, 145, 165, 195, 215, 240,
            260, 280, 320, 350, 385, 400, 410, 435, 455, 495, 525, 545, 555],
    "75C": [0, 0, 20, 25, 35, 50, 65, 85, 100, 115, 130, 150, 175, 200, 230, 255, 285,
            310, 335, 380, 420, 460, 475, 490, 520, 545, 590, 625, 650, 665],
    "90C": [14, 18, 25, 30, 40, 55, 75, 95, 115, 130, 145, 170, 195, 225, 260, 290, 320,
            350, 380, 430, 475, 520, 535, 555, 585, 615, 665, 705, 735, 750]
})


#tabla_aluminio = pd.DataFrame({
tabla_310_15_b_16_aluminio = pd.DataFrame({
    "mm2": [0.824, 1.31, 2.08, 3.31, 5.26, 8.37, 13.3, 21.2, 26.7, 33.6, 42.4, 53.49,
            67.43, 85.01, 107.2, 127, 152, 177, 203, 253, 304, 355, 380, 405, 456,
            507, 633, 760, 887, 1013],
    "60C": [0, 0, 0, 0, 0, 0, 40, 55, 65, 75, 85, 100, 115, 130, 150, 170, 195, 210,
            225, 260, 285, 315, 320, 330, 355, 375, 405, 435, 455, 470],
    "75C": [0, 0, 0, 0, 0, 0, 50, 65, 75, 90, 100, 120, 135, 155, 180, 205, 230, 250,
            270, 310, 340, 375, 385, 395, 425, 445, 485, 520, 545, 560],
    "90C": [0, 0, 0, 0, 0, 0, 55, 75, 85, 100, 115, 135, 150, 175, 205, 230, 260, 280,
            305, 350, 385, 425, 435, 445, 480, 500, 545, 585, 615, 630]
})


#tabla_awg = pd.DataFrame({
mm2_to_AWG = pd.DataFrame({
    "mm2": [0.824, 1.31, 2.08, 3.31, 5.26, 8.37, 13.3, 21.2, 26.7, 33.6, 42.4, 53.49,
            67.43, 85.01, 107.2, 127, 152, 177, 203, 253, 304, 355, 380, 405, 456,
            507, 633, 760, 887, 1013],
    "awg": ["18", "16", "14", "12", "10", "8", "6", "4", "3", "2", "1", "1/0",
            "2/0", "3/0", "4/0", "250", "300", "350", "400", "500", "600", "700",
            "750", "800", "900", "1000", "1250", "1500", "1750", "2000"]
})


#tabla_pe_cobre = pd.DataFrame({
tabla_250_122_cobre = pd.DataFrame({
    "Amperes": [15, 20, 60, 100, 200, 300, 400, 500, 600, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000],
    "mm2": [2.08, 3.31, 5.26, 8.37, 13.3, 21.2, 33.6, 33.6, 42.4, 53.5, 67.4, 85, 107, 127, 177, 203, 253, 355, 405]
})


#tabla_pe_aluminio = pd.DataFrame({
tabla_250_122_aluminio = pd.DataFrame({
    "Amperes": [15, 20, 60, 100, 200, 300, 400, 500, 600, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000],
    "mm2": [21.2, 21.2, 21.2, 21.2, 21.2, 33.6, 42.4, 53.5, 67.4, 85, 107, 127, 177, 203, 304, 304, 380, 608, 608]
})


# Función: amp_cable_fv
def amp_cable_fv(I_OC, T_amb, D_suel_mm, n_cond_can, TC):
    """
    Calcula la corriente máxima admisible para un conductor en un sistema fotovoltaico.

    Parámetros:
    - I_OC: Corriente de corto circuito del arreglo fotovoltaico.
    - T_amb: Temperatura ambiente promedio del lugar.
    - D_suel_mm: Distancia de la superficie al canal (en mm).
    - n_cond_can: Número de conductores en la canalización.
    - TC: Temperatura máxima soportada por el conductor (en °C).

    Retorno:
    - Corriente máxima admisible (amperios).
    """
    try:
        # Art 210-19 a)1 - Ajuste inicial de corriente
        I_OC_1 = I_OC * 1.56

        # Art 310-15 b) 3) c) - Ajustes por temperatura "sum_temp = la suma de temperatura que se le agregara a la temperatura ambiente"
        sum_temp = tabla_310_15_b_3_c.loc[
            tabla_310_15_b_3_c['D_suelo_mm_T'] >= D_suel_mm, 'Sum_Temp'
        ].iloc[0]
        T_amb_corr = T_amb + sum_temp if 0 < D_suel_mm <= 900 else T_amb

        # Factor de corrección por temperatura
        # Tabla 310-15 b) 2) a)
        #"FC_Temp= Factor de correcion de temperatura para cables a 60C, 75C o 90C"
        if tabla_310_15_b_2_a.loc[
            tabla_310_15_b_2_a['T_amb_corr_T'] >= T_amb_corr, TC
        ].empty:
            raise ValueError(f"No hay un factor de corrección válido para T={T_amb_corr}°C y TC={TC}°C")
#Tabla 310-15 b) 3) a)
#Factor de correccion por canalizacion o numeros de conductores en canalizacion

        FC_Temp = tabla_310_15_b_2_a.loc[
            tabla_310_15_b_2_a['T_amb_corr_T'] >= T_amb_corr, TC
        ].iloc[0]

        # Factor de corrección por número de conductores
        if tabla_310_15_b_3_a.loc[
            tabla_310_15_b_3_a['n_cond_can_T'] >= n_cond_can, 'FC_Can'
        ].empty:
            raise ValueError(f"No hay un factor de corrección válido para n_cond_can={n_cond_can}")

        FC_Can = tabla_310_15_b_3_a.loc[
            tabla_310_15_b_3_a['n_cond_can_T'] >= n_cond_can, 'FC_Can'
        ].iloc[0]

        # Cálculo ajustado de corriente
        I_OC_2 = (I_OC * 1.25) / (FC_Can * FC_Temp)

        # Resultado final
        return max(I_OC_1, I_OC_2)

    except Exception as e:
        raise RuntimeError(f"Error en el cálculo de la capacidad del cable: {e}")


# Función: seleccion_cable_mm2
def seleccion_cable_mm2(Amp, T, material):
    try:
        if material == "Cobre":
            mm2 = tabla_310_15_b_16_cobre.loc[tabla_310_15_b_16_cobre[T] >= Amp, 'mm2'].iloc[0]
        elif material == "Aluminio":
            mm2 = tabla_310_15_b_16_aluminio.loc[tabla_310_15_b_16_aluminio[T] >= Amp, 'mm2'].iloc[0]
        else:
            st.error("Material no válido.")
            return None
    except IndexError:
        st.error("El valor de amperaje o temperatura no está en la tabla.")
        return None
    return mm2


# Función: calibre_awg
def calibre_awg(mm2):
    try:
        awg = mm2_to_AWG.loc[mm2_to_AWG['mm2'] >= mm2, 'awg'].iloc[0]
    except IndexError:
        st.error("El valor de mm² no está en la tabla.")
        return None
    return awg


# Función: c_pe
def c_pe(Amp, material_PE):
    try:
        if material_PE == "Cobre":
            mm2_pe = tabla_250_122_cobre.loc[tabla_250_122_cobre['Amperes'] >= Amp, 'mm2'].iloc[0]
        elif material_PE == "Aluminio":
            mm2_pe = tabla_250_122_aluminio.loc[tabla_250_122_aluminio['Amperes'] >= Amp, 'mm2'].iloc[0]
        else:
            st.error("Material no válido.")
            return None
    except IndexError:
        st.error("El valor de amperaje no está en la tabla para el material seleccionado.")
        return None
    return mm2_pe

# Función para calcular el área del conductor por caida de tension
def calcular_area_conductor(L_C,V_OC, sigma, delta_v_c,Pot):

    return (2 * L_C * Pot) / (sigma * delta_v_c* V_OC)


#Funcion para determinar cual seria el valor del area al que le corresponde en la tabla mm2
def get_mm2(value):
    """
    Retorna el valor en la columna 'mm2' que es igual o mayor al valor dado.

    :param value: Valor de entrada para buscar en la tabla.
    :return: Valor de mm2 igual o mayor al dado, o None si no se encuentra.
    """
    # Filtrar los valores mayores o iguales al valor dado
    filtered = mm2_to_AWG[mm2_to_AWG['mm2'] >= value]
    # Si hay resultados, devolver el primer valor
    if not filtered.empty:
        return filtered.iloc[0]['mm2']

    # Si no hay resultados, devolver None
    return None

# Entradas del usuario
st.header("Datos de entrada")
I_OC = st.number_input("Corriente de corto circuito (I_OC)", value=18.47)
V_OC = st.number_input("Voltaje de circuito abierto (V_OC)", value=150)
T_amb = st.number_input("Temperatura ambiente (°C)", value=30)
D_suel_mm = st.number_input("Distancia canalización (mm)", value=100)
n_cond_can = st.number_input("Numero de conductores portadores de corriente", value=2)
TC = st.selectbox("Temperatura conductor portador de corriente (°C)", ["60C", "75C", "90C"])
material = st.selectbox("Material conductor de cables portadores de corriente", ["Cobre", "Aluminio"])
L_C = st.number_input("Longitud del Cable (mts)", value=30)
caida_tension = st.number_input("Caida de Tension maxima (%)", value=1)
material_PE = st.selectbox("Material conductor de cable de puesta a Tierra",["Cobre", "Aluminio"])




# Cálculo
if st.button("Calcular"):
    amp = amp_cable_fv(I_OC, T_amb, D_suel_mm, n_cond_can, TC)
    # Determinar la conductividad según el material
    sigma = 56 if material == "Cobre" else 36
    #Calcular la potencia
    Pot = I_OC * V_OC
    #Porcentaje de caida de tension
    P_CT=1


    if amp:
        #st.write(f"Amperaje corregido: {amp:.2f} A")
        mm2 = seleccion_cable_mm2(amp, TC, material)
        #Cantidad de voltaje que se puede perder por caida de tension
        DELTA_V_C = (P_CT * V_OC) / 100

        #Calculo cableado de tierra
        mm2_PE=c_pe(I_OC,material_PE)
        awg_PE=calibre_awg(mm2_PE)
        if mm2:
            awg = calibre_awg(mm2)
            S_C = get_mm2((2 * L_C * Pot) / (sigma * DELTA_V_C * V_OC))
            awg_CT=calibre_awg(S_C)
            if awg:
               st.subheader("Resultados")
            st.write(f"Corriente corregida: {amp:.2f} A")
            st.write(f"Calibre recomendado de conductores portadores de corriente CD Por Ampacidad: {awg} AWG ({mm2} mm²)")
            st.write(f"Calibre recomendado de conductores portadores de corriente CD Por Caida de Tensión: {awg_CT} AWG ({S_C} mm²) ")
            st.write(f"Calibre recomendado de conductores de PE: {awg_PE} AWG ({mm2_PE} mm²) ")
            #st.write(f"EL tamaño del conductor en AWG es: {(2 * L_C * Pot) / (sigma * DELTA_V_C * V_OC)}")


# Mostrar tablas (opcional)
if st.checkbox("Mostrar tablas de referencia"):
    st.write("Tabla de factores de corrección por temperatura:")
    st.dataframe(tabla_310_15_b_2_a)

    st.write("Tabla de factores de corrección por número de conductores:")
    st.dataframe(tabla_310_15_b_3_a)

    st.write("Tabla de calibres de conductores (Cobre):")
    st.dataframe(tabla_310_15_b_16_cobre)

    st.write("Tabla de calibres de conductores (Aluminio):")
    st.dataframe(tabla_310_15_b_16_aluminio)