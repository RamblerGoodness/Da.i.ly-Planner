import openai
import config
openai.api_key = config.api_key()


def generate_prompt():

    prompt = (f"Turn this into my daily schedule for one day 'prompt', "
              f"remember that things i tell you are set, you do not modify their time, "
              f"but fill the gaps in the schedule to be productive")
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300
    )
    generated_text = response.choices[0].text.strip()

    return response

print(generate_prompt())