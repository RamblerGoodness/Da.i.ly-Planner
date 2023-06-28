import openai
import config
openai.api_key = config.api_key()


def generate_prompt( input_prompt):

    prompt = (f"Turn this into my daily schedule for one day 'prompt', "
              f"remember that things i tell you are set, you do not modify their time, "
              f"but fill the gaps in the schedule to be productive"
              f"ask questions about the users day so you know what they already have planned"
              f"build a plan then clarify with the user if it is correct and update if not"
              f"if the user is finished then end the conversation and print the schedule in a readable format"
              f"if the user wants to change something then ask what they want to change and update the schedule"
              f"start by asking the user what time they want wake up and what time they go to sleep"
              f"recommend about 8 hours of sleep"
              f"do not take the role of the user and make decisions for them, wait for their input")
    prompt += input_prompt
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300
    )
    generated_text = response.choices[0].text.strip()
    prompt += response.choices[0].text.strip()

    return response.choices[0].text.strip()

while True:

    print(generate_prompt( input("Enter a prompt: ")))