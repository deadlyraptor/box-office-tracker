This Python program tracks box office grosses and payments made to film
distributors.

Database Schema

CREATE TABLE distributors (disid INTEGER PRIMARY KEY, name TEXT, payee TEXT,
                           address TEXT, city TEXT, state TEXT, zip TEXT,
                           attn TEXT);

table: distributors
1. disid INTEGER PRIMARY KEY
2. name TEXT
3. payee TEXT
4. address TEXT
5. city TEXT
6. state TEXT
7. zip TEXT
8. attn TEXT

CREATE TABLE films (filmid INTEGER, name TEXT, distributor INTEGER,
                    start_date TEXT, end_date TEXT, percentage INT,
                    guarantee INT, gross INT, overage IT, total_paid INT,
                    net INT, mg_num INT, mg_date INT, o_num INT, o_date INT, posted INT,
                    settled INT,
                    FOREIGN KEY (distributor) REFERENCES distributors(disid));

table: films
1. filmid INTEGER
2. name TEXT
3. distributor INTEGER
4. start_date TEXT
5. end_date TEXT
6. percentage INT
7. guarantee INT
8. gross INT
9. overage INT
10. total_paid INT
11. net INT
12. mg_num INT
13. mg_date INT
14. o_num INT
15. o_date INT
16. posted INT
17. settled INT
18. FOREIGN KEY (distributor) REFERENCES distributors(disid)
