#ifndef _ADC_
#define _ADC_

#include <stdint.h>

//ADMUX bits
#define refs1 0b10000000
#define refs0 0b01000000
#define adlar 0b00100000
#define mux3  0b00001000
#define mux2  0b00000100
#define mux1  0b00000010
#define mux0  0b00000001

//Multiplexor input MUX3|MUX2|MUX1|MUX0
#define adc0 0b0000
#define adc1 0b0001
#define adc2 0b0010
#define adc3 0b0011
#define adc4 0b0100
#define adc5 0b0101
#define adc6 0b0110
#define adc7 0b0111
#define adc8 0b1000 //temperature sensor
#define adc1_1V 0b1110 //14
#define adcgnd  0b1111 //15

//Voltage Reference REFS1|REFS0
#define vAREF 0b00000000
#define v5V   0b01000000
#define v1_1V 0b11000000

//ADCSRA bits
#define aden    0b10000000
#define adsc    0b01000000
#define adps2   0b00000100
#define adps1   0b00000010
#define adps0   0b00000001

// prescaler ADSP2|ADSP1|ADSP0
#define pre2   0b001
#define pre4   0b010
#define pre8   0b011
#define pre16  0b100
#define pre32  0b101
#define pre64  0b110
#define pre128 0b111

//DIDR0 combinations
//to disable two digital inputs
//inputs DIDR0=adc5d|adc4d
#define adc5d 0b00100000
#define adc4d 0b00010000
#define adc3d 0b00001000
#define adc2d 0b00000100
#define adc1d 0b00000010
#define adc0d 0b00000001
#define adcxd 0b00000000

void setup_ADC(uint8_t adc_input,uint8_t v_ref,uint8_t adc_pre);
//adc_input (0-5 (default=5),8 Tª, 14 1.1V, 15 GND
//v_ref 0 (AREF), 1(1.1V), default=5 (5V)
//adc_pre 2,4,8,16(default),32,64,128
uint8_t read8_ADC();
void start_ADC();

#endif
