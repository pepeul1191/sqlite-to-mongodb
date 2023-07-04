-- migrate:up

CREATE TABLE districts (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(45),
  province_id	INTEGER NOT NULL,
  FOREIGN KEY (province_id) REFERENCES provinces (id)
);

-- migrate:down

DROP TABLE IF EXISTS districts;
