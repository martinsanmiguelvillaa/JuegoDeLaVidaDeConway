# Juego de la Vida de Conway — Python & Pygame

Implementación interactiva del **Juego de la Vida de Conway** desarrollada en Python utilizando Pygame.

El proyecto permite simular autómatas celulares en tiempo real, editar el tablero manualmente y controlar la evolución del sistema con distintas herramientas de interacción.

## Descripción

El Juego de la Vida es un autómata celular propuesto por John Conway donde cada célula evoluciona según reglas simples basadas en sus vecinos.

Esta implementación permite:

- Simulación en tiempo real
- Edición manual del tablero
- Control de velocidad
- Copiado y restauración de estados
- Interfaz visual interactiva

## Controles

| Tecla | Acción |
|------|-------|
| Click | Activar/desactivar célula |
| Espacio | Pausar / reanudar simulación |
| R | Reiniciar tablero |
| ↑ | Aumentar velocidad |
| ↓ | Disminuir velocidad |
| C | Copiar estado actual |
| V | Pegar copia guardada |
| T | Volver al último estado pausado |
| Esc | Salir |

<img width="997" height="799" alt="image" src="https://github.com/user-attachments/assets/6c51f447-4168-499c-8b5b-29bec7edc488" />

## Estructura del proyecto

- `interfaz.py` → interfaz gráfica y controles  
- `logica_juego.py` → reglas del juego y evolución del tablero  

## Ejecutar

Clonar el repositorio y ejecutar:

```bash
python interfaz.py
