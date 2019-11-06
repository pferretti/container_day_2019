CREATE DATABASE test_database;

\connect test_database;

CREATE SEQUENCE character_names_id_seq;
CREATE TABLE character_names (
    id integer PRIMARY KEY DEFAULT nextval('character_names_id_seq'),
    field1 varchar(255) NOT NULL,
    field2 varchar(255) NOT NULL
);

INSERT INTO character_names (field1, field2) VALUES ('George', 'McFly');
INSERT INTO character_names (field1, field2) VALUES ('Biff', 'Tannen');
