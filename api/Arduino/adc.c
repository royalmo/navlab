#include <avr/io.h>
#include "adc.h"

void  setup_ADC(uint8_t adc_input,uint8_t v_ref,uint8_t adc_pre){
  uint8_t adc,adcd,vref,pre;
  //adc_input (0-5 (default=5),8 Tª, 14 1.1V, 15 GND
  switch (adc_input){
  case 0 :adc=adc0;adcd=adc0d;break;
  case 1 :adc=adc1;adcd=adc1d;break;
  case 2 :adc=adc2;adcd=adc2d;break;
  case 3 :adc=adc3;adcd=adc3d;break;
  case 4 :adc=adc4;adcd=adc4d;break;
  case 5 :adc=adc5;adcd=adc5d;break;
  case 8 :adc=adc8;adcd=adcxd;break;
  case 14:adc=adc1_1V;adcd=adcxd;break;
  case 15:adc=adcgnd;adcd=adcxd;break;
  default:adc=adc5;adcd=adc5d;break;
  }

  // pull-up deactivated INITIAL VALUE is deactivated)
  switch (adc_input){
  case 0 :PORTC &=~(1<<PC0);break;
  case 1 :PORTC &=~(1<<PC1);break;
  case 2 :PORTC &=~(1<<PC2);break;
  case 3 :PORTC &=~(1<<PC3);break;
  case 4 :PORTC &=~(1<<PC4);break;
  case 5 :PORTC &=~(1<<PC5);break;
  default:PORTC &=~(1<<PC5);break;
  }
  
  //vref 0 (AREF), 1(1.1V), default=5 (5V)
  switch (v_ref){
  case 0:vref=vAREF;break;
  case 1:vref=v1_1V;break;
  case 5:vref=v5V;break;
  default:vref=v5V;break;
  }

  //adc_pre 2,4,8,default=16,32,64,128
  switch (adc_pre){
  case 2:pre=pre2;break;
  case 4:pre=pre4;break;
  case 8:pre=pre8;break;
  case 16:pre=pre16;break;
  case 32:pre=pre32;break;
  case 64:pre=pre64;break;
  case 128:pre=pre128;break;
  default:pre=pre16;break;
  }

  ADMUX  = vref|adc|adlar;
  ADCSRA = aden|pre;
  // disable digital input if needed
  DIDR0  = adcd;//DIDR0 | adcd;
}

uint8_t read8_ADC(){
  while (bit_is_set(ADCSRA, ADSC));
  return ADCH;
}

void start_ADC(){
  ADCSRA|=(1<<ADSC);
}
