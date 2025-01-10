import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

def cardinalidad(df: pd.DataFrame):
    """Funciòn cardinalidad

    Args:
        df (pd.DataFrame): DataFrame

    Returns:
        df (pd.DataFrame) : incluye -> valores únicos, la cardinalidad, el tipo de dato y por último un input que deberá rellenarse de forma manual para calificar nuestro dato.
    """
    cardi = pd.DataFrame(columns=['cardinalidad', 'porcentaje_cardinalidad', 'tipo_de_dato', 'valores_unicos', 'tipo_de_variable'],
                         index=df.columns)

    cardi['cardinalidad'] = [df[col].nunique() for col in df.columns]
    cardi['porcentaje_cardinalidad'] = cardi['cardinalidad'] / len(df) * 100
    cardi['tipo_de_dato'] = df.dtypes
    cardi['valores_unicos'] = [valor if valor <= 15 else 'valores unicos no representativos' for valor in
                               [df[columna].nunique() for columna in df.columns]]

    valores_tipo_variable = [input(f'Para la columna {columna} ingrese el valor "Tipo_de_variable": ') for columna in df.columns]
    cardi['tipo_de_variable'] = valores_tipo_variable

    return cardi

def extended_describe(column : str, df : pd.DataFrame) -> pd.DataFrame:
    """ DataFrame con medidas de tendencias central y de distribución incluído la kurtosis y asimetría.

    Args:
        column (str)
        df (pd.DataFrame)

    Returns:
        DataFrame
    """

    describe_df = df[column].describe()
    # Crear un nuevo DataFrame con las estadísticas extendidas
    extended_describe_df = pd.DataFrame({
        'count': describe_df['count'],
        'mean': describe_df['mean'],
        'median':df[column].median(),
        'mode' : df[column].mode()[0],
        'std' : round(describe_df['std'],2),
        'min': describe_df['min'],
        '25%': describe_df['25%'],
        '50%': describe_df['50%'],
        '75%': describe_df['75%'],
        'max': describe_df['max'],
        'kurtosis': round(kurtosis(df[column]), 2),
        'skewness': round(skew(df[column]),2)
    }, index=[column])
    
    if kurtosis(df[column]) > 0 :
        print(f"La distribución es leptocúrtica con una curtosis de {round(kurtosis(df[column]), 2)}. Los datos se encuentran concentrados alrededor de la media.")
    elif kurtosis(df[column]) < 0 :
        print(f"La distribución es platicúrtica con una curtosis de {round(kurtosis(df[column]), 2)}. Los datos se encuentran dispersos.")
    elif kurtosis(df[column]) == 0 :
        print(f"La distribución es mesocúrtica con una curtosis de {round(kurtosis(df[column]), 2)}. Los datos se comportan de manera normal")
        
    if skew(df[column]) > 0 :
        print(f"La distribución se encuentra sesgada hacia la izquierda {round(skew(df[column]),2)}.")
    else:
        print(f"La distribución se encuentra sesgada hacia la derecha {round(skew(df[column]),2)}.")
        
    return extended_describe_df

class CategoricalAnalysis:
    """
    Análisis categórico de Variables, con el fin de dar un pantallazo más amplio.
    
    """
    def __init__(self, df):
        self.df = df
        
    def plot_top_categories(self, title : str, column_name : str, labely : str, n=5):
        """Incluyen dos gráficos, uno de brras con máximo de 5 valores y los mismos dentro de un gráfico de pie.

        Args:
            title (str)
            column_name (str)
            labely (str): label del eje y.
            n (int, optional): Defaults to 5.
        """
        # Obtener recuento de valores y nombres de las primeras n categorías
        top_categories = self.df[column_name].value_counts().nlargest(n)
        top_category_names = top_categories.index.tolist()
        top_category_counts = top_categories.values.tolist()
        
        # Colores para los gráficos
        branch_col = ['navy', 'crimson', 'forestgreen', 'orange', 'purple', 'darkblue', 'darkred', 'darkgreen', 'yellow', 'darkviolet']
        
        # Crear gráficos
        with plt.style.context('fivethirtyeight'):
            plt.rcParams.update({'font.size': 12})
            fig, ax = plt.subplots(1, 2, figsize=(13, 6))
            plt.subplots_adjust(wspace=0.3)
            
            # Gráfico de barras
            if len(top_category_names) >= 5:  # Si hay cinco o menos categorías
                ax[0].bar(top_category_names, 
                          top_category_counts, 
                          color=branch_col[:n])
                ax[0].tick_params(axis='x', rotation=65)  # Rotar el eje x 45 grados
            else:
                ax[0].bar(top_category_names, 
                          top_category_counts, 
                          color=branch_col[:n], width=0.7)  # Ajustar el ancho de las barras si hay más de cinco categorías
            for x , y, col in zip(top_category_names, 
                             top_category_counts, branch_col[:n]):
                ax[0].text(x, y/2, y, 
                           ha='center',color='white', 
                           bbox=dict(facecolor=col, edgecolor='white', boxstyle='circle'))
            ax[0].set_ylabel(labely)
            # Agregar leyenda para el gráfico de barras
   
            # Gráfico de pastel
            pie = ax[1].pie(x=top_category_counts, 
                            labels=top_category_names,
                            colors=branch_col[:n],  
                            autopct='%1.1f%%',
                            textprops={'color': 'darkgray'}) 
            
            ax[1].legend(loc='upper left', fontsize="xx-small")
            plt.title(title, loc= 'center', fontsize=12)

            plt.show()


    def plot_distribution(self, title : str, column_name: str, alpha : float, color: str, cant_bins : int, rotation : int):
        """histplot con estilo uniforme al igual que la función plot_top_categories

        Args:
            title (str)
            column_name (str)
            alpha (float): entre 0 y 1.
            color (str)
            cant_bins (int)
            rotation (int): de labels sobre el eje X.

        Returns:
            Gráficos
        """
        plt.rcParams['axes.labelpad'] = 5  # Ajustar el espaciado entre las etiquetas y los ejes
        plt.rcParams['xtick.bottom'] = True  # Colocar las etiquetas del eje X en la parte inferior
        plt.rcParams['ytick.left'] = True  # Colocar las etiquetas del eje Y en la izquierda
        plt.rcParams['xtick.top'] = False  # Deshabilitar las etiquetas del eje X en la parte superior
        plt.rcParams['ytick.right'] = False  # Deshabilitar las etiquetas del eje Y en la derecha
        
        # Crear el histograma sin KDE
        with plt.style.context('fivethirtyeight'):
            plt.rcParams.update({'font.size': 10})
            plt.figure(figsize=(10,7))
            plt.grid(True, alpha=0.3)  # Establecer la transparencia del grid
            sns.histplot(data=self.df, x=column_name, color=color, bins=cant_bins, alpha=alpha, edgecolor='white', linewidth=0)
            plt.xlabel(column_name)
            plt.ylabel('Frequency')
            plt.xticks(rotation=rotation)
            plt.title(title, loc='center', fontsize=12)
            plt.show()

        answer_df = input('¿Deseas un dataframe con las medidas centrales, de distribución y asimetría del gráfico? : si / no')
        
        if answer_df.lower() == 'si':
            return extended_describe(column_name, self.df)
           

