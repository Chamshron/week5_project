DROP TABLE matches CASCADE;
DROP TABLE players CASCADE;
DROP TABLE teams CASCADE;

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
    team_id INT REFERENCES teams(id) ON DELETE CASCADE 
);

CREATE TABLE matches(
    id SERIAL PRIMARY KEY,
    team_a INT REFERENCES teams(id) ON DELETE CASCADE,
    team_b INT REFERENCES teams(id) ON DELETE CASCADE,
    team_a_score INT,
    team_b_score INT,
    match_date VARCHAR(255)
);