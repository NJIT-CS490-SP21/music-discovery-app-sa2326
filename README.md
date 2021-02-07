#Music Discovery App Milestone #1 documentation

Known problems:
1. Due to copyright issues, some songs may not have preview functionalities. This was taken into account when hardcoding list of artists; only artists with song preview links were selected.

Possible Additional features:
1. List multiple songs from an artist. Instead of displaying only one song, there can be multiple songs listed. The top song will look bigger than the other trailing recommended songs. Music.py and Get.py will need to be adjusted to pull multiple songs. Style.css will help with displaying top song bigger than others.
2. Genre selection. Top songs from different artists can be recommended using user input of a genre selection. This can be done by creating buttons on index.html and reading user input through Javascript. Style.css can be used for UI.

Technical Issues faced:
1. Hiding the API keys in .env files were not working for me and not giving me the access token. I used the blog post linked in HW5 question 1 (https://stmorse.github.io/journal/spotify-api.html) and tried to follow their code as close as possible to fix my issue.
2. It was hard to tell which indexes in the JSON object contained the information that I needed. To solve this, I used the JSON formatter (https://jsonformatter.curiousconcept.com/) to find what I needed.
2. Song previews were not showing up for the three artist that I had initially listed. I ended up manually looking artists up that had working preview links and editing my list of artists.
