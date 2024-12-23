CC = g++
RM = /bin/rm -rf

CFLAGS = -O3 -Wall

INCDIRS = -I.  
LIBDIRS = -L.
LIBS = -lGL -lGLEW -lglfw -lm

BIN = sample
SRCS = main.cpp 

OBJS = main.o 

${BIN}: ${OBJS}
	${CC} ${OBJS} ${LIBDIRS} ${LIBS} -o $@

%.o: %.cpp
	${CC} ${CFLAGS} ${INCDIRS} -c $< -o $@

.PHONY : clean remake
clean :
	${RM} ${BIN}
	${RM} ${OBJS}

remake : clean ${BIN}

depend:
	makedepend -- $(CFLAGS) -- -Y $(SRCS)
