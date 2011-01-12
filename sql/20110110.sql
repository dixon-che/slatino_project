CREATE TABLE "Institute_occupation" (
    "id" integer NOT NULL PRIMARY KEY,
    "institute_id" integer NOT NULL REFERENCES "Institute_institute" ("id"),
    "name" varchar(255) NOT NULL,
    "work_time" varchar(255) NOT NULL,
    "work_days" varchar(255) NOT NULL,
    "phone" varchar(13) NOT NULL
)
;
CREATE TABLE "Institute_occupationperiod" (
    "id" integer NOT NULL PRIMARY KEY,
    "occupation_id" integer NOT NULL REFERENCES "Institute_occupation" ("id"),
    "personalee_id" integer NOT NULL REFERENCES "Personalee_personalee" ("id"),
    "date_start" date NOT NULL,
    "date_end" date
)
;
CREATE INDEX "Institute_occupation_25a0dd70" ON "Institute_occupation" ("institute_id");
CREATE INDEX "Institute_occupationperiod_6ea0cf59" ON "Institute_occupationperiod" ("occupation_id");
CREATE INDEX "Institute_occupationperiod_2981be58" ON "Institute_occupationperiod" ("personalee_id");

ALTER TABLE "Institute_institute" DROP COLUMN 'pub_date';
ALTER TABLE "Institute_institute" DROP COLUMN 'publisher';

ALTER TABLE "Institute_institute" ADD COLUMN 'published' bool NOT NULL DEFAULT 1;

DROP TABLE "Institute_Room";
