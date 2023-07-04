-- migrate:up

CREATE TABLE provinces (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(45),
  department_id	INTEGER NOT NULL,
  FOREIGN KEY (department_id) REFERENCES departaments (id)
);

-- migrate:down

DROP TABLE IF EXISTS provinces;
