-- 1 Top n movies - input (movieNo) - output -> (title, ratings) 
SELECT Movies.title AS Title, Ratings.weighted_average_vote AS Rating, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Ratings ON Movies.imdb_title_id = Ratings.imdb_title_id ORDER BY Ratings.weighted_average_vote DESC LIMIT 250;

-- 2 actors in movies - input(movieName) - output (all actors)
SELECT Actors.name AS "Actor Name" FROM Movies INNER JOIN Actors ON Movies.imdb_title_id = Actors.imdb_title_id WHERE Movies.title = 'Miss Jerry';

-- 3 Top 10 movie by genre - input(genre) - output(movie details)
SELECT DISTINCT T1.Name AS 'Name', Ratings.weighted_average_vote AS 'Rating', T1.Language AS Language, T1.Duration AS Duration FROM Ratings INNER JOIN (SELECT Movies.title AS 'Name', Genres.genre AS 'genre', Movies.imdb_title_id AS 'imdb_title_id', Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Genres ON Movies.imdb_title_id = Genres.imdb_title_id) AS T1 ON T1.imdb_title_id = Ratings.imdb_title_id WHERE T1.genre like '%Drama%' ORDER BY Ratings.weighted_average_vote DESC LIMIT 10;

-- 4 Actors born today - input(date) - output(actors born today)
select DISTINCT Names.name AS Name from Names INNER JOIN MovieRoles ON Names.imdb_name_id = MovieRoles.imdb_name_id where (MovieRoles.played_role="actor" AND Names.date_of_birth like '%-09-10%');

-- 5 Most Voted n movies in US - - input(n) - output(all movie details)
SELECT Movies.title AS Title, Ratings.us_voters_votes AS Votes, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Ratings ON Movies.imdb_title_id = Ratings.imdb_title_id ORDER BY Ratings.us_voters_votes DESC LIMIT 10;

-- 6 Most voted n movies overall - input(n) - output(all movie details)
SELECT Movies.title AS Title, Ratings.total_votes AS Votes, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Ratings ON Movies.imdb_title_id = Ratings.imdb_title_id ORDER BY Ratings.total_votes DESC LIMIT 10;

-- 7 Top movies released in x country - input(countryName) - output (all movie details)
SELECT Movies.title AS Title, Ratings.weighted_average_vote AS Rating, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Ratings ON Movies.imdb_title_id = Ratings.imdb_title_id WHERE Movies.country LIKE '%USA%' ORDER BY Ratings.weighted_average_vote DESC LIMIT 250;

-- 8 Lowest rated movies - input() - output(movie details exclude null) 
SELECT Movies.title AS Title, Ratings.weighted_average_vote AS Rating, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Ratings ON Movies.imdb_title_id = Ratings.imdb_title_id ORDER BY Ratings.weighted_average_vote LIMIT 250;

-- 9 Actors who acted in movies(atleast one) between x and y year - input(x year, y year) - output(all movie details)
SELECT DISTINCT Actors.name AS Name from Movies INNER JOIN Actors ON Movies.imdb_title_id = Actors.imdb_title_id where Movies.year_of_release BETWEEN 2000 AND 2020;

-- 10 movies by actor - input(actorName) - output(all movies)
SELECT Movies.title AS Title, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Actors ON Movies.imdb_title_id = Actors.imdb_title_id WHERE Actors.name = 'Fred Astaire';

-- 11 All movies directed by a given director - input(director name) - output (movie details)
SELECT Movies.title AS Title, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Directors ON Movies.imdb_title_id = Directors.imdb_title_id WHERE Directors.name = 'Louis Feuillade';

-- 12 Top n movies of year - input (year) - output (movie details)
SELECT Movies.title AS Title, Ratings.weighted_average_vote AS Rating, Movies.language AS Language, Movies.duration AS Duration FROM Movies INNER JOIN Ratings ON Movies.imdb_title_id = Ratings.imdb_title_id WHERE Movies.year_of_release = "1990" ORDER BY Ratings.weighted_average_vote DESC LIMIT 250;

-- 13 Actor that is in both movies x and y - input (movie name 1, movie name 2) - output (Actor details)
SELECT Actors.name AS 'Name' FROM Movies INNER JOIN Actors ON Movies.imdb_title_id = Actors.imdb_title_id WHERE Movies.title = 'Follie di jazz' AND Name IN (SELECT Actors.name AS 'Name' FROM Movies INNER JOIN Actors ON Movies.imdb_title_id = Actors.imdb_title_id WHERE Movies.title = 'Cenerentola a Parigi');

