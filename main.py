import openai


response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{
        'role': 'system',
        'content': 'You are a helpful assistant'
    },

        {
            'role': 'user',
            'content': 'List out all the necessary/required skills/technical-skills for a junior java developer'
        }],
    temperature=.7
)

print(response['choices'][0]['message']['content'])
