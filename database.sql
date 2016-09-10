PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE distributors (disid INTEGER PRIMARY KEY, name TEXT, payee TEXT,
                           address TEXT, city TEXT, state TEXT, zip TEXT,
                           attn TEXT);
INSERT INTO "distributors" VALUES(1,'Kino Lorber','Kino Lorber','333 West 39th Street','New York','New York','10018','');
INSERT INTO "distributors" VALUES(2,'Park Circus','Park Circus, Inc.','11846 Ventura Blvd, Suite 140','Studio City','California','91604','Cyndi Ex');
INSERT INTO "distributors" VALUES(3,'Universal Pictures','Universal Film Exchanges, Inc.','PO Box 848270','Dallas','Texas','75284','');
INSERT INTO "distributors" VALUES(4,'Rialto Pictures','Rialto Pictures','45 E. 72nd St, #16A','New York','New York','10021','');
INSERT INTO "distributors" VALUES(5,'Warner Bros.','Warner Bros.','PO Box 936193','Atlanta','Georgia','31193-6193','');
INSERT INTO "distributors" VALUES(6,'GKIDS','GKIDS, Inc.','225 Broadway, Suite 2610','New York','New York','10007','');
INSERT INTO "distributors" VALUES(7,'Imagina','imagina','','','Spain','','');
CREATE TABLE films (filmid INTEGER, title TEXT, distributor TEXT,
                    start_date TEXT, end_date TEXT, percentage INT,
                    guarantee INT, gross INT, overage IT, total_paid INT,
                    net INT, mg_num INT, mg_date INT, o_num INT, o_date INT, posted INT,
                    settled INT);
INSERT INTO "films" VALUES(NULL,'Nosferatu','Kino Lorber','10/29','10/19',0.35,250,0,0,0,0,NULL,NULL,NULL,NULL,0,0);
INSERT INTO "films" VALUES(NULL,'Isla Bonita','imagina','7/24','7/30',0.35,0,0,0,0,0,NULL,NULL,NULL,NULL,0,0);
INSERT INTO "films" VALUES(NULL,'Elevator to the Gallows','Rialto Pictures','8/12','8/18',0.4,350,0,0,0,0,NULL,NULL,NULL,NULL,0,0);
INSERT INTO "films" VALUES(NULL,'City of God','Park Circus','8/13','8/13',0.35,350,0,0,0,0,NULL,NULL,NULL,NULL,0,0);
INSERT INTO "films" VALUES(NULL,'Midnight Cowboy','Park Circus','8/5','8/5',0.35,350,0,0,0,0,NULL,NULL,NULL,NULL,0,0);
INSERT INTO "films" VALUES(NULL,'Kid Flix Mix','GKIDS','8/13','8/14',0.35,250,0,0,0,0,NULL,NULL,NULL,NULL,0,0);
COMMIT;
