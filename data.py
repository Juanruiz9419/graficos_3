import pandas as pd
import plotly.express as px

# Crear el DataFrame con los datos proporcionados
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Definir colores para cada materia
colors = px.colors.qualitative.Set1[:5]

# Boxplot con Plotly
fig = px.box(df, x='materia', y='nota', points=False, color='materia',
            title='Distribución de Notas por Materia',
            labels={'nota': 'Nota', 'materia': 'Materia'},
            category_orders={'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']},
            color_discrete_sequence=colors)

# Ajustar ejes y diseño
fig.update_layout( yaxis_title='Nota', boxmode='group')

# Ajustar el grosor de las líneas de los boxplots
fig.update_traces(marker=dict(size=8),
            line=dict(width=1),  # Grosor de las líneas de los boxplot
            offsetgroup='materia')  # Centrar sobre su respectiva materia



# Mostrar el gráfico
fig.show()

df = pd.DataFrame(data)

# Contar el número de aprobados y no aprobados
aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

# Crear el pie chart con Plotly
fig = px.pie(names=['Aprobados', 'No Aprobados'], values=[aprobados, no_aprobados],
            title='Distribución de Aprobados y No Aprobados')

# Mostrar el gráfico
fig.show()