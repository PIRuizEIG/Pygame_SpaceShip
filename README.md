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
* **Gestión de Eventos:** Temporizadores sincronizados con el estado del juego (los enemigos no se generan en pausa).
* **Audio:**
    * Música de fondo persistente para cada estado.
    * Canal de sonido exclusivo para el motor con detección de movimiento.
    * efectos de sonido para disparos y explosiones.
* **Renderizado:**
    * Mosaico de fondo (Tiled background) infinito.
    * UI dinámica alineada a la derecha con manejo de `Rect`.
    * Limitación de 60 FPS estables.

---

## 🛠️ Requisitos e Instalación

1.  **Python 3.x** instalado.
2.  **Librería Pygame:**
    ```bash
    pip install pygame
    ```
    o **Librería Pygame Community:**
    ```bash
    pip install pygame-ce
    ```
## Ejecución

```bash
python shipGame.py
```

## 📁 Estructura de Carpetas
Para el correcto funcionamiento, el proyecto debe estar organizado así:
```text
/
├── shipGame.py
├── audio/
│   ├── Explosion.wav
│   ├── laser.ogg
│   ├── Level 1.wav
│   ├── thruster.ogg
│   └── Title Screen.wav
├── sprites/
│   ├── bg.png
│   ├── enemy.png
│   ├── ship.png
│   └── titleBG.jpg
└── fonts/
    ├── future-earth.ttf
    └── kenvector_future.ttf
