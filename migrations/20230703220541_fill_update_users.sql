-- migrate:up

UPDATE users SET district_id =1528 WHERE id = 1;
UPDATE users SET district_id =875 WHERE id = 2;
UPDATE users SET district_id =754 WHERE id = 3;
UPDATE users SET district_id =990 WHERE id = 4;
UPDATE users SET district_id =22 WHERE id = 5;
UPDATE users SET district_id =586 WHERE id = 6;
UPDATE users SET district_id =1676 WHERE id = 7;
UPDATE users SET district_id =1685 WHERE id = 8;
UPDATE users SET district_id =920 WHERE id = 9;
UPDATE users SET district_id =737 WHERE id = 10;


-- migrate:down

UPDATE users SET district_id =NULL WHERE id = 10;