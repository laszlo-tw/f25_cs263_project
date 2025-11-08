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

 ## Week of 11/7 Progress
 - I wasn't having much luck with the Official STM32 Tutorial so I switched to a very commprehensive and informative tutorial on YouTube. Here are my notes:

[Starting with STM32 - Programming Tutorial for Beginners](https://www.youtube.com/watch?v=dnfuNT1dPiM) by Robert Feranec on Youtube
1. Install and launch the STM32CubeIDE
    - starting the IDE will prompt you to select a directory to use as a workspace. Choose whichever you'd like.
    - A workspace may contain many projects, but you typically will use separate workspaces for different projects, and you can have multiple sub-projects within each.
2. Create a project and get your bearings
    1. Click "Create a New STM32 Project".
    2. Indicate your hardware. You would use the MCU/MPU Selector tab for a custom board. In our case, we have an STM32 provided board, so we use the Board Selector tab. Enter board name (in my case, "STM32 Nucleo-L476RG") into the search bar. Select the correct result and click "Next".
    3. Click "Finish" to accept the default Firmware Library Package Setup and initialize all peripherals with their default Mode.
        - What this means is that instead of starting from scratch, you get STM32's user-friendly custom drivers and HAL package for this particular product. The downside is that the comprehensive HAL code may include a lot of extra code that your project might not need, slowing down your interface. Eventually, you can build and use your own drivers, throwing out all the extra code to make your system more efficient--especially if you are working on a very tiny and critical system.
3. Starting the project will load in the IOC (`.ioc` file), a GUI that shows your chip configuration.
    - It comes pre-configured, and you can add your own configurations.
        - You can even change the system clock frequency in the Clock tab to save power, for example in power-efficient systems.
    - You can download the open-source schematics for your board for comparison/reference. I found mine [here](https://www.st.com/en/evaluation-tools/nucleo-l476rg.html#cad-resources).
    - Close the IOC window; don't save any changes for now.
4. Exploring the project tree
    - `/Core/`: Contains most of your project. Note the header files in `/Core/Inc/` and `main.c` in `/Core/Src/`. You can see where you will add your code between `/* USER CODE BEGIN */` and `/* USER CODE END */` comments--if you place code outside of those sections, you will lose it upon regenerating code through the `.ioc` file. There are also some auto-generated modules in `stm32l4xx_hal_msp.c` and `stml4xx_it.c` that were noted in the tutorial. The `/Startup/` directory contains startup code. For example, `startup_stm32l476rgtx.s` contains interrupt mapping, memory address areas, etc.
    - `/Drivers/`: Contains auto-generated drivers mentioned before during project configuration. You generally don't need to modify these, but it may be helpful to investigate the code.
    - A helpful programming tool is to right click a function and click "Open Declaration" on the dropdown that appears.
    - You can also look at the header files under `/Inc/` for function definitions and explanations.
    - You can also find HAL documentation for your board online. I found mine [here](https://www.st.com/resource/en/user_manual/um1884-description-of-stm32l4l4-hal-and-lowlayer-drivers-stmicroelectronics.pdf).
5. Moving on to the main task: making the built-in LED blink
    - Earlier we saw in the IOC interface that the built in LED was pin PA5.
    - Navigate to the `main` function in `/Core/Src/main.c`.
    - We see that configuration happens first (HAL initialization, system clock configuration, GPIO configuration, and UART interface configuation), then a while loop is entered.
    - We want to repeatedly turn the LED on and off in the infinite loop using GPIO configuration. We use these two functions:
        - `HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET)` -- see `project/Drivers/STM32L4xx_HAL_Driver/Inc/stm32l4xx_hal_gpio.h` for documentation
        - `void HAL_Delay(uint32_t Delay)` -- see `project/Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal.c`, where you will also find other helpful functions.
    - Code added to while loop:
```
HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_SET); // LED ON
HAL_Delay(1000);
HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_RESET); // LED OFF
HAL_Delay(1000);
```
6. Connect the board
    - Connect the board to your computer using USB Type-A to Mini-B cable
    - For your first time, navigate to Help --> ST-LINK Upgrade. Click "Open in update mode". This upgrades the old firmware that came on your device to update the debugging interface on the board. (Part of the board, including a second chip, is a debugger interface.) If you use a custom board, you will have to figure out other solutions.
7. Build and launch
    - You have two options here:
       1. Green play button symbol: Run as
       2. Hammer symbol: Build project. Then, Run.
    - A console appears and it should tell you that your build is finished.
    - A configuration window pops up that you would only really touch if you have a custom board.
    - You should see the LED blinking on your board.
   
Next time I will finish the tutorial (unfortunately I was really busy this week and didn't have as much time as I would've liked to work on this project), where they go through an interrupt code example.
