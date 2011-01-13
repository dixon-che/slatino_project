CREATE TABLE `Institute_occupation` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `institute_id` integer NOT NULL,
    `name` varchar(255) NOT NULL,
    `work_time` varchar(255) NOT NULL,
    `work_days` varchar(255) NOT NULL,
    `phone` varchar(13) NOT NULL
)
;

ALTER TABLE `Institute_occupation` ADD CONSTRAINT `institute_id_refs_id_f50b6990` FOREIGN KEY (`institute_id`) REFERENCES `Institute_institute` (`id`);
CREATE TABLE `Institute_occupationperiod` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `occupation_id` integer NOT NULL,
    `personalee_id` integer NOT NULL,
    `date_start` date NOT NULL,
    `date_end` date
)
;
ALTER TABLE `Institute_occupationperiod` ADD CONSTRAINT `occupation_id_refs_id_6b134448` FOREIGN KEY (`occupation_id`) REFERENCES `Institute_occupation` (`id`);
ALTER TABLE `Institute_occupationperiod` ADD CONSTRAINT `personalee_id_refs_id_8fa4a9f` FOREIGN KEY (`personalee_id`) REFERENCES `Personalee_personalee` (`id`);


ALTER TABLE `Institute_institute` DROP COLUMN `pub_date`;
ALTER TABLE `Institute_institute` DROP COLUMN `publisher`;

ALTER TABLE `Institute_institute` ADD COLUMN `published` bool NOT NULL DEFAULT 1;

DROP TABLE `Institute_Room`;
