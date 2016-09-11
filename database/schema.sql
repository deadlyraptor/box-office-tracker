CREATE TABLE distributors (disid INTEGER PRIMARY KEY, name TEXT, payee TEXT,
                           address TEXT, city TEXT, state TEXT, zip TEXT,
                           attn TEXT);
CREATE TABLE films (filmid INTEGER, title TEXT, distributor TEXT,
                    start_date TEXT, end_date TEXT, percentage INT,
                    guarantee INT, gross INT, overage IT, total_paid INT,
                    net INT, mg_num INT, mg_date INT, o_num INT, o_date INT, posted INT,
                    settled INT);
