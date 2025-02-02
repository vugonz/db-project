DROP TABLE IF EXISTS category CASCADE;
DROP TABLE IF EXISTS simple_category CASCADE;
DROP TABLE IF EXISTS super_category CASCADE;
DROP TABLE IF EXISTS has_other CASCADE;
DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS has_category CASCADE;
DROP TABLE IF EXISTS ivm CASCADE;
DROP TABLE IF EXISTS point_of_retail CASCADE;
DROP TABLE IF EXISTS installed_at CASCADE;
DROP TABLE IF EXISTS shelf CASCADE;
DROP TABLE IF EXISTS planogram CASCADE;
DROP TABLE IF EXISTS retailer CASCADE;
DROP TABLE IF EXISTS responsible_for CASCADE;
DROP TABLE IF EXISTS replenishment_event CASCADE;

CREATE TABLE IF NOT EXISTS category
   (category_name	varchar(80)	 NOT NULL UNIQUE,
   	PRIMARY KEY(category_name));


CREATE TABLE IF NOT EXISTS simple_category
   (category_name	varchar(80)	 NOT NULL UNIQUE,
   	PRIMARY KEY(category_name),
   	CONSTRAINT fk_simple_category	FOREIGN KEY(category_name)	REFERENCES category(category_name) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS super_category
   (category_name	varchar(80)	 NOT NULL UNIQUE,
   	PRIMARY KEY(category_name),
   	CONSTRAINT fk_super_category	FOREIGN KEY(category_name)	REFERENCES category(category_name) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS has_other
	(super_category	 varchar(80)	NOT NULL,
	 category        varchar(80)    NOT NULL,
	 PRIMARY KEY(category),
	 CONSTRAINT fk_other_super			FOREIGN KEY(super_category)	  REFERENCES super_category(category_name) ON DELETE CASCADE,
	 CONSTRAINT fk_other_category		FOREIGN KEY(category)		  	  REFERENCES category(category_name) ON DELETE CASCADE,
	 CHECK(super_category <> category));


CREATE TABLE IF NOT EXISTS product
	(ean 			NUMERIC(13,0)	 NOT NULL UNIQUE,
	 category       varchar(80)    	 NOT NULL,
	 description    varchar(80)      NOT NULL,
	 PRIMARY KEY(ean),
	 CONSTRAINT fk_product_category	 FOREIGN KEY(category)	REFERENCES category(category_name) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS has_category
	(ean 			 NUMERIC(13,0)	 		NOT NULL,
	 category_name	 varchar(80)		NOT NULL,
	 CONSTRAINT fk_has_product			FOREIGN KEY(ean)	  			  REFERENCES product(ean),
	 CONSTRAINT fk_has_category		FOREIGN KEY(category_name)	  REFERENCES category(category_name) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS ivm
	(serial_number	varchar(80)	 NOT NULL,
	 manufacturer	varchar(80)	 NOT NULL,
	 PRIMARY KEY(serial_number, manufacturer));


CREATE TABLE IF NOT EXISTS point_of_retail
	(location_name		varchar(80)	 NOT NULL UNIQUE,
	 location_district	varchar(80)	 NOT NULL,
	 location_county	varchar(80)	 NOT NULL,
	 PRIMARY KEY(location_name));


CREATE TABLE IF NOT EXISTS installed_at
	(serial_number						varchar(80)	 NOT NULL,
	 manufacturer						varchar(80)	 NOT NULL,
	 local								varchar(80)  NOT NULL,
	 PRIMARY KEY(serial_number, manufacturer),
	 CONSTRAINT fk_installed_serial		FOREIGN KEY(serial_number, manufacturer)	REFERENCES ivm(serial_number, manufacturer) ON DELETE CASCADE,
	 CONSTRAINT fk_installed_local		FOREIGN KEY(local)								REFERENCES point_of_retail(location_name) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS shelf
	(shelf_number	INT 		 	 NOT NULL,
	 serial_number	varchar(80)	 NOT NULL,
	 manufacturer	varchar(80)	 NOT NULL,
	 height			INT     	 	 NOT NULL,
	 category_name	varchar(80)	 NOT NULL,
	 UNIQUE(shelf_number, serial_number, manufacturer),
	 PRIMARY KEY(shelf_number, serial_number, manufacturer),
	 CONSTRAINT fk_shelf_category			FOREIGN KEY(category_name)	REFERENCES category(category_name) ON DELETE CASCADE,
	 CONSTRAINT fk_shelf_ivm_serial		FOREIGN KEY(serial_number, manufacturer)	REFERENCES ivm(serial_number, manufacturer) ON DELETE CASCADE);	


CREATE TABLE IF NOT EXISTS planogram
	(ean 			NUMERIC(13,0)	 	 NOT NULL,
	 shelf_number	INT 	 		 	 NOT NULL,
	 serial_number	varchar(80)	 	 NOT NULL,
	 manufacturer	varchar(80)	 	 NOT NULL,
	 faces			INT             NOT NULL,
	 units          INT            NOT NULL,
	 loc            varchar(80)    NOT NULL,
	 PRIMARY KEY(shelf_number, ean, serial_number, manufacturer),
	 CONSTRAINT fk_planogram_product_ean		FOREIGN KEY(ean)			    REFERENCES product(ean) ON DELETE CASCADE,
	 CONSTRAINT fk_planogram_shelf_number		FOREIGN KEY(shelf_number, serial_number, manufacturer)	 REFERENCES shelf(shelf_number, serial_number, manufacturer) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS retailer
	(tin 					INT			   NOT NULL UNIQUE,
	 retailer_name		varchar(80)		NOT NULL UNIQUE,
	 PRIMARY KEY(tin));


CREATE TABLE IF NOT EXISTS responsible_for
	(category_name	varchar(80)	 NOT NULL,
	 tin 			   INT	 	    NOT NULL,
	 serial_number	varchar(80)	 NOT NULL,
	 manufacturer	varchar(80)	 NOT NULL,
	 PRIMARY KEY(serial_number, manufacturer),
	 CONSTRAINT fk_responsible_category			FOREIGN KEY(category_name)	 REFERENCES category(category_name) ON DELETE CASCADE,
	 CONSTRAINT fk_responsible_retailer			FOREIGN KEY(tin)	 		    REFERENCES retailer(tin) ON DELETE CASCADE,
	 CONSTRAINT fk_responsible_ivm_serial		FOREIGN KEY(serial_number, manufacturer)	 REFERENCES ivm(serial_number, manufacturer) ON DELETE CASCADE);



CREATE TABLE replenishment_event
	(ean 					   NUMERIC(13,0)	 NOT NULL,
	 shelf_number			INT 	 		    NOT NULL,
	 serial_number			varchar(80)	 	 NOT NULL,
	 manufacturer			varchar(80)	 	 NOT NULL,
	 instant        		TIMESTAMP		 NOT NULL,
	 replenished_units	INT             NOT NULL,
	 tin 				      INT		       NOT NULL,
	 PRIMARY KEY(ean, shelf_number, serial_number, manufacturer, instant),
	 CONSTRAINT fk_replenishment_planogram		    FOREIGN KEY(ean, shelf_number, serial_number, manufacturer)	     REFERENCES planogram(ean, shelf_number, serial_number, manufacturer) ON DELETE CASCADE,
	 CONSTRAINT fk_replenishment_retailer			 FOREIGN KEY(tin)	  		           											  REFERENCES retailer(tin) ON DELETE CASCADE);
	
