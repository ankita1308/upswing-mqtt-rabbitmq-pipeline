## 1. Installation

Before installing RabbitMQ, ensure that its dependencies are met. Additionally, for Windows systems, make sure you have a 64-bit supported version of Erlang installed.

-> Install RabbitMQ from the official website. Ensure that you download the appropriate version for your operating system.

## 2. Starting RabbitMQ Server

### Set Up System Path:

Add the RabbitMQ directory to your system path. This directory is typically located at `C:\Program Files\RabbitMQ Server\rabbitmq_server-3.13.0\sbin`.

### Starting RabbitMQ Server:

- Open Command Prompt:
  - Press `Win + R`, type `cmd`, and press Enter.

- Navigate to the RabbitMQ Installation Directory (if needed):

- Start the RabbitMQ server:   
- Visit `http://localhost:15672/` in your web browser to access the RabbitMQ management interface. If you encounter issues accessing the interface, try restarting your system and accessing the link again.

## 3. Install Virtualenv (if not already installed):
- If you haven't installed virtualenv yet, you can install it   using pip: `pip install virtualenv`

## 4. Create a Virtual Environment:
- Navigate to the directory where you want to create the virtual environment and run: `virtualenv venv`

## 5. Activate the Virtual Environment:

Windows: `venv\Scripts\activate`

## 6. Install all dependencies from requirements.txt file:
Using: `pip install -r requirements.txt`

## 7. Run Your Code
Execute your code using `py main.py` in your terminal.