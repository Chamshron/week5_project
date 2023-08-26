DROP TABLE match_score;
DROP TABLE matches;
DROP TABLE players;
DROP TABLE teams;

CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    score INT
);

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    grade INT,
    team INT REFERENCES teams(id) ON DELETE CASCADE 
);

CREATE TABLE matches(
    id SERIAL PRIMARY KEY,
    team_a INT REFERENCES teams(id) ON DELETE CASCADE,
    team_b INT REFERENCES teams(id) ON DELETE CASCADE,
    match_date VARCHAR(255)
);

CREATE TABLE match_score(
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    match_id INT REFERENCES matches(id) ON DELETE CASCADE,
    result VARCHAR(255)
);