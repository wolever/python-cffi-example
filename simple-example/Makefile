CC=clang

all: libadd.so add-example.exe _add_module.so

libadd.so: add.c
	${CC} -shared $< -o $@

add-example.exe: add-example.c add.h
	${CC} -L. -ladd $< -o $@

_add_module.so: build_add_module.py add.h libadd.so
	python $<

clean:
	rm add-example.exe *.so *.o
