# 🚀 Space Game - Práctica 3

**Autor:** Pablo Illescas  
**Versión:** 1.0  
**Tecnología:** Python + Pygame (-ce)

---

## 🎮 Descripción del Juego
Un arcade shooter espacial donde controlas una nave con sistema de propulsión avanzada. El juego cuenta con una arquitectura de estados que incluye pantalla de título, modo de pausa y reinicio automático de estadísticas.

## 🕹️ Controles de Vuelo

| Acción | Tecla / Control |
| :--- | :--- |
| **Moverse** | `W`, `A`, `S`, `D` / **Flechas de Dirección** |
| **Disparar / Iniciar** | `Espacio` |
| **Turbo (Sprint)** | `L-Shift` (Shift Izquierdo) |
| **Pausar Juego** | `P` |
| **Menú / Salir** | `Esc` |

---

## ✨ Características Técnicas
* **Gestión de Estados:** Soporta transiciones fluidas entre Menú -> Juego -> Pausa.
* **Audio Pro:** * Música de fondo persistente para cada estado.
    * Canal de sonido exclusivo para el motor con detección de movimiento.
    * Mezcla de efectos de sonido dinámicos para disparos.
* **Renderizado:** * Mosaico de fondo (Tiled background) infinito.
    * UI dinámica alineada a la derecha con manejo de `Rect`.
    * Limitación de 60 FPS estables.

---

## 🛠️ Requisitos e Instalación

1.  **Python 3.x** instalado.
2.  **Librería Pygame:**
    ```bash
    pip install pygame
    ```

## 📁 Estructura de Carpetas
Para el correcto funcionamiento, el proyecto debe estar organizado así:
```text
/
├── main.py
├── audio/
│   ├── Title Screen.wav
│   ├── Level 1.wav
│   ├── laser.ogg
│   └── thruster.ogg
├── sprites/
│   ├── ship.png
│   ├── bg.png
│   └── titleBG.jpg
└── fonts/
    ├── kenvector_future.ttf
    └── future-earth.ttf