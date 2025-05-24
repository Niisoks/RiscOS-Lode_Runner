CC = gcc
CFLAGS = -mlibscl -IOSLib: -std=c99 -Wall -Wextra -pedantic
LD = gcc
LDFLAGS = -mlibscl
LIBS = -LOSLib: -lOSLib32
OBJS = main.o entity.o wimp.o render.o enemy.o text.o menu.o config.o
RM = delete

application: $(OBJS)
	$(LD) $(LDFLAGS) -o $@ $^ $(LIBS)
	SetType $@ Absolute

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	$(RM) o.main
	$(RM) o.render
	$(RM) o.entity 
	$(RM) o.wimp
	$(RM) o.enemy
	$(RM) o.text
	$(RM) o.menu
	$(RM) o.config

#	$(RM) $(OBJS)
#	$(RM) application
