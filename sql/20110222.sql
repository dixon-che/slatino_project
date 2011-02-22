alter table Personalee_personalee rename to Persons_person;
alter table Personalee_personalee_tags rename to Persons_person_tags;
alter table Persons_person_tags change column personalee_id person_id integer NOT NULL;
