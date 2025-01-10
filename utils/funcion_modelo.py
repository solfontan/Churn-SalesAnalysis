# Preparación de datos 
from sklearn.model_selection import train_test_split, cross_validate
# Modelos
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import  RandomForestClassifier,  GradientBoostingClassifier, AdaBoostClassifier, HistGradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from catboost import CatBoostClassifier
import lightgbm as lgb
import xgboost as xgb
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Ignorar warnings
import warnings
warnings.filterwarnings('ignore')

def BaseLine(x_train, y_train, cv: int, metricas_cross_validate: list):
    """ Crea la validación cruzada para los modelos que deseemos.

    Args:
        x_train (_type_): _description_
        y_train (_type_): _description_
        cv (int): folds.
        metricas_cross_validate (list): solo Clasificación.

    Returns:
        df: DtaFrame con las métricas obtenidas de la validación cruzada.
    """
    try:
        # Definir modelos disponibles
        modelos = {
            "1":  LogisticRegression(),
            "2":  RandomForestClassifier(),
            "3":  AdaBoostClassifier(),
            "4":  GradientBoostingClassifier(),
            "5":  ExtraTreeClassifier(),
            "6":  DecisionTreeClassifier(),
            "7":  CatBoostClassifier(silent=True),
            "8":  lgb.LGBMClassifier(verbosity= -1),
            "9":  xgb.XGBClassifier(),
            "10": KNeighborsClassifier(),
            "11": SVC(), 
            "12": HistGradientBoostingClassifier()
        }

        # Pedir al usuario que seleccione los modelos
        answer_modelos = input('¿Cuáles son los modelos que desea utilizar? (seleccione números separados por comas o escriba "todos" para seleccionar todos los modelos): 1: Logistic Regression, 2: Random Forest, 3: ADABoosting, 4: GradientBoosting, 5: ExtraTrees, 6: DecisionTree, 7: CatBoost, 8: LGBM, 9: XGBoost, 10: KNN, 11: SVC, 12: HistGradientBoost')

        # Seleccionar modelos según la entrada del usuario
        if answer_modelos.lower() == 'todos':
            modelos_seleccionados = modelos
        else:
            selected_models_indices = [int(x.strip()) for x in answer_modelos.split(',')]
            modelos_seleccionados = {key: modelos[key] for key in map(str, selected_models_indices)}

        # Realizar la validación cruzada y calcular las métricas
        metricas = metricas_cross_validate
        resultados_dict = {}

        for nombre_modelo, modelo in modelos_seleccionados.items():
            if cv:
                cv_resultados = cross_validate(modelo, x_train, y_train, cv=cv, scoring=metricas)
            else:
                cv_resultados = cross_validate(modelo, x_train, y_train, cv=5, scoring=metricas)

            for metrica in metricas:
                clave = f"{nombre_modelo}_{metrica}"
                resultados_dict[clave] = cv_resultados[f"test_{metrica}"].mean()

        # Mapear claves numéricas a nombres de modelos más descriptivos
        nombres_descriptivos = ['Logistic Regression', 'Random Forest', 'ADABoosting', 'Gradient Boosting', 'Extra Trees', 'Decision Tree', 'CatBoost', 'LGBM', 'XGBoost', 'KNN', 'SVC', 'HistGradientBoost']
        diccionario_nombres = {clave: nombres_descriptivos[int(clave) - 1] for clave in modelos_seleccionados}

        index = [diccionario_nombres.get(clave.split('_')[0]) for clave in resultados_dict.keys()]
        metrica = [clave.split('_')[1] for clave in resultados_dict.keys()]

       # Crear DataFrame con nombres descriptivos y métricas como columnas
        resultados_df = pd.DataFrame({'Modelo': index, 'Metrica': metrica, 'Score': resultados_dict.values()})

        # Crear una tabla pivote para tener las métricas como columnas
        resultados_pivot = resultados_df.pivot(index='Modelo', columns='Metrica', values='Score')

        return resultados_pivot

    except Exception as e:
        print('Surgió un error:', e)