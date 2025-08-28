from machine import I2S, Pin
import time

# I2S pin configuration
I2S_ID = 0
I2S_SCK_PIN = 32
I2S_WS_PIN = 25
I2S_SD_PIN = 33

# Audio configuration
I2S_SAMPLE_RATE = 16000
I2S_NUM_CHANNELS = 1 # Mono
I2S_BITS_PER_SAMPLE = 16

def setup_i2s():
    """
    Initializes the I2S interface for the INMP441 microphone.
    """
    sck_pin = Pin(I2S_SCK_PIN)
    ws_pin = Pin(I2S_WS_PIN)
    sd_pin = Pin(I2S_SD_PIN)

    audio_in = I2S(
        I2S_ID,
        sck=sck_pin,
        ws=ws_pin,
        sd=sd_pin,
        mode=I2S.RX,
        bits=I2S_BITS_PER_SAMPLE,
        format=I2S.MONO,
        rate=I2S_SAMPLE_RATE,
        ibuf=40000,
    )
    return audio_in

def main():
    """
    Main function to read and print audio samples from the microphone.
    """
    print("Initializing I2S...")
    audio_in = setup_i2s()
    print("I2S Initialized.")

    # Create a buffer to store the audio samples
    samples = bytearray(1024)

    print("Reading audio samples...")
    while True:
        try:
            # Read audio samples from the I2S interface
            num_read = audio_in.readinto(samples)
            if num_read > 0:
                # Calculate RMS of the samples
                sum_sq = 0
                num_samples = num_read // 2
                for i in range(0, num_read, 2):
                    # Combine two bytes to a 16-bit signed integer (little-endian)
                    sample = (samples[i+1] << 8) | samples[i]
                    if sample > 32767: # convert to signed
                        sample -= 65536
                    sum_sq += sample * sample

                mean_sq = sum_sq / num_samples
                rms = mean_sq ** 0.5
                print("RMS:", int(rms))

            time.sleep_ms(10) # Lower sleep time for more responsive output
        except KeyboardInterrupt:
            print("Stopping...")
            break
        except Exception as e:
            print("Error:", e)
            break

    # Deinitialize the I2S interface
    audio_in.deinit()
    print("I2S deinitialized.")

if __name__ == "__main__":
    main()
