import serial
import time

# Configure Serial Port
serial_port = "/dev/ttyUSB0"  # LED Client
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:
            received_signal = ser.readline().strip().decode('utf-8')
            print(f"📥 Received: {received_signal}")

            if received_signal == "GAMESTART":
                ser.write(b"2\n")
                print("📤 Sent: 2 to /dev/ttyUSB0")

except KeyboardInterrupt:
    print("🔴 Stopping LED Client")
finally:
    ser.close()
