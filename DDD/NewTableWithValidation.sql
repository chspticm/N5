-- using trial.db

CREATE TABLE pupil (
    pupilID INTEGER NOT NULL PRIMARY KEY,
    forename TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER,
    email TEXT
);
