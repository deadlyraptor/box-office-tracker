# Box Office Tracker
This Python program tracks box office grosses and payments made to film
distributors.

### Database Schema

#### distributors

| disid | name | payee | address | city | state | zip | attn |
|:-----:|:----:|:-----:|:-------:|:----:|:-----:|:---:|:----:|
| INTEGER PRIMARY KEY | TEXT | TEXT | TEXT | TEXT | TEXT | TEXT | TEXT |

```sql
CREATE TABLE distributors (disid INTEGER PRIMARY KEY, name TEXT, payee TEXT,
                           address TEXT, city TEXT, state TEXT, zip TEXT,
                           attn TEXT);
```

#### films

| bookingid | title | distributor | start_date | end_date | percentage | guarantee | gross | overage | total_paid | net | mg_num | mg_date | o_num | o_date | posted | settled |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|INTEGER | TEXT | TEXT | TEXT | TEXT | INT | INT | INT | INT | INT | INT | INT | TEXT | INT | TEXT | INT | INT

```sql
CREATE TABLE films (bookingid INTEGER PRIMARY KEY, title TEXT, distributor TEXT,
                    start_date TEXT, end_date TEXT, percentage INT,
                    guarantee INT, gross INT, overage IT, total_paid INT,
                    net INT, mg_num INT, mg_date TEXT, o_num INT, o_date TEXT, posted INT,
                    settled INT);
```
