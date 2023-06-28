from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '###'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sort_time', methods=['POST'])
def sort_time():
    checkbox_value = request.form.get('time_checkbox')
    if checkbox_value:
        time_prompt = 'Make sure to sort them by time'
    else:
        time_prompt = 'They do not need to be sorted by time'


@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    time_prompt = request.form.get('time_checkbox')

    prompt = (f"Turn this into my daily schedule for one day {request.form['prompt']} {time_prompt}, "
              f"remember that things i tell you are set, you do not modify their time, "
              f"but fill the gaps in the schedule to be productive")
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300
    )
    generated_text = response.choices[0].text.strip()

    return render_template('index.html', generated_text=generated_text)


if __name__ == '__main__':
    app.run(debug=True)
