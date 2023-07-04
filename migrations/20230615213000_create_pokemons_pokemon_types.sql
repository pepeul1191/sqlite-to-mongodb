-- migrate:up

CREATE TABLE pokemons_pokemon_types (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  pokemon_id	INTEGER NOT NULL,
  pokemon_type_id	INTEGER NOT NULL,
  FOREIGN KEY (pokemon_id) REFERENCES pokemons (id),
  FOREIGN KEY (pokemon_type_id) REFERENCES users (id)
);

-- migrate:down

DROP TABLE IF EXISTS pokemons_pokemon_types;
