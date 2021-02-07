\c mydatabase
CREATE TABLE random (
   id SERIAL,
   uuid TEXT	NOT NULL
);
insert into random (uuid) select md5(random()::text) from generate_Series(1,20) s;
COMMIT;
