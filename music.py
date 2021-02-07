import os
import random

from flask import Flask, render_template
from get import get_music_data

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def music_discovery():
    rand = random.randint(0,2)
    #In respective order: Bazzi, Frocious, Pink Sweat$
    artists = ['4GvEc3ANtPPjt1ZJllr5Zl', '0W96fH9CZR4WRGI4x3iBJs', '1W7FNibLa0O0b572tB2w7t']
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