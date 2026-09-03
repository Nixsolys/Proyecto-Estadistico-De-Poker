# 🎴 Proyect - Póker - Probability

Aplicación de escritorio desarrollada en **Python y PySide6** para el análisis y cálculo de probabilidades relacionadas con manos de **Texas Hold'em Poker**.

El proyecto busca combinar conceptos de **programación orientada a objetos, probabilidad, estadística y desarrollo de interfaces gráficas** en una aplicación de escritorio.

## ✨ Características

* 🎴 Representación de cartas mediante programación orientada a objetos.
* ♠️ Manejo de palos y valores de las cartas.
* 📊 Cálculo y análisis de probabilidades.
* 🖥️ Interfaz gráfica desarrollada con PySide6.
* 📁 Organización del proyecto mediante separación de responsabilidades.
* 🔀 Flujo de trabajo basado en Git y GitHub.

---

## 🛠️ Tecnologías

| Tecnología | Uso                        |
| ---------- | -------------------------- |
| Python     | Lenguaje principal         |
| PySide6    | Interfaz gráfica           |
| Git        | Control de versiones       |
| GitHub     | Repositorio y colaboración |
| PlantUML   | Diagramas UML              |

---

## 🏗️ Arquitectura

El proyecto utiliza una organización basada en la separación entre **Modelo, Vista y Controlador (MVC)**.

```text
src/
├── modelo/
│   └── cartas.py
│
├── vista/
│   ├── ventana.py
│   └── botones.py
│
├── controlador/
│   └── controlador.py
│
└── main.py
```

### Modelo

Contiene la lógica y representación de los datos del sistema.

### Vista

Contiene los elementos visuales de la aplicación y la interfaz gráfica.

### Controlador

Gestiona la comunicación entre la vista y la lógica del sistema.


