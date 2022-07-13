from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECRET_KEY'] = "nokey"

debug = DebugToolbarExtension(app)

@app.route('/')
def get_words():
    words = story.prompts
    return render_template('words_form.html', words = words)


@app.route('/rendered')
def build_phrase():
    phrase = story.generate(request.args)
    return render_template('rendered.html', phrase = phrase)