
# Juego de la Vida de Conway (Conway's Game of Life)

Este proyecto es una implementación en Python del famoso autómata celular creado por John Conway. El sistema simula la evolución de una población de células sobre una grilla bidimensional aplicando reglas simples pero capaces de generar comportamientos complejos.

---

## Descripción general

Cada celda puede estar **viva (1)** o **muerta (0)**. Su evolución depende del número de vecinos vivos que tenga. Las reglas se aplican simultáneamente a todas las celdas en cada "generación".

### Reglas del juego

1. **Soledad:** Una celda viva con menos de 2 vecinos vivos muere.
2. **Superpoblación:** Una celda viva con más de 3 vecinos vivos muere.
3. **Supervivencia:** Una celda viva con 2 o 3 vecinos sobrevive.
4. **Reproducción:** Una celda muerta con exactamente 3 vecinos vivos revive.

<!-- ---

## 📦 Estructura del proyecto

```
📁 game_of_life_project/
├── game_of_life.py       # Clase con la lógica del juego
├── main.py               # Script principal que ejecuta y anima el juego
├── performance_test.py   # Archivo para medir rendimiento (ver más abajo)
├── README.md             # Este archivo
├── 📁 captures/          # Aquí puedes guardar capturas o gifs de tus simulaciones
└── 📁 results/           # Para guardar gráficas de rendimiento y tiempos
```

--- -->
## Cómo ejecutar el juego

1. Instala las dependencias (recomendado en un entorno virtual):

```bash
pip install numpy matplotlib
```

2. Ejecuta el juego con animación:

```bash
python main.py
```

Esto abrirá una ventana con la animación del juego en tiempo real.

---

## 📸 Cómo agregar pruebas de que el código funciona

1. Toma capturas de la animación en ejecución.
2. Guarda esas imágenes o gifs en la carpeta `captures/`.
3. Luego puedes referenciar esas imágenes aquí mismo:

```markdown
### Glider funcionando:
![glider](captures/glider.png)
```

---

## ⏱️ Pruebas de rendimiento (6.3)

Para cumplir con el análisis empírico, se recomienda lo siguiente:

1. Crear un script `performance_test.py` que haga lo siguiente:
   - Ejecute el juego en grillas de diferentes tamaños: 32x32, 64x64, 128x128, ..., 1024x1024.
   - Mida el tiempo promedio de ejecución por iteración usando `timeit`.
   - Genere una gráfica de tiempo promedio vs número total de celdas.
   - Incluya una visualización log-log.

2. Guarda las gráficas generadas en la carpeta `results/` y referencia aquí:

```markdown
### Gráfica de rendimiento (log-log):
![rendimiento](results/loglog_plot.png)
```

---

## 🧪 Análisis y discusión (6.4)

Al final, asegúrate de reflexionar sobre:

- ¿Cómo escala la implementación?
- ¿Hay cuellos de botella?
- ¿Tu implementación es eficiente?
- ¿Cómo se compararía con una versión paralela?
- ¿Qué mejoras podrías implementar?

Incluye tus conclusiones como texto final o en un archivo `ANALISIS.md`.

---

## ✍️ Autor

- Nombre: *(tu nombre aquí)*
- Curso: Computación Paralela y Distribuida
- Fecha: Junio 2025
