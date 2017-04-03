drop table if exists accounts;
create table accounts (
  id integer primary key autoincrement,
  name text not null,
  type text not null,
  balance REAL  
);
insert into accounts (name, type, balance) values ('BOA', 'CHECKING', 392.34);
insert into accounts (name, type, balance) values ('BOA', 'SAVING', 23.34);
insert into accounts (name, type, balance) values ('CHASE', 'CHECKING', 23.34);
insert into accounts (name, type, balance) values ('SAPPHIRE', 'CREDIT', 23.34);
insert into accounts (name, type, balance) values ('FREEDOM', 'CREDIT', 23.34);
insert into accounts (name, type, balance) values ('DCU', 'SAVING', 23.34);
insert into accounts (name, type, balance) values ('DCU', 'CHECKING', 392.34);
insert into accounts (name, type, balance) values ('DCU', 'CREDIT', 23.34);
insert into accounts (name, type, balance) values ('AMEX', 'CREDIT', 23.34);
insert into accounts (name, type, balance) values ('CAPITAL', 'CREDIT', 23.34);
insert into accounts (name, type, balance) values ('PERSONAL SAVING', 'PERSONAL SAVING', 23.34);