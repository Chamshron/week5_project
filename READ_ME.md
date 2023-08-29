Sport Scoring Application

This is a Sport Scoring application that provides the European Kendo League the main functions you would expect of a score keeping app; allow the user to create, edit, and remove teams; allow the user to create new games; allow the user to view all games for a team and all teams in a game; allow the user to see if a game was won or lost.

MVP:
- The app should allow the user to create, edit, and remove teams.
- The user should be able to create a new game.
- There should be a way to display all games for a team and all teams in a game.
- The app should show if a game was won or lost.

Extensions:
- The app should allow the user to add players to their team and remove them. 
- The app should allow the user to delete a game. 

Extended Extensions:
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