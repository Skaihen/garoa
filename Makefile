all:
	g++ main.cpp -o Garoa -Wall -Wno-missing-braces -I src/include/ -L src/lib/ -lmingw32 -lSDL2main -lSDL2