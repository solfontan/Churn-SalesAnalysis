## 📊 **Análisis del Abandono de Clientes (Churn) 📉  

🚀 **¿Cómo predecimos y reducimos la pérdida de clientes?** En este proyecto se analizarán patrones y tendencias en los datos, con el objetivo de identificar posibles correlaciones y proporcionar información que pueda servir para estrategias futuras de retención de clientes.

## 🔍 **Descripción del Proyecto**  

Este análisis se centra en identificar los principales factores que afectan la retención de clientes. A través de la exploración de datos, visualizaciones y validación de hipótesis, descubrimos qué variables tienen mayor impacto en la decisión de los clientes de continuar o cancelar nuestro servicio.  

💡 **Objetivo principal:** Proporcionar insights accionables para mejorar la fidelización y reducir la tasa de churn.  

## 📌 **Estructura del Proyecto**  

📁 **`data/`** → Conjunto de datos utilizado en el análisis.  
- **raw** → bases de datos en formato .csv
- **clean** → bases de datos, procesadas y limpias para la presentación de gráficos e hipótesis.
📁 **`notebooks/`** → Análisis exploratorio, limpieza de datos y pruebas de hipótesis.  
📁 **`utils/`** → Funciones auxiliares para el procesamiento de datos.  

## 📊 **Análisis Destacados**  

1️⃣ **Limpieza y preparación de datos** 🧹  
   - Tratamiento de valores nulos y atípicos.  
   - Conversión de variables categóricas.  

2️⃣ **Exploración de Factores Clave** 🔬  
   - 📍 **Ubicación geográfica y churn** → ¿Influye la región en la retención del cliente?  
   - 💳 **Método de pago** → ¿Los pagos manuales generan más cancelaciones?  
   - 📈 **Tipo de contrato** → ¿Los contratos mensuales tienen mayor tasa de churn?  

3️⃣ **Validación de Hipótesis** ✅  
   - Se analizaron patrones estadísticos y se confirmaron factores relevantes.  
   - Se investigó la efectividad de **ofertas** para reducir el churn.  

4️⃣ **Dashboard Interactivo** 📊  
   - Implementamos un dashboard para visualizar tendencias y tomar decisiones estratégicas en formato .xlsm  

## ⚙️ **Configuración del Entorno**  

Para ejecutar este proyecto de forma local, sigue estos pasos:  

### 1️⃣ **Clonar el repositorio**  
```bash
git clone https://github.com/tu_usuario/churn-analysis.git  
cd churn-analysis
```

### 2️⃣ **Crear un entorno virtual**  
```bash
# En Windows
python -m venv .venv  
.venv\Scripts\activate  

# En macOS/Linux
python3 -m venv .venv  
source .venv/bin/activate  
```

### 3️⃣ **Instalar dependencias**  
```bash
pip install -r requirements.txt  
```

### 4️⃣ **Ejecutar los notebooks**  
Abre Jupyter Notebook para visualizar los análisis:  
```bash
jupyter notebook  
```

## 🚀 **Tecnologías Utilizadas**  

🔹 **Python** 🐍 (pandas, numpy, seaborn, matplotlib, scikit-learn)  
🔹 **Jupyter Notebooks** 📒  
🔹 **Excel** 📊 (para visualizaciones)  

## 📎 **Accede al Análisis Completo**  

🔗 **Hipótesis y Validaciones:** [Explorar hipótesis](Notebooks)  
🔗 **Resúmen del Proyecto:** [Ver Resúmen](project_resume.ipynb)  