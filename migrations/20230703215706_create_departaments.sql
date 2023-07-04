-- migrate:up

CREATE TABLE departments (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(45)
);

-- migrate:down

DROP TABLE IF EXISTS departments;
