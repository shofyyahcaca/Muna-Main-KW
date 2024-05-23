
drop database if exists sinau;
create database sinau;

use sinau;

create table if not exists `study_programs` (
  `stupro_id` int auto_increment,
  `name` varchar(100) not null,
  `alias` char(5) not null,
  primary key(`stupro_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `courses` (
  `course_id` int auto_increment,
  `name` varchar(100) not null,
  `alias` char(6) not null,
  `stupro_id` int not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`course_id`)
  constraint `fk_stupro_id`
  foreign key (`stupro_id`)
  references `study_program`(stupro_id)
) engine=InnoDB default charset=utf8;

create table if not exists `group_classes` (
  `grocla_id` int auto_increment,
  `position` varchar(30) not null,
  `alias_pos` char(4) not null,
  `class` char(4) not null,
  primary key(`grocla_id`) 
) engine=InnoDB default charset=utf8;

create table if not exists `lecture` (
  `lecture_id` int auto_increment,
  `name` varchar(100) not null,
  `alias` char(5) not null,
  primary key(`stupro_id`)
) engine=InnoDB default charset=utf8;
