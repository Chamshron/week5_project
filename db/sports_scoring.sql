DROP TABLE teams;

CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    score INT
);

