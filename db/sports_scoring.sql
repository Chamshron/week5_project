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
    team VARCHAR(255) REFERENCES teams(id) ON DELETE CASCADE 
);
