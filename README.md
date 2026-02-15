# 🏦 ROE DuPont Interactivo

Una aplicación interactiva para el análisis financiero mediante el modelo DuPont, desarrollada como herramienta educativa para comprender la rentabilidad empresarial de manera visual e intuitiva.

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Características Principales](#características-principales)
- [Requisitos Técnicos](#requisitos-técnicos)
- [Instalación](#instalación)
- [Guía de Uso](#guía-de-uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Interpretación de Resultados](#interpretación-de-resultados)
- [Licencia](#licencia)

---

## 🎯 Descripción del Proyecto

**ROE DuPont Interactivo** es una aplicación web educativa que permite analizar la rentabilidad de una empresa utilizando el modelo DuPont, una metodología financiera que descompone el Return on Equity (ROE) en tres componentes fundamentales:

1. **Margen Neto**: Mide la rentabilidad de las ventas
2. **Rotación de Activos**: Evalúa la eficiencia en el uso de activos
3. **Apalancamiento Financiero**: Analiza el nivel de endeudamiento

La aplicación ofrece una experiencia visual completa con gráficos interactivos, un prisma 3D que representa el modelo DuPont, y estados financieros simplificados que facilitan la comprensión de los conceptos financieros.

---

## ✨ Características Principales

### Funcionalidad 1: Cálculo de Ratios Financieros Básicos
- **Cálculo automático del ROE** mediante la fórmula DuPont
- **Métricas clave**: Margen Neto, Rotación de Activos, Apalancamiento Financiero
- **Indicadores visuales** con gauges interactivos
- **Validación de datos** para evitar errores de cálculo

### Funcionalidad 2: Prisma 3D DuPont
- **Visualización tridimensional** del modelo DuPont
- **Representación volumétrica** donde el volumen del prisma representa el ROE
- **Interacción completa**: rotación, zoom y navegación 3D
- **Colores intuitivos** para cada componente del modelo

### Funcionalidad 3: Estados Financieros Simplificados
- **Estado de Resultados**: Visualización de Ventas, Gastos y Utilidad Neta
- **Balance General**: Representación de Activos, Deuda y Patrimonio
- **Gráficos alineados** según estándares financieros
- **Cálculos automáticos** para mantener la coherencia financiera

---

## 🔧 Requisitos Técnicos

### Sistema Operativo
- Windows 10/11
- macOS 10.14+
- Linux (Ubuntu 18.04+)

### Python
- **Versión mínima**: Python 3.8+
- **Recomendada**: Python 3.9+

### Librerías Necesarias
```
streamlit>=1.28.0
numpy>=1.21.0
pandas>=1.3.0
plotly>=5.0.0
```

### Hardware Recomendado
- **RAM**: Mínimo 4GB, recomendado 8GB
- **Procesador**: Intel i5/AMD Ryzen 5 o superior
- **Navegador**: Chrome, Firefox, Safari o Edge (versiones recientes)

---

## 🚀 Instalación

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/aldanfertest-cursor/windsurf-roe-dupont.git
cd windsurf-roe-dupont
```

### Paso 2: Crear Entorno Virtual (Recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### Paso 3: Instalar Dependencias
```bash
pip install -r documentos/requirements.txt
```

O instalar manualmente:
```bash
pip install streamlit numpy pandas plotly
```

### Paso 4: Ejecutar la Aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web en `http://localhost:8501`

---

## 📖 Guía de Uso

### Inicio Rápido

1. **Abrir la aplicación**: Ejecuta `streamlit run app.py` en tu terminal
2. **Ajustar parámetros**: Usa los sliders en la barra lateral derecha
3. **Observar resultados**: Los gráficos se actualizan en tiempo real
4. **Analizar**: Explora las diferentes secciones para entender los resultados

### Ejemplo Básico: Análisis de Empresa Manufacturera

**Configuración Inicial:**
- **Ventas**: $1,000,000
- **Gastos**: $900,000
- **Utilidad Neta**: $100,000 (calculada automáticamente)
- **Activos**: $800,000
- **Deuda**: $400,000
- **Patrimonio**: $400,000 (calculado automáticamente)

**Resultados Esperados:**
- **ROE**: 31.25%
- **Margen Neto**: 10%
- **Rotación de Activos**: 1.25x
- **Apalancamiento**: 2.0x

### Navegación por Secciones

#### 1. Panel de Control (Sidebar)
- **Parámetros DuPont**: Ajusta las variables principales del análisis
- **Estados Financieros**: Configura los datos para los gráficos financieros
- **Cálculos automáticos**: La aplicación mantiene la coherencia matemática

#### 2. Métricas Principales
- **Tarjetas de resumen**: Vista rápida de los indicadores clave
- **Colores codificados**: Verde para positivos, rojo para alertas

#### 3. Prisma 3D DuPont
- **Rotación**: Click y arrastra para rotar el prisma
- **Zoom**: Usa la rueda del mouse
- **Interpretación**: El volumen representa el ROE total

#### 4. Estados Financieros
- **Estado de Resultados**: Barras horizontales alineadas
- **Balance General**: Gráfico apilado de estructura financiera
- **Métricas detalladas**: Porcentajes y ratios adicionales

---

## 📁 Estructura del Proyecto

```
windsurf-roe-dupont/
├── app.py                          # Aplicación principal
├── documentos/
│   ├── requirements.txt              # Dependencias del proyecto
│   ├── Estado de Resultados.png     # Referencia visual del gráfico
│   └── Imagen Prisma dD.png      # Referencia visual del prisma
├── venv/                          # Entorno virtual (no incluir en git)
├── .git/                          # Control de versiones
└── .windsurf/                     # Configuración de Windsurf
```

### Archivos Clave

#### `app.py`
- **Función principal**: `main()` - Orquesta la interfaz Streamlit
- **Cálculos DuPont**: `calcular_dupont()` - Implementa la fórmula DuPont
- **Visualizaciones**:
  - `crear_prisma_3d_dupont()` - Genera el prisma tridimensional
  - `crear_estado_resultados()` - Crea el gráfico del estado de resultados
  - `crear_balance_general()` - Genera el balance general visual
  - `crear_metricas_dupont()` - Indicadores con gauges

#### `documentos/requirements.txt`
Lista las dependencias necesarias para el funcionamiento del proyecto.

---

## 📊 Interpretación de Resultados

### Entendiendo el ROE DuPont

El **Return on Equity (ROE)** mide la rentabilidad generada para los accionistas. El modelo DuPont lo descompone en:

#### 1. Margen Neto (Rentabilidad Operativa)
```
Margen Neto = Utilidad Neta / Ventas
```
- **Alto margen (>15%)**: Empresa eficiente en costos o con productos premium
- **Margen medio (5-15%)**: Rendimiento estándar del sector
- **Bajo margen (<5%)**: Posibles problemas de costos o competencia alta

#### 2. Rotación de Activos (Eficiencia Operativa)
```
Rotación de Activos = Ventas / Activos Promedio
```
- **Alta rotación (>2x)**: Uso eficiente de los activos
- **Rotación media (1-2x)**: Rendimiento normal
- **Baja rotación (<1x)**: Activos subutilizados

#### 3. Apalancamiento Financiero (Estructura de Capital)
```
Apalancamiento = Activos / Patrimonio
```
- **Alto apalancamiento (>3x)**: Mayor riesgo, potencial de mayor rentabilidad
- **Apalancamiento medio (1.5-3x)**: Estructura equilibrada
- **Bajo apalancamiento (<1.5x)**: Menor riesgo, crecimiento más lento

### Ejemplo Práctico: Análisis Comparativo

#### Empresa A (Retail)
- **Ventas**: $2,000,000
- **Utilidad Neta**: $100,000
- **Activos**: $1,000,000
- **Patrimonio**: $500,000

**Resultados:**
- **Margen Neto**: 5% (bajo, típico de retail)
- **Rotación**: 2.0x (alta, eficiente)
- **Apalancamiento**: 2.0x (moderado)
- **ROE**: 20% (bueno)

#### Empresa B (Software)
- **Ventas**: $500,000
- **Utilidad Neta**: $100,000
- **Activos**: $500,000
- **Patrimonio**: $400,000

**Resultados:**
- **Margen Neto**: 20% (alto, típico de software)
- **Rotación**: 1.0x (media, activos intangibles)
- **Apalancamiento**: 1.25x (bajo, conservador)
- **ROE**: 25% (excelente)

### Interpretación del Prisma 3D

El prisma representa visualmente la fórmula:
```
ROE = Margen Neto × Rotación de Activos × Apalancamiento
```

- **Eje X (base)**: Margen Neto - más largo = mayor rentabilidad
- **Eje Y (profundidad)**: Rotación - más profundo = mayor eficiencia
- **Eje Z (altura)**: Apalancamiento - más alto = mayor apalancamiento
- **Volumen total**: ROE combinado

### Estados Financieros Simplificados

#### Estado de Resultados
Muestra la ecuación fundamental: **Ventas = Gastos + Utilidad Neta**
- **Ventas (celeste)**: Ingresos totales del período
- **Gastos (rosado)**: Costos y gastos operativos
- **Utilidad Neta (verde)**: Resultado final después de gastos

#### Balance General
Representa: **Activos = Deuda + Patrimonio**
- **Activos (verde)**: Recursos económicos de la empresa
- **Deuda (rosado)**: Obligaciones financieras
- **Patrimonio (celeste)**: Capital de los accionistas

---

## 📚 Notas Educativas

### Conceptos Clave para Estudiantes

1. **ROE no lo es todo**: Un ROE alto puede venir de alto riesgo (apalancamiento)
2. **Contexto sectorial**: Los ratios normales varían por industria
3. **Tendencias**: Más importante que el valor absoluto es la evolución temporal
4. **Calidad de ganancias**: Analizar el origen del margen neto

### Errores Comunes al Interpretar

- **Ignorar el riesgo**: Un ROE alto con alto apalancamiento puede ser peligroso
- **Comparar sectores diferentes**: Cada industria tiene sus propios benchmarks
- **Foco en corto plazo**: El análisis financiero requiere perspectiva temporal

---

## 📜 Licencia

### Aviso Educativo

**Este proyecto tiene fines exclusivamente educativos** y ha sido desarrollado como herramienta de aprendizaje para estudiantes de finanzas, administración y carreras afines.

### Limitaciones del Uso

- ✅ **Permitido**: Uso educativo, aprendizaje, modificaciones para fines académicos
- ❌ **No permitido**: Uso comercial, toma de decisiones financieras reales sin validación profesional
- ⚠️ **Advertencia**: Los resultados son aproximados y no deben reemplazar asesoría profesional

### Créditos y Atribución

- **Desarrollado por**: Proyecto educativo DuPont Interactivo
- **Tecnologías**: Streamlit, Plotly, NumPy, Pandas
- **Metodología**: Modelo DuPont de análisis financiero

### Mejoras Futuras

- [ ] Análisis de tendencias temporales
- [ ] Comparación entre empresas
- [ ] Exportación de reportes
- [ ] Integración con datos reales de mercados
- [ ] Análisis de sensibilidad

---

## 🤝 Contribuciones

Este proyecto educativo bienven contribuciones que mejoren su valor pedagógico. Por favor:
1. Fork el repositorio
2. Crear una rama para tu mejora
3. Documentar los cambios educativos
4. Submit un pull request

---

**🎓 Para uso educativo y de aprendizaje únicamente**

*Última actualización: Diciembre 2024*
