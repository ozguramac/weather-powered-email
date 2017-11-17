CREATE TABLE app_location (
    id          SERIAL PRIMARY KEY,
    city        varchar(255) NOT NULL,
    state       varchar(255) NOT NULL
);
CREATE TABLE app_user (
    id          SERIAL PRIMARY KEY,
    email       varchar(255) UNIQUE NOT NULL,
    location    SERIAL REFERENCES app_location(id)
);