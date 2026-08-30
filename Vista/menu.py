from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget

''' ------------------------------------ [ Menu - Pantalla de Inicio ] ------------------------------------'''

#Creamos un objeto que se encarga de administrar
pant_inicio = QApplication() #<--- Es el modulo de Ps6 que encarga de administrar Botoens, Campos de texto, etc

#--Ventana 1
ventana = QWidget()

#Modificar las caracteristicas de la ventana
ventana.setWindowTitle("3P")
ventana.resize(800,500)

#--Textos
texto = QLabel("3P")

#Botones
boton_iniciar = QPushButton("ENTER Para Explotar")
boton_iniciar.setStyleSheet("""
    /* Botón normal */
    QPushButton {
        background-color: red;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
    }

    /* Cuando el mouse está encima */
    QPushButton:hover {
        background-color: blue;
    }

    /* Mientras se está presionando */
    QPushButton:pressed {
        background-color: green;
    }
""")

#boton1.clicked.connect(explotar)

#Layouts son sistemas que organizan los widgets

layout1 = QVBoxLayout() #<-- Creamos el layout, funciona como una caja

layout1.addWidget(texto) #<-- Guardamos texto
layout1.addWidget(boton_iniciar) #<-- Guardamos boton

ventana.setLayout(layout1)

ventana.show() #<-- Activa la ventana
boton_iniciar.show()

pant_inicio.exec() #<-- Activa el administrador

