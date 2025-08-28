# ESP32 I2S Microphone Tester for INMP441

This project provides a simple way to test an INMP441 I2S microphone with an ESP32 development board using MicroPython.

## Wiring

Connect the INMP441 to your ESP32 board as follows:

| INMP441 Pin | ESP32 Pin |
| ----------- | --------- |
| VDD         | 3.3V      |
| GND         | GND       |
| L/R         | GND       |
| SCK         | GPIO32    |
| WS          | GPIO25    |
| SD          | GPIO33    |

**Note on L/R pin:** Connecting the L/R pin to GND selects the left channel. If you want to use the right channel, connect it to VDD. For stereo, you would need to use two microphones and a different script.

## Firmware

This project requires a MicroPython firmware version that includes the `I2S` module. You can download the latest firmware from the [MicroPython website](https://micropython.org/download/esp32/). Make sure to select a stable version that includes I2S support.

To flash the firmware to your ESP32, you can use the `esptool` utility. You can find instructions on how to do this in the [ESP32 documentation](https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html).
Sample Code: esptool erase_flash # start new 
esptool --baud 460800 write_flash 0x1000 ESP32_GENERIC-20250809-v1.26.0.bin #flash the downloaded firmware from Micropython https://micropython.org/download/ESP32_GENERIC/


## Running the Test

1.  Connect the ESP32 to your computer.
2.  Upload the `src/main.py` file to the root directory of your ESP32's filesystem. You can use a tool like Thonny IDE to do this. Start Thonny from the command line - type thonny Go to Tools -> options -> Interperter and select MicroPython (ESP32) save the code to the device as main.py and click run
3.  Open a serial terminal connected to your ESP32. (at the bottom of Thonny)
4.  Reset the ESP32.
5.  The script will start running automatically. You should see output in the terminal indicating that the I2S interface has been initialized and that audio samples are being read.

## ESP32-S3-DevKitC-1

If you are using an ESP32-S3-DevKitC-1, the pinout will be different. You will need to consult the pinout diagram for your specific board and modify the `I2S_SCK_PIN`, `I2S_WS_PIN`, and `I2S_SD_PIN` variables in the `src/main.py` script accordingly.

## Troubleshooting

*   **No output:** Make sure the wiring is correct and that the ESP32 is properly flashed with MicroPython.
*   **Garbled output:** The I2S settings (sample rate, bits per sample) might be incorrect for your microphone. Check the INMP441 datasheet for the correct values.
*   **"I2S" not defined:** Your MicroPython firmware does not include the `I2S` module. Make sure you have downloaded a version that supports I2S.
