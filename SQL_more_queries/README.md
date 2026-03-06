# Git Intro Project

──┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-privileges.sql
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ -- List privileges of user_0d_1 and user_0d_2
   2   │ SHOW GRANTS FOR 'user_0d_1'@'localhost';
   3   │ SHOW GRANTS FOR 'user_0d_2'@'localhost';
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 10-genre_id_by_show.sql
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ -- Listing all shows contained in `hbtn_0d_tvshows` having at least one genre linked.
   2   │ SELECT tv_shows.title, tv_show_genres.genre_id
   3   │ FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
   4   │ ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 11-genre_id_all_shows.sql
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ -- Lists all shows contained in hbtn_0d_tvshows that have an optional genre.
   2   │ SELECT tv_shows.title, tv_show_genres.genre_id
   3   │ FROM tv_shows
   4   │ LEFT JOIN tv_show_genres
   5   │ ON tv_shows.id = tv_show_genres.show_id
   6   │ ORDER BY tv_shows.title, tv_show_genres.genre_id;
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 12-no_genre.sql
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ -- Listing all shows contained in hbtn_0d_tvshows without a genre linked.
   2   │ SELECT tv_shows.title, tv_show_genres.genre_id
   3   │ FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
   4   │ WHERE tv_show_genres.genre_id IS NULL
   5   │ ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 13-count_shows_by_genre.sql
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ -- Listing all genre from tv_shows and displaying the number of shows linked to each
   2   │ SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
   3   │ FROM tv_genres
   4   │ JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
   5   │ GROUP BY tv_genres.name
   6   │ ORDER BY number_of_shows DESC;
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 14-my_genres.sql
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ -- Lists all genres of the Dexter show.
   2   │ SELECT tv_genres.name
   3   │   FROM tv_shows
