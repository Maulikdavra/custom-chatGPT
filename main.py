import openai

chat_log = []

while True:

    user_input = input()

    if user_input.lower == 'stop':
        break

    chat_log.append({'role': 'user', 'content': user_input})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_log,
        temperature=.7
    )

    bot_response = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_response})
    print(bot_response)

