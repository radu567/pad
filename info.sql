create table student(
	id int primary key not null,
  name varchar(50),
	mark float);

insert into student values(1, 'Daniel M', 9.5);
insert into student values(2, 'Marin C', 8.0);

/* Example of insert into database from server
curs.execute("insert into student values(1, 'Daniel M', 9.5);")
conn.commit()
*/
