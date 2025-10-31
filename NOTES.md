# Project Notes

## Borrowed Equipment:
- Raspberry Pi 3 (#08)
- Elegoo Uno R3 Controller Board plus additional USB cable
- STM32 Nucleo-L476RG
- Elegoo Electronics Fun Kit
- Bojack DHT11 Temperature & Humidity Sensor with wires

## Week of 10/31 Progress
- (Re)configured my Raspberry Pi (headless setup):
    - I can now ssh into it from my house's local network
- Installed Arduino IDE and wrote basic program for Arduino to light different color LEDs based on temperature data from DHT11 (verified that it worked)
- Wrote basic program for Pi to light different color LEDs based on temperature data from BME280
    - Followed [this familiar tutorial](https://randomnerdtutorials.com/raspberry-pi-bme280-python/) for a refresher on how to setup the BME280 with my Raspberry Pi
- Started [Official STM32 Tutorial](https://wiki.st.com/stm32mcu/wiki/STM32StepByStep:Getting_started_with_STM32_:_STM32_step_by_step): 
    - Installed their entire recommended ecosystem, including STM32CubeIDE
    - Currently stuck on Step 5; my screen looks different