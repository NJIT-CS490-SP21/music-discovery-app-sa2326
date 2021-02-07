import os
import random

from flask import Flask, render_template
from get import get_music_data

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def music_discovery():
    rand = random.randint(0,2)
    #In respective order: Post Malone, Justin Bieber, Juice WRLD
    artists = ['246dkjvS1zLTtiykXe5h60', '1uNFoZAHBGtllmzznpCI3s', '4MCBfE4596Uoi2O4DtmEMz']
    my_music=get_music_data(artists[rand])
    
    return render_template(
        "index.html",
        num = rand,
        my_artists = artists,
        all_data=my_music['data'],
    )

app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)