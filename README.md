# Personal AI Chatbot

Author
Maulik Davra

Date
08/27/2023

Version
v1

Overview
This project is a personal AI chatbot built using FastAPI and OpenAI's GPT-3.5 Turbo. The chatbot provides a simple interface for users to interact with it and also has an image generation feature.

Features
Text-based chat with the AI chatbot
Image generation based on user input
Built with FastAPI for high performance
Uses OpenAI's GPT-3.5 Turbo for chat and image generation
Installation
Requirements
Python 3.x
FastAPI
OpenAI Python package
Mangum
Steps
Clone the repository
Install the required packages
bash
Copy code
pip install fastapi openai mangum
Run the FastAPI server
bash
Copy code
uvicorn main:app --reload
Usage
Chat
Open your browser and navigate to http://localhost:8000/
Type your message in the text area and click "Send" to chat with the bot.
Image Generation
Navigate to http://localhost:8000/image
Type your input in the text area and click "Send" to generate an image.
Code Structure
main.py
app: FastAPI application instance
handler: Mangum handler for AWS Lambda
chat_response: List to store chat responses
chat_page(): Endpoint to serve the chat page
chat_log: Initial chat log with a system message
chat(): Endpoint to handle chat interactions
image_page(): Endpoint to serve the image generation page
create_image(): Endpoint to handle image generation
HTML Templates
image.html: Template for the image generation page
navbar.html: Navigation bar template
layout.html: Layout template
home.html: Template for the chat page
License
MIT License

