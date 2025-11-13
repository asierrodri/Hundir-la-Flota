# Hundir la Flota 🎯

Implementación en Python del clásico juego **Hundir la Flota** (Batalla Naval) para jugar por consola.

El objetivo del juego es adivinar la posición de los barcos del rival disparando coordenadas hasta hundirlos todos.

---

## 🧱 Estructura del proyecto

- `main.py` → Punto de entrada del programa. Gestiona el flujo principal de la partida.
- `clases.py` → Clases principales del juego (barcos, tableros, etc.).
- `funciones.py` → Funciones de apoyo (comprobaciones, colocación de barcos, disparos…).
- `variables.py` → Variables globales y configuraciones del juego.
- `.gitignore` → Archivos y carpetas ignoradas por Git.

---

## ▶️ Cómo ejecutar el juego

1. Clona el repositorio:

```bash
git clone https://github.com/asierrodri/Hundir-la-Flota.git
cd Hundir-la-Flota

2. Asegúrate de tener Python 3 instalado.

3. Ejecuta el juego:

'''bash
python main.py
'''

📌 Reglas básicas

El tablero se genera con los barcos colocados automáticamente.

El jugador introduce coordenadas para disparar.

El programa indica si has hecho agua, tocado o hundido.

La partida termina cuando se hunden todos los barcos.

🔧 Posibles mejoras futuras

Añadir modo de dos jugadores.

Mejorar la interfaz en consola (colores, mensajes, etc.).

Crear una versión con interfaz gráfica o API web.
