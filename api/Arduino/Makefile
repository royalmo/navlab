CC=avr-gcc
CFLAGS= -std=c99 -Os -mmcu=atmega328p -fshort-enums -Ilibpbn  
CPPFLAGS=-DF_CPU=16000000UL	
LDFLAGS= -std=c99 -mmcu=atmega328p -fshort-enums 
OBJCOPY=avr-objcopy
DEV_ACM0=/dev/ttyACM0
DEV_USB0=/dev/ttyUSB0
DUDE=avrdude -c arduino -p atmega328p -P
PRINCIPAL = main
TARNAME = pract-$(NPRACT)-equip-$(NEQUIP)

vpath lib% libpbn

.PHONY: clean veryclean release picocom

clean:
	\rm -f *~ *.o *.s *.hex

veryclean: clean
	\rm -f $(PRINCIPAL)

picocom:
	picocom /dev/ttyACM0

%.hex: %
	$(OBJCOPY) -Oihex $< $@ 

injecta_ACM0_%: %.hex
	$(DUDE) $(DEV_ACM0) -U $<

injecta_USB0_%: %.hex
	$(DUDE) $(DEV_USB0) -U $<

main: main.o adc.o -lpbn
main.o: main.c adc.c adc.h

adc.o: adc.c adc.h