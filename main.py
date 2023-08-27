# Author: Maulik Davra
# Date: 08/27/2023
# Version: v1

# Importing required libraries
import openai
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from mangum import Mangum

# Initializing FastAPI app and Mangum handler
app = FastAPI()
handler = Mangum(app)

# Setting up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# List to store chat responses
chat_response = []

# Endpoint to serve the chat page
@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    # Render the home.html template and pass the chat responses
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_response})

# Initialize chat log with a system message
chat_log = [{'role': 'system',
             'content': 'You are a professional senior java developer, assist users with industry standard code practise \
              and advice given at senior level'
             }]

# Endpoint to handle chat interactions
@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    # Append user input to chat log and chat response list
    chat_log.append({'role': 'user', 'content': user_input})
    chat_response.append(user_input)

    # Generate a response using OpenAI's GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_log,
        temperature=.7
    )

    # Extract the bots response and append it to chat log and chat response list
    bot_response = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_response})
    chat_response.append(bot_response)

    # Render the home.html template and pass the updated chat responses
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_response})


# Endpoint to serve the image generation page
@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})


# Endpoint to handle image generation
@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):
    # Generate an image using OpenAI's API
    response = openai.Image.create(
        prompt=user_input,
        n=1,
        size="512x512"
    )

    # Extract the image URL from the response
    image_url = response['data'][0]['url']

    # Render the image.html template and pass the image URL
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})
