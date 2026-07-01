CC=emcc
CFLAGS=-O3 -s WASM=1 -s EXPORTED_FUNCTIONS=['_process_and_evolve'] -s EXTRA_EXPORTED_RUNTIME_METHODS=['ccall']

all:
	emcc engine.cpp  -o sedaram.js
