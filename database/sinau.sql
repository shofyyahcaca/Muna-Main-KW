
drop database if exists sinau;
create database sinau;

use sinau;

create table if not exists `lecture` (
  `lecture_id` int auto_increment,
  `lecture_uuid` text not null,
  `name` varchar(100) not null,
  `nip` varchar(20) not null,
  primary key(`lecture_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `work_unit` (
  `worun_id` int auto_increment,
  `unit` varchar(100) not null,
  primary key(`worun_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `lecture_unit` (
  `lecun_id` int auto_increment,
  `worun_id` int not null,
  `lecture_id` int not null,
  primary key(`lecun_id`),
  constraint `fk_worun_id`
  foreign key (`worun_id`)
  references `work_unit`(worun_id),
  constraint `fk_lecture_id`
  foreign key (`lecture_id`)
  references `lecture`(lecture_id)
) engine=InnoDB default charset=utf8;

create table if not exists `science_consortium` (
  `scico_id` int auto_increment,
  `scico` varchar(100) not null,
  primary key(`scico_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `science_lecture` (
  `scile_id` int auto_increment,
  `scico_id` int not null,
  `lecture_id` int not null,
  primary key(`scile_id`),
  constraint `fk_scico_id2`
  foreign key (`scico_id`)
  references `science_consortium`(scico_id),
  constraint `fk_lecture_id2`
  foreign key (`lecture_id`)
  references `lecture`(lecture_id)
) engine=InnoDB default charset=utf8;

create table if not exists `study_programs` (
  `stupro_id` int auto_increment,
  `name` varchar(100) not null,
  `alias` char(100) not null,
  primary key(`stupro_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `student` (
  `student_id` int auto_increment,
  `student_uuid` text not null,
  `stupro_id` int not null,
  `nim` varchar(15) not null,
  `jenjang` varchar(5) not null,
  `name` varchar(100) not null,
  `semester` int unsigned not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`student_id`),
  constraint `fk_stupro_id`
  foreign key (`stupro_id`)
  references `study_programs`(stupro_id)
) engine=InnoDB default charset=utf8;

create table if not exists `thesis` (
  `thesis_id` int auto_increment,
  `thesis_uuid` text not null,
  `student_id` int not null,
  `title` text not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`thesis_id`),
  constraint `fk_student_id`
  foreign key (`student_id`)
  references `student`(student_id)
) engine=InnoDB default charset=utf8;
