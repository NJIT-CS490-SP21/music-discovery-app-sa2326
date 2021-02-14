import os
import random

from flask import Flask, render_template
from get import get_music_data, get_lyrics

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def music_discovery():
    rand = random.randint(0,8)
    #In respective order: Bazzi, Frocious, Pink Sweat$
    artists = [ '4GvEc3ANtPPjt1ZJllr5Zl', '0W96fH9CZR4WRGI4x3iBJs', '1W7FNibLa0O0b572tB2w7t',
        '2pAWfrd7WFF3XhVt9GooDL', '2s1fodCLf7tb0bogSUNBqY', '0TImkz4nPqjegtVSMZnMRq', '68DWke2VjdDmA75aJX5C57',
        '6gWGD0yeQYobb2sq0LUr7k', '5eIbEEQnDM8yuDVB0bimSP']
    my_music=get_music_data(artists[rand])
    music_data=my_music['data']
    song_title=music_data[0]
    
    my_lyrics_url=get_lyrics(song_title)
    
    return render_template(
        "index.html",
        all_data=music_data,
        lyrics=my_lyrics_url['lyrics_url']
    )

app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

