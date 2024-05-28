
drop database if exists munaqasyah;
create database munaqasyah;

use munaqasyah;

create table if not exists `topics` (
  `topic_id` int auto_increment,
  `name` varchar(100) not null,
  primary key(`topic_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `topic_relation` (
  `toprel_id` int auto_increment,
  `thesis_uuid` text not null,
  `topic_id` int not null,
  primary key(`toprel_id`),
  constraint `fk_topic_id`
  foreign key (`topic_id`)
  references `topics`(topic_id)
) engine=InnoDB default charset=utf8;

create table if not exists `munaqasyah` (
  `muna_id` int auto_increment,
  `lecture_uuid` text not null,
  `student_uuid` text not null,
  `munaqasyah` int not null,
  primary key(`muna_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `courses` (
  `courses_id` int auto_increment,
  `lecture_uuid` text not null,
  `day` varchar(20) not null,
  `start_time` time not null,
  `end_time` time not null,
  primary key(`courses_id`)
) engine=InnoDB default charset=utf8;

