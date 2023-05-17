#include <pbn.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "adc.h"

#define debugging false

#if debugging
#define debug(m) (void)(print(m))
#define debug_put(m) (void)(serial_put(m))
#else
#define debug(m)
#define debug_put(m)
#endif


char input_string[40] = {'\0'};
uint8_t pointer = 0;

static bool led_status;

static pin_t led_builtin;
static pin_t led_shield;


int main(){
    setup_ADC(1,5,16);//(adc_input,v_ref,adc_pre)
    start_ADC();//actual value will be read next sampling time
    led_builtin = pin_create(&PORTB,5,Output); // LED_BUILTIN (13) de l'Arduino UNO
    led_shield = pin_create(&PORTD,5,Output); // LED de l'Arduino shield
    pin_w(led_builtin,false);
    pin_w(led_shield,false);
    serial_open();
    sei();
    char input_char;
    while(1){
        // Esperem una nova recepció
        while(!serial_can_read());
        // Gestionem la recepció del caràcter rebut
        input_char = serial_get();
        debug("He rebut: ");
        debug_put(input_char);
        debug("\n\r");

        if (input_char=='%'){
            pointer = 0;
        }
        else{
            input_string[pointer]=input_char;
            pointer+=1;
        }
        input_string[pointer]='\0';
        // Comprovem si hem rebut un missatge conegut
        if (strcmp(input_string,"L0")==0){
            pin_w(led_builtin,false);
            pin_w(led_shield,false);
            led_status = false;
            print("%0\n\r");
        }
        else if (strcmp(input_string,"L1")==0){
            pin_w(led_builtin,true);
            pin_w(led_shield,true);
            led_status = true;
            print("%1\n\r");
        }
        else if (strcmp(input_string,"L?")==0){
            print("%");
            if (led_status){
                print("1\n\r");
            }
            else{
                print("0\n\r");
            }
        }
        else if (strcmp(input_string,"P?")==0){
            start_ADC();
            print("%");
            char str[4];
            sprintf(str, "%d", read8_ADC());
            print(str);
            print("\n\r");
            start_ADC();
        }
        debug("Actualment string:");
        debug(input_string);
        debug("\n\r");
        
        
    }
    serial_close();
}
