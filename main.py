import machine
import network
import socket

led = machine.Pin(2, machine.Pin.OUT)  # Assuming the LED is connected to GPIO pin 2

# Connect to your Wi-Fi network
ssid = "HUAWEI-BR4G-2G"
password = "PaRwGKd4"
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

# Wait until connected to the Wi-Fi network
while not station.isconnected():
    pass


# Print the assigned IP address
print('Network config:', station.ifconfig())


# Define the HTML content for the web page
html = """
<!DOCTYPE html>
<html>
<head>
    <title>ESP8266 LED Control</title>
    <style>
        body {
            background-color: #ffffff; /* white background */
            text-align: center;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #008000; /* green color */
        }
        button {
            background-color: #008000; /* green button */
            color: #ffffff; /* text color of the button */
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Hello Slido</h1>
    <p>Click the button to toggle the LED</p>
    <button onclick="toggleLed()">Toggle LED</button>
    <script>
        function toggleLed() {
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "/toggle", true);
            xhr.send();
        }
    </script>
</body>
</html>
"""

# Create a socket and bind it to a port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


# Respond to requests
while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)

    if 'toggle' in request:
        led.value(not led.value())  # Toggle the LED state

    response = html
    conn.send(response)
    conn.close()
