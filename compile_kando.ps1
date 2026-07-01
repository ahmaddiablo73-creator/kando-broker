emcc engine.cpp -O3 -s WASM=1 -s EXPORTED_FUNCTIONS=['_process_and_evolve'] -s EXTRA_EXPORTED_RUNTIME_METHODS=['ccall'] -o sedaram.js
