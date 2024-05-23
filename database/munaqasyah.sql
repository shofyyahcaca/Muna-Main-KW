
drop database if exists munaqasyah;
create database munqasyah;

use munqasyah;

create table if not exists `topics` (
  `topic_id` int auto_increment,
  `name` varchar(100) not null,
  primary key(`user_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `topic_relation` (
  `toprel_id` int auto_increment,
  `relation` text not null,
  `topic_id` int not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`toprel_id`),
  constraint `fk_toprel_id`
  foreign key (`topic_id`)
  references `topics`(topic_id)
) engine=InnoDB default charset=utf8;

create table if not exists `teach_schedule` (
  `teasch_id` int auto_increment,
  `name` text not null,
  `user_id` int not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`teasch_id`),
  constraint `fk_user_id`
  foreign key (`user_id`)
  references `users`(user_id)
) engine=InnoDB default charset=utf8;

create table if not exists `lecture_counter` (
  `lectcount_id` int auto_increment,
  `user_id` int not null,
  `name` text not null,
  `first_week` int unsigned not null,
  `two_week` int unsigned not null,
  `three_week` int unsigned not null,
  `four_week` int unsigned not null,
  primary key(`lectcount_id`),
  constraint `fk_user_id`
  foreign key (`user_id`)
  references `users`(user_id)
) engine=InnoDB default charset=utf8; 