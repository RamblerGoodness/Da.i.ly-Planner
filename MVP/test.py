import openai
import config

def generate_prompt(conversation):
    openai.api_key = config.api_key()  # Replace with your actual OpenAI API key
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=conversation,
        max_tokens=50,  # Adjust as per your needs
        temperature=0.7,  # Adjust as per your needs
    )
    choices = response.choices[0].text.strip()
    if choices:
        return choices
    else:
        return "No response received from the API."

# Set the initial context or message
initial_message = 'You are a chat bot used to plan out the users day. The user will input a time and a task and you will add it to the schedule.'

# Create the conversation history with the initial message
conversation = f'{initial_message}\n'

# Prompt the user for input and generate a response
while True:
    user_input = input("Enter a prompt: ")
    conversation += f'User: {user_input}\n'
    response = generate_prompt(conversation)
    conversation += f'system: {response}\n'
    print(response)
