# ESP8266 LED Control Web Server

This project demonstrates how to control an LED on an ESP8266 (or similar microcontroller) using a simple web server. The server is hosted on the ESP8266, which connects to a Wi-Fi network and serves a webpage where the user can toggle an LED by clicking a button. 

## Features
- Connects to a Wi-Fi network.
- Serves a webpage with a button to toggle an LED.
- The webpage is styled with basic CSS for a simple user interface.
- The button on the webpage sends an HTTP request to toggle the LED's state.

## Requirements
- **Hardware:**
  - ESP8266 or similar microcontroller with Wi-Fi support.
  - LED connected to GPIO pin 2.

- **Software:**
  - MicroPython installed on the ESP8266.
  - Basic knowledge of networking and HTML.

## Installation and Setup

### Step 1: Set up your ESP8266
1. Flash MicroPython onto your ESP8266 device.
2. Connect the LED to GPIO pin 2 of the ESP8266.
3. Ensure that the ESP8266 is able to connect to a Wi-Fi network.

### Step 2: Modify the Code
1. Update the `ssid` and `password` variables with your Wi-Fi credentials.
   
   ```python
   ssid = "your-ssid"
   password = "your-password"
   ```
### Step 3: Upload the Script to the ESP8266
1. Upload the provided Python script to the ESP8266 using a suitable tool like ampy or rshell.
2. Once uploaded, run the script. The ESP8266 will connect to your Wi-Fi network and print its assigned IP address to the console.

### Step 4: Access the Web Interface
1. Open a browser and navigate to the IP address of your ESP8266 (printed in the console after the device connects to Wi-Fi).
2. You should see a webpage with a button labeled "Toggle LED". Clicking this button will toggle the LED on and off.


## Code Explanation
### 1. Wi-Fi Connection:

- The ESP8266 connects to the Wi-Fi network specified in the script using network.WLAN().
- The device waits until the connection is successful and then prints the assigned IP address.

### 2. Web Server:
- The ESP8266 hosts a simple HTTP server that listens for incoming requests on port 80.-
- When the user clicks the "Toggle LED" button, an HTTP request is sent to the server to toggle the LED.
- The server responds by serving an HTML page with a button and handling the toggle action.

### 3. HTML Page:
- The webpage displays a button that sends a GET request to /toggle when clicked.
-  Basic styling is applied to the page to make it visually simple but functional.

### 4. LED Control:
- The LED is connected to GPIO pin 2.
-  When the button is clicked, the LED's state is toggled by changing the output value of GPIO pin 2.

## Troubleshooting
- If the ESP8266 doesn't connect to Wi-Fi, check the SSID and password.
- If the LED doesn't toggle, ensure the LED is properly connected to GPIO pin 2 and that the code is running without errors.
- If the webpage doesn't load, ensure that the ESP8266 is correctly connected to the Wi-Fi network and check the IP address.
