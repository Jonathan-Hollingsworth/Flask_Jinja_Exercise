from stories import Story
from flask import Flask, request, render_template
from random import choice

app = Flask(__name__)

story = Story(
    ["noun", "adverb", "adjective", "3rd_person_pronoun", "intransitive_verb"],
    """What shall we do with the {adjective} {noun}, 
       What shall we do with the {adjective} {noun},
       What shall we do with the {adjective} {noun},
       {adverb} in the morning?
       Hoo-ray and up {3rd_person_pronoun} {intransitive_verb},
       Hoo-ray and up {3rd_person_pronoun} {intransitive_verb},
       Hoo-ray and up {3rd_person_pronoun} {intransitive_verb},
       {adverb} in the morning."""
)

@app.route('/')
def madlib():
    "generates madlib prompts depending on the story"
    return render_template("madlibs.html", prompts=story.prompts)

@app.route('/story')
def generate_story():
    "Generates and shows the final story"
    args = request.args
    madlib = story.generate(args)
    return render_template("story.html", story=madlib)