"""
ROE DuPont Interactivo - Funcionalidades 1, 2 y 3: 
- Funcionalidad 1: Cálculo de ratios financieros básicos
- Funcionalidad 2: Prisma 3D modelo DuPont
- Funcionalidad 3: Estados Financieros Simplificados
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

def crear_prisma_3d_dupont(resultados):
    """
    Crea un prisma tridimensional que representa visualmente el modelo DuPont
    basado en la imagen de referencia proporcionada
    
    Args:
        resultados (dict): Resultados del cálculo DuPont con margen_neto, rotacion_activos, apalancamiento_financiero
    
    Returns:
        plotly.graph_objects.Figure: Gráfico 3D del prisma DuPont
    """
    
    # Normalizar valores para visualización (escala 0-1 para mejor visualización)
    margen_normalizado = min(resultados['margen_neto'] * 5, 1.0)  # Escalar para mejor visualización
    rotacion_normalizada = min(resultados['rotacion_activos'] / 3, 1.0)  # Normalizar rotación
    apalancamiento_normalizado = min(resultados['apalancamiento_financiero'] / 4, 1.0)  # Normalizar apalancamiento
    
    # Crear prisma 3D según la imagen de referencia
    # Base del prisma (rectángulo en el plano XY) - AZUL
    base_x = [0, margen_normalizado, margen_normalizado, 0, 0]
    base_y = [0, 0, rotacion_normalizada, rotacion_normalizada, 0]
    base_z = [0, 0, 0, 0, 0]
    
    # Cara superior del prisma - ROJO (altura del apalancamiento)
    superior_x = [0, margen_normalizado, margen_normalizado, 0, 0]
    superior_y = [0, 0, rotacion_normalizada, rotacion_normalizada, 0]
    superior_z = [apalancamiento_normalizado, apalancamiento_normalizado, apalancamiento_normalizado, 
                  apalancamiento_normalizado, apalancamiento_normalizado]
    
    # Crear figura 3D
    fig = go.Figure()
    
    # Crear una sola malla para todo el prisma con color uniforme
    # Definir todos los vértices del prisma
    vertices_x = [
        0, margen_normalizado, margen_normalizado, 0,  # Base
        0, margen_normalizado, margen_normalizado, 0   # Techo
    ]
    vertices_y = [
        0, 0, rotacion_normalizada, rotacion_normalizada,  # Base
        0, 0, rotacion_normalizada, rotacion_normalizada   # Techo
    ]
    vertices_z = [
        0, 0, 0, 0,  # Base
        apalancamiento_normalizado, apalancamiento_normalizado, apalancamiento_normalizado, apalancamiento_normalizado  # Techo
    ]
    
    # Definir las caras del prisma
    i = [0, 0, 0, 0, 4, 4, 4, 4, 0, 1, 2, 3]
    j = [1, 1, 2, 3, 5, 5, 6, 7, 4, 5, 6, 7]
    k = [2, 5, 3, 7, 6, 1, 7, 3, 1, 2, 3, 0]
    
    # Crear malla única con color celeste uniforme
    fig.add_trace(go.Mesh3d(
        x=vertices_x,
        y=vertices_y,
        z=vertices_z,
        i=i,
        j=j,
        k=k,
        facecolor=['lightcyan'] * 12,
        opacity=0.4,
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Añadir aristas para mejor definición
    # Base
    fig.add_trace(go.Scatter3d(
        x=base_x, y=base_y, z=base_z,
        mode='lines',
        line=dict(color='darkblue', width=4),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Superior
    fig.add_trace(go.Scatter3d(
        x=superior_x, y=superior_y, z=superior_z,
        mode='lines',
        line=dict(color='darkblue', width=4),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Aristas verticales
    for i in range(4):
        fig.add_trace(go.Scatter3d(
            x=[base_x[i], superior_x[i]],
            y=[base_y[i], superior_y[i]],
            z=[base_z[i], superior_z[i]],
            mode='lines',
            line=dict(color='darkblue', width=2),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Configurar layout
    fig.update_layout(
        title=dict(
            text=f"<b>Prisma DuPont 3D - ROE: {resultados['roe']:.2%}</b>",
            x=0.5,
            font=dict(size=16)
        ),
        scene=dict(
            xaxis=dict(
                title=dict(text='Margen Neto', font=dict(size=14, color='black')),
                range=[0, 1],
                showgrid=True,
                gridcolor='lightgray',
                showbackground=True,
                backgroundcolor='rgba(240, 240, 240, 0.5)',
                tickfont=dict(size=12, color='black'),
                showticklabels=True
            ),
            yaxis=dict(
                title=dict(text='Rotación de Activos', font=dict(size=14, color='black')),
                range=[0, 1],
                showgrid=True,
                gridcolor='lightgray',
                showbackground=True,
                backgroundcolor='rgba(240, 240, 240, 0.5)',
                tickfont=dict(size=12, color='black'),
                showticklabels=True
            ),
            zaxis=dict(
                title=dict(text='Apalancamiento Financiero', font=dict(size=14, color='black')),
                range=[0, 1],
                showgrid=True,
                gridcolor='lightgray',
                showbackground=True,
                backgroundcolor='rgba(240, 240, 240, 0.5)',
                tickfont=dict(size=12, color='black'),
                showticklabels=True
            ),
            camera=dict(
                eye=dict(x=1.2, y=1.2, z=0.8),
                center=dict(x=0.5, y=0.5, z=0.3)
            ),
            bgcolor='white',
            aspectmode='cube'
        ),
        width=800,
        height=600,
        margin=dict(l=0, r=0, t=40, b=0),
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='black',
            borderwidth=1
        )
    )
    
    # Añadir anotación de ROE
    fig.add_annotation(
        x=0.5, y=0.5,
        xref='paper', yref='paper',
        text=f"<b>ROE = {resultados['roe']:.2%}</b><br>"
             f"Volumen del Prisma",
        showarrow=False,
        font=dict(size=14, color='black'),
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="black",
        borderwidth=2,
        align="center"
    )
    
    return fig

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

def crear_estado_resultados(ventas, gastos, utilidad_neta):
    """
    Crea un gráfico de barras horizontales para el Estado de Resultados
    según la imagen de referencia proporcionada
    
    Args:
        ventas (float): Monto de ventas totales
        gastos (float): Monto de gastos totales
        utilidad_neta (float): Monto de utilidad neta
    
    Returns:
        plotly.graph_objects.Figure: Gráfico de barras horizontales del Estado de Resultados
    """
    
    # Crear figura
    fig = go.Figure()
    
    # Datos para el gráfico según la imagen de referencia
    # Ventas: barra hacia la izquierda (negativo) - alineada por derecha
    fig.add_trace(go.Bar(
        y=['Ventas'],
        x=[-ventas],  # Negativo para alinear por derecha
        orientation='h',
        name='Ventas',
        marker=dict(color='lightblue'),
        text=[f'${ventas:,.0f}'],
        textposition='outside',
        hovertemplate='<b>Ventas</b><br>Monto: $%{abs(x):,.0f}<extra></extra>'
    ))
    
    # Gastos: barra hacia la izquierda (negativo) - alineado por derecha
    fig.add_trace(go.Bar(
        y=['Gastos'],
        x=[-gastos],  # Negativo para alinear por derecha
        orientation='h',
        name='Gastos',
        marker=dict(color='lightpink'),
        text=[f'${gastos:,.0f}'],
        textposition='outside',
        hovertemplate='<b>Gastos</b><br>Monto: $%{abs(x):,.0f}<extra></extra>'
    ))
    
    # Utilidad Neta: barra hacia la izquierda (negativo) - alineada por izquierda con Ventas
    fig.add_trace(go.Bar(
        y=['Utilidad Neta'],
        x=[-utilidad_neta],  # Negativo para alinear por izquierda con Ventas
        orientation='h',
        name='Utilidad Neta',
        marker=dict(color='lightgreen'),
        text=[f'${utilidad_neta:,.0f}'],
        textposition='outside',
        hovertemplate='<b>Utilidad Neta</b><br>Monto: $%{abs(x):,.0f}<extra></extra>'
    ))
    
    # Configurar layout
    fig.update_layout(
        title=dict(
            text="<b>Estado de Resultados</b>",
            x=0.5,
            font=dict(size=16)
        ),
        xaxis=dict(
            title="Monto ($)",
            showgrid=True,
            gridcolor='lightgray',
            zeroline=True,
            zerolinecolor='black',
            zerolinewidth=2,
            tickformat=',.0f'
        ),
        yaxis=dict(
            showgrid=False,
            categoryorder='array',
            categoryarray=['Ventas', 'Gastos', 'Utilidad Neta']
        ),
        height=400,
        margin=dict(l=120, r=120, t=40, b=40),
        showlegend=False,
        barmode='relative'
    )
    
    # Añadir línea vertical en el centro (punto cero)
    fig.add_vline(x=0, line_dash="dash", line_color="black", line_width=2)
    
    # Añadir anotación de la fórmula
    fig.add_annotation(
        x=0.5, y=1.05,
        xref='paper', yref='paper',
        text="Ventas = Gastos + Utilidad Neta",
        showarrow=False,
        font=dict(size=12, color='gray'),
        align="center"
    )
    
    return fig

def crear_balance_general(activos, deuda, patrimonio):
    """
    Crea un gráfico apilado para el Balance General
    
    Args:
        activos (float): Monto total de activos
        deuda (float): Monto total de deuda
        patrimonio (float): Monto total de patrimonio
    
    Returns:
        plotly.graph_objects.Figure: Gráfico apilado del Balance General
    """
    
    # Crear figura
    fig = go.Figure()
    
    # Lado izquierdo: Activos
    fig.add_trace(go.Bar(
        x=['Activos'],
        y=[activos],
        name='Activos',
        marker=dict(color='lightgreen'),
        text=[f'${activos:,.0f}'],
        textposition='auto',
        hovertemplate='<b>Activos</b><br>Monto: $%{y:,.0f}<extra></extra>'
    ))
    
    # Lado derecho: Deuda y Patrimonio (apilados)
    fig.add_trace(go.Bar(
        x=['Pasivo + Patrimonio'],
        y=[deuda],
        name='Deuda',
        marker=dict(color='lightpink'),
        text=[f'${deuda:,.0f}'],
        textposition='auto',
        hovertemplate='<b>Deuda</b><br>Monto: $%{y:,.0f}<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        x=['Pasivo + Patrimonio'],
        y=[patrimonio],
        name='Patrimonio',
        marker=dict(color='lightblue'),
        text=[f'${patrimonio:,.0f}'],
        textposition='auto',
        hovertemplate='<b>Patrimonio</b><br>Monto: $%{y:,.0f}<extra></extra>'
    ))
    
    # Configurar layout
    fig.update_layout(
        title=dict(
            text="<b>Balance General</b>",
            x=0.5,
            font=dict(size=16)
        ),
        yaxis=dict(
            title="Monto ($)",
            showgrid=True,
            gridcolor='lightgray'
        ),
        xaxis=dict(
            showgrid=False
        ),
        height=400,
        margin=dict(l=80, r=80, t=40, b=40),
        showlegend=True,
        legend=dict(
            x=0.5,
            y=1.02,
            orientation='h',
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='black',
            borderwidth=1
        ),
        barmode='stack'
    )
    
    # Añadir anotación de la fórmula
    fig.add_annotation(
        x=0.5, y=1.05,
        xref='paper', yref='paper',
        text="Activos = Deuda + Patrimonio",
        showarrow=False,
        font=dict(size=12, color='gray'),
        align="center"
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
    
    st.sidebar.markdown("---")
    st.sidebar.header("📊 Estados Financieros Simplificados")
    st.sidebar.markdown("Ajuste los parámetros para los estados financieros:")
    
    # Sliders para Estados Financieros
    gastos = st.sidebar.slider(
        "Gastos ($)",
        min_value=0,
        max_value=4000000,
        value=900000,
        step=25000,
        help="Gastos operativos totales"
    )
    
    # Calcular automáticamente para mantener la lógica financiera
    utilidad_calculada = max(0, ventas - gastos)
    
    # Ajustar utilidad_neta para que coincida con la lógica
    utilidad_neta = utilidad_calculada
    
    st.sidebar.markdown(f"*Utilidad Neta calculada: ${utilidad_neta:,.0f}*")
    
    deuda = st.sidebar.slider(
        "Deuda Total ($)",
        min_value=0,
        max_value=2000000,
        value=400000,
        step=25000,
        help="Total de deudas y pasivos"
    )
    
    # Calcular automáticamente para mantener el balance
    patrimonio_balance = max(0, activos_promedio - deuda)
    
    st.sidebar.markdown(f"*Patrimonio calculado: ${patrimonio_balance:,.0f}*")
    
    # Usar el patrimonio calculado para consistencia
    patrimonio_promedio = patrimonio_balance
    
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
    
    # Visualización 3D del Prisma DuPont
    st.header("🔮 Prisma DuPont 3D")
    st.markdown("Visualización interactiva del modelo DuPont - El volumen del prisma representa el ROE")
    
    # Crear y mostrar el prisma 3D
    fig_prisma = crear_prisma_3d_dupont(resultados)
    st.plotly_chart(fig_prisma, use_container_width=True)
    
    # Explicación del prisma
    with st.expander("📖 Interpretación del Prisma 3D"):
        st.markdown("""
        **El Prisma DuPont 3D** representa visualmente cómo los tres componentes se combinan para generar el ROE:
        
        - **Eje X (Margen Neto)**: Base del prisma en el eje horizontal. Mayor margen = base más larga.
        - **Eje Y (Rotación de Activos)**: Profundidad del prisma. Mayor rotación = prisma más profundo.
        - **Eje Z (Apalancamiento)**: Altura del prisma. Mayor apalancamiento = prisma más alto.
        
        **El volumen total del prisma representa el ROE**. Al modificar los sliders, verás cómo cambia la forma y volumen del prisma, 
        permitiendo entender intuitivamente el impacto de cada componente en la rentabilidad final.
        
        **Interacción con el gráfico:**
        - Haz clic y arrastra para rotar el prisma
        - Usa la rueda del mouse para hacer zoom
        - Pasa el cursor sobre los elementos para ver detalles
        """)
    
    # Estados Financieros Simplificados - Funcionalidad 3
    st.markdown("---")
    st.header("📊 Estados Financieros Simplificados")
    st.markdown("Visualización interactiva de los estados financieros básicos")
    
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        # Estado de Resultados
        st.markdown("### 📈 Estado de Resultados")
        st.markdown("Ventas = Gastos + Utilidad Neta")
        
        fig_estado_resultados = crear_estado_resultados(ventas, gastos, utilidad_neta)
        st.plotly_chart(fig_estado_resultados, use_container_width=True)
        
        # Métricas del Estado de Resultados
        st.markdown("**Resumen Financiero:**")
        st.markdown(f"- **Ventas:** ${ventas:,.0f}")
        st.markdown(f"- **Gastos:** ${gastos:,.0f}")
        st.markdown(f"- **Utilidad Neta:** ${utilidad_neta:,.0f}")
        st.markdown(f"- **Margen Neto:** {(utilidad_neta/ventas)*100:.1f}%")
    
    with col2:
        # Balance General
        st.markdown("### 📋 Balance General")
        st.markdown("Activos = Deuda + Patrimonio")
        
        fig_balance_general = crear_balance_general(activos_promedio, deuda, patrimonio_balance)
        st.plotly_chart(fig_balance_general, use_container_width=True)
        
        # Métricas del Balance General
        st.markdown("**Estructura del Balance:**")
        st.markdown(f"- **Activos Totales:** ${activos_promedio:,.0f}")
        st.markdown(f"- **Deuda Total:** ${deuda:,.0f}")
        st.markdown(f"- **Patrimonio Neto:** ${patrimonio_balance:,.0f}")
        st.markdown(f"- **Ratio Deuda/Patrimonio:** {(deuda/patrimonio_balance):.2f}x" if patrimonio_balance > 0 else "- **Ratio Deuda/Patrimonio:** N/A")
    
    # Explicación de los Estados Financieros
    with st.expander("📖 Interpretación de los Estados Financieros"):
        st.markdown("""
        **Estados Financieros Simplificados** proporcionan una visión clara de la salud financiera:
        
        **Estado de Resultados:**
        - Muestra la rentabilidad del período
        - Las ventas se alinean a la derecha (salidas de efectivo)
        - La utilidad neta se alinea a la izquierda (entrada neta)
        - La fórmula fundamental: Ventas = Gastos + Utilidad Neta
        
        **Balance General:**
        - Muestra la posición financiera en un momento específico
        - Los activos (izquierda) deben igualar la suma de deuda + patrimonio (derecha)
        - La fórmula fundamental: Activos = Deuda + Patrimonio
        - Refleja cómo se financian los activos de la empresa
        
        **Relación con el ROE:**
        - La utilidad neta del estado de resultados alimenta el cálculo del ROE
        - La estructura del balance general afecta el apalancamiento financiero
        - Ambos estados son fundamentales para el análisis DuPont completo
        """)

if __name__ == "__main__":
    main()
