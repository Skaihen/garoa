all:
	g++ *.cpp -o Garoa -Wall -m64 -I src/include/ -L src/lib/ -lmingw32 -lSDL2main -lSDL2