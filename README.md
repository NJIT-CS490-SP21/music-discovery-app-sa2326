#Music Discovery App Milestone #1 documentation

Known problems:
1. Due to copyright issues, some songs may not have preview functionalities. This was taken into account when hardcoding list of artists; only artists with song preview links were selected.
2. There is a limited selection of songs and artists. The list of artists are hardcoded and therefore is limited in how many songs the app can recommend to the users.

Possible Additional features:
1. Room selection: upon entry to the app, users can be provided 4 different pictures of rooms with different moods. Possible choices can be the following: cozy and LED lit room, cafe with books, a club, and camping ground. This will be done with Javascript, CSS, HTML, and python code. Buttons, event listeners, CSS, and HTML will be used for user input page. Python code will be used to select music based on user input.
2. Artist information: there can be a feature to explore more about the artist when the 3 songs are shown to the users. Using the Spotify or Genius API, their information can be linked to their name when the 3 songs come up. This will be done through API calls in get.py file. 
3. Listing of album covers: upon entry, the app can list a bunch of albums without any other information. It would be up to the users to "judge an album by its cover" and decide to listen to its preview and learn more about it by clicking on it. Javascript, HTML, CSS needed. Multiple albums will be pulled from Spotify API and stored in an array. 

Technical Issues faced:
1. Hiding the API keys in .env files were not working for me and not giving me the access token. I used the blog post linked in HW5 question 1 (https://stmorse.github.io/journal/spotify-api.html) and tried to follow their code as close as possible to fix my issue.
2. It was hard to tell which indexes in the JSON object contained the information that I needed. To solve this, I used the JSON formatter (https://jsonformatter.curiousconcept.com/) to find what I needed.
3. Song previews were not showing up for couple artists that I had initially listed. I ended up manually looking artists up that had working preview links and editing my list of artists.
