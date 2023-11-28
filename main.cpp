#include <iostream>
#include <SDL2/SDL.h>

int main(int argc, char* argv[]) {
    // Inicializar SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        std::cerr << "Error al inicializar SDL: " << SDL_GetError() << std::endl;
        return 1;
    }
 
    // Crear una ventana
    SDL_Window* window = SDL_CreateWindow(
        "Garoa",
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        800,
        600,
        SDL_WINDOW_SHOWN
    );

    if (window == nullptr) {
        std::cerr << "Error al crear la ventana: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    // Variable para controlar el bucle principal
    bool running = true;
    SDL_Event event;
 
    while (running) {
        // Procesar la cola de eventos
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }
    }
 
    // Limpiar y cerrar
    SDL_DestroyWindow(window);
    SDL_Quit();
 
    return 0;
}