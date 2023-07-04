-- migrate:up

CREATE TABLE pokemon_types (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(25)
);

-- migrate:down

DROP TABLE IF EXISTS pokemon_types;
