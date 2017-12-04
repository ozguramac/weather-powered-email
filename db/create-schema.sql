CREATE TABLE app_location (
    id          SERIAL PRIMARY KEY,
    city        varchar(255) NOT NULL,
    state       varchar(255) NOT NULL,
    latitude    numeric(7,4) NOT NULL,
    longtitude  numeric(7,4) NOT NULL
);
CREATE TABLE app_user (
    id          SERIAL PRIMARY KEY,
    email       varchar(255) UNIQUE NOT NULL,
    location    SERIAL REFERENCES app_location(id)
);