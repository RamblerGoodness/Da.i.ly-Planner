from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'


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
    return jsonify({'time_prompt': time_prompt})


@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    time_prompt = request.form.get('time_checkbox')

    prompt = (f"create a detailed daily schedule for one day using JSON. I should use the value of {request.form['prompt']} as the prompt for the schedule and {time_prompt} as the time for each event. I need to remember that the events you mention are fixed and their times should not be changed. I should fill in the gaps in the schedule to ensure productivity. The JSON should be formatted with 'time' as the key and 'event' as the value ")
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=800
    )
    generated_text = response.choices[0].text.strip()
    json_data = {
        "8:00": "Wake up",
        "8:30": "Have breakfast",
        "9:00": "Brush your teeth",
        "9:15": "Take a shower",
        "9:45": "Take a bath",
        "10:00": "Get dressed",
        "10:30": "Go to school",
        "11:00": "Study English",
        "12:00": "Have lunch",
        "12:30": "Wash the dishes",
        "1:00": "Read a book",
        "2:00": "Do your homework",
        "3:00": "Cook dinner",
        "4:00": "Go to bed",
        "4:30": "Practice the guitar",
        "5:00": "Play with friends",
        "5:30": "Exercise",
        "6:00": "Brush your hair",
        "6:30": "Go shopping",
        "7:00": "Go for a walk",
        "7:30": "Take out the trash",
        "8:00": "Clean the house",
        "8:30": "Read the newspaper",
        "9:00": "Surf the internet",
        "9:30": "Water"
    }
    print(generated_text)
    return jsonify({'generated_text': generated_text, 'json_data': json_data})


if __name__ == '__main__':
    app.run(debug=True)
