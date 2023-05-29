import streamlit as st
import pandas as pd
import joblib

def predict(df):
    # Cargar el modelo entrenado
    model_path = "/home/estudiante/proyecto_final/notebook/best_model.pkl"
    model = joblib.load(model_path)

    # Realizar la inferencia utilizando el modelo cargado
    predictions = model.predict(df)

    return predictions

def main():
    st.title("Aplicacion de inferencia. ")
    st.write("El modelo considerado para la siguiente prediccion es Gradient Boosting Classifier")
    st.write("Carga un archivo CSV para realizar inferencia")

    # Agregar la opcion para cargar un archivo CSV
    uploaded_file = st.file_uploader("Cargar archivo CSV", type="csv")

    if uploaded_file is not None:
        # Leer el archivo CSV
        df = pd.read_csv(uploaded_file)

        # Realizar las inferencias llamando a la funcion predict()
        predictions = predict(df)

        # Mostrar los resultados
        st.write("Resultado de la prediccion:")
        st.write(predictions)

if __name__ == "__main__":
    main()


