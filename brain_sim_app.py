from flask import Flask, render_template, request
import brain_model as bm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perform_surgery', methods=['GET', 'POST'])
def perform_surgery():

    # brain params
    brain_age = request.form['brainAges']
    brain_size = request.form['brainSizes']
    insertion_depth = request.form['insertionDepths']
    insertion_speed = request.form['insertionSpeeds']

    # microelectrode params
    electrode_type = request.form['electrodeTypes']
    cleanliness = request.form['cleanliness']
    texture = request.form['textures']

    # perform surgery simulation
    brain = bm.BrainModel(brain_age, brain_size, insertion_depth, insertion_speed)
    electrode = bm.Microelectrode(electrode_type, cleanliness, texture)
    deformation = brain.insert(electrode)

    return render_template('index.html', deformation_value=deformation)
