
drop database if exists auth;
create database auth;

use auth;

create table if not exists `types` (
  `type_id` int auto_increment,
  `name` varchar(255) not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`type_id`),
) engine=InnoDB default charset=utf8;

create table if not exists `connect` (
  `connect_id` int auto_increment,
  `name` varchar(255) not null,
  `type_id` varchar(255) not null, -- it is not real password but salt + hash + user level
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`connect_id`),
  constraint `fk_type_id`
  foreign key (`type_id`)
  references `types`(type_id)
) engine=InnoDB default charset=utf8;

create table if not exists `auth` (
  `auth_id` int auto_increment,
  `user_name` varchar(255) not null,
  `password` varchar(255) not null, -- it is not real password but salt + hash + user level
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`auth_id`),
) engine=InnoDB default charset=utf8;

create table if not exists `forgets` (
  `forget_id` int auto_increment,
  `freq_forget` varchar(255) not null,
  `auth_id` varchar(255) not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`forget_id`),
  constraint `fk_auth_id`
  foreign key (`auth_id`)
  references `auth`(auth_id)
) engine=InnoDB default charset=utf8;

create table if not exists `user_levels` (
  `usle_id` int auto_increment,
  `name` varchar(100) not null,
  primary key(`usle_id`)
) engine=InnoDB default charset=utf8;

create table if not exists `users` (
  `user_id` int auto_increment,
  `full_name` varchar(255) not null,
  `nick_name` varchar(50) not null,
  `created_at` int unsigned not null,
  `updated_at` int unsigned not null,
  primary key(`user_id`)
) engine=InnoDB default charset=utf8;