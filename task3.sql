create table if not exists gengre (
    id SERIAL primary key,
    name VARCHAR(60) not null unique 
);

create table if not exists gengre_sing (
	id SERIAL primary key,
	gengre_id INTEGER references gengre(id),
	singer_id INTEGER references singer(id)
);

create table if not exists singer (
    id SERIAL primary key,
    name VARCHAR(50) not null
);

create table if not exists album_isp (
	id SERIAL primary key,
	album_id INTEGER references album(id),
	singer_id INTEGER references singer(id)
);

create table if not exists album (
    id SERIAL primary key,
    name VARCHAR(50) not null,
    album_date INTEGER not null
);



create table if not exists track (
	id SERIAL primary key,
	name VARCHAR(100) not null,
	lenth time not null,
	album_id INTEGER references album(id)
); 

create table if not exists sbor_tr (
	id SERIAL primary key,
	track_id INTEGER references track(id),
	sbor_id INTEGER references sbor(id)
);


create table if not exists sbor (
	id SERIAL primary key,
	name VARCHAR(50) not null,
	sbor_date INTEGER not null
);



