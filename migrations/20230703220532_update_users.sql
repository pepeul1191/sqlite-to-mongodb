-- migrate:up

ALTER TABLE users ADD COLUMN district_id INTEGER 
REFERENCES districts(id) ON UPDATE CASCADE ON DELETE CASCADE;

-- migrate:down

ALTER TABLE users
DROP COLUMN district_id;