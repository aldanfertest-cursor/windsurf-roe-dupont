"""
ROE DuPont Interactivo - Funcionalidad 1: Cálculo de ratios financieros básicos
Desarrollado con Streamlit, NumPy, Pandas y Plotly
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def calcular_dupont(utilidad_neta, ventas, activos_promedio, patrimonio_promedio):
    """
    Calcula los componentes del modelo DuPont y el ROE
    
    Args:
        utilidad_neta (float): Utilidad neta de la empresa
        ventas (float): Ventas totales
        activos_promedio (float): Activos totales promedio
        patrimonio_promedio (float): Patrimonio promedio
    
    Returns:
        dict: Diccionario con todos los ratios calculados
    """
    
    # Validación para evitar división por cero
    if ventas == 0 or activos_promedio == 0 or patrimonio_promedio == 0:
        return None
    
    # Cálculo de los tres componentes del modelo DuPont
    margen_neto = utilidad_neta / ventas  # Margen de rentabilidad
    rotacion_activos = ventas / activos_promedio  # Eficiencia en el uso de activos
    apalancamiento_financiero = activos_promedio / patrimonio_promedio  # Nivel de endeudamiento
    
    # Cálculo del ROE como producto de los tres factores
    roe = margen_neto * rotacion_activos * apalancamiento_financiero
    
    return {
        'margen_neto': margen_neto,
        'rotacion_activos': rotacion_activos,
        'apalancamiento_financiero': apalancamiento_financiero,
        'roe': roe,
        'utilidad_neta': utilidad_neta,
        'ventas': ventas,
        'activos_promedio': activos_promedio,
        'patrimonio_promedio': patrimonio_promedio
    }

def crear_metricas_dupont(resultados):
    """
    Crea visualización de métricas numéricas para los resultados DuPont
    
    Args:
        resultados (dict): Resultados del cálculo DuPont
    
    Returns:
        plotly.graph_objects.Figure: Gráfico con las métricas
    """
    
    # Crear subplots para mostrar las métricas principales
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('ROE Total', 'Margen Neto', 'Rotación de Activos', 'Apalancamiento'),
        specs=[[{"type": "indicator"}, {"type": "indicator"}],
               [{"type": "indicator"}, {"type": "indicator"}]]
    )
    
    # ROE Total - Métrica principal
    fig.add_trace(
        go.Indicator(
            mode="number+gauge+delta",
            value=resultados['roe'] * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "ROE (%)"},
            gauge={
                'axis': {'range': [None, 50]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 10], 'color': "lightgray"},
                    {'range': [10, 20], 'color': "gray"},
                    {'range': [20, 30], 'color': "lightblue"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 25
                }
            },
            delta={'reference': 15}
        ),
        row=1, col=1
    )
    
    # Margen Neto
    fig.add_trace(
        go.Indicator(
            mode="number+gauge",
            value=resultados['margen_neto'] * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Margen Neto (%)"},
            gauge={'axis': {'range': [None, 30]}, 'bar': {'color': "green"}}
        ),
        row=1, col=2
    )
    
    # Rotación de Activos
    fig.add_trace(
        go.Indicator(
            mode="number+gauge",
            value=resultados['rotacion_activos'],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Rotación Activos"},
            gauge={'axis': {'range': [None, 3]}, 'bar': {'color': "orange"}}
        ),
        row=2, col=1
    )
    
    # Apalancamiento Financiero
    fig.add_trace(
        go.Indicator(
            mode="number+gauge",
            value=resultados['apalancamiento_financiero'],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Apalancamiento"},
            gauge={'axis': {'range': [None, 5]}, 'bar': {'color': "purple"}}
        ),
        row=2, col=2
    )
    
    fig.update_layout(
        title="Análisis DuPont - Métricas Financieras Clave",
        height=600,
        showlegend=False
    )
    
    return fig

def main():
    """
    Función principal de la aplicación Streamlit
    """
    
    # Configuración de la página
    st.set_page_config(
        page_title="ROE DuPont Interactivo",
        page_icon="📊",
        layout="wide"
    )
    
    # Título principal
    st.title("🏦 ROE DuPont Interactivo")
    st.markdown("### Análisis de Rentabilidad mediante el Modelo DuPont")
    st.markdown("---")
    
    # Sidebar para entrada de datos
    st.sidebar.header("📈 Parámetros Financieros")
    st.sidebar.markdown("Ajuste las variables financieras para analizar el ROE:")
    
    # Sliders para las 4 variables principales (uno por renglón)
    utilidad_neta = st.sidebar.slider(
        "Utilidad Neta ($)",
        min_value=0,
        max_value=1000000,
        value=100000,
        step=10000,
        help="Utilidad neta después de impuestos"
    )
    
    ventas = st.sidebar.slider(
        "Ventas ($)",
        min_value=0,
        max_value=5000000,
        value=1000000,
        step=50000,
        help="Ventas totales del período"
    )
    
    activos_promedio = st.sidebar.slider(
        "Activos Promedio ($)",
        min_value=0,
        max_value=5000000,
        value=800000,
        step=50000,
        help="Valor promedio de activos totales"
    )
    
    patrimonio_promedio = st.sidebar.slider(
        "Patrimonio Promedio ($)",
        min_value=0,
        max_value=2000000,
        value=400000,
        step=25000,
        help="Valor promedio del patrimonio neto"
    )
    
    # Calcular resultados del modelo DuPont
    resultados = calcular_dupont(utilidad_neta, ventas, activos_promedio, patrimonio_promedio)
    
    if resultados is None:
        st.error("⚠️ Error: Las variables de entrada no pueden ser cero. Por favor ajuste los valores.")
        return
    
    # Información adicional
    with st.expander("📚 ¿Qué es el Modelo DuPont?"):
        st.markdown("""
        **El Modelo DuPont** es un framework de análisis financiero que descompone el Return on Equity (ROE) 
        en tres componentes fundamentales:
        
        1. **Margen Neto**: Mide la rentabilidad de las ventas (Utilidad Neta / Ventas)
        2. **Rotación de Activos**: Mide la eficiencia en el uso de activos (Ventas / Activos)
        3. **Apalancamiento Financiero**: Mide el nivel de endeudamiento (Activos / Patrimonio)
        
        Esta descomposición permite identificar qué factores están impulsando la rentabilidad 
        y dónde se pueden implementar mejoras.
        """)
    
    # Mostrar resultados principales
    st.header("📊 Resultados del Análisis DuPont")
    
    # Métricas principales en formato de tarjetas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="ROE Total",
            value=f"{resultados['roe']:.2%}",
            delta=f"{resultados['roe']:.2%}"
        )
    
    with col2:
        st.metric(
            label="Margen Neto",
            value=f"{resultados['margen_neto']:.2%}"
        )
    
    with col3:
        st.metric(
            label="Rotación Activos",
            value=f"{resultados['rotacion_activos']:.2f}x"
        )
    
    with col4:
        st.metric(
            label="Apalancamiento",
            value=f"{resultados['apalancamiento_financiero']:.2f}x"
        )

if __name__ == "__main__":
    main()
