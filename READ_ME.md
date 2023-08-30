Sport Scoring Application

The European Kendo Federation has reached out to you to create a sport scoring application for their coaches; this app would allow the user to create, edit, and remove teams; allow the user to create new games; allow the user to view all games for a team and all teams in a game; allow the user to see if a game was won or lost.

MVP:
- The app should allow the user to create, edit, and remove teams.
- The user should be able to create a new game.
- There should be able to display all games for a team and all teams in a game.
- The app should show if a game was won or lost.

Extensions:
- The app should allow the user to add players to their team and remove them. 
- The app should allow the user to delete a game. 
- The app should show if a game ended in a draw.
- The app should not allow the same team to be selected twice for one match.

Extended Extensions:
- The app should be able to display all players for a team.
- The app should show the different categories the individual players are competing in as well.
- The app should show a ranking of highest number of wins to lowest number of wins. 

Setup:
- Clone this report to your desktop
- Create a database named "sports_scoring" using the line:
createdb sports_scoring

- Run the code below:
psql -d sports_scoring -f db/sports_scoring.sql

- Run the console to populate the database:
python3 console.py

- Run Flask
python -m flask run