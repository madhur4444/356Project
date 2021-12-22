-- Top n movies - input (movieNo) - output -> (title, ratings) 
SELECT Movies.title AS Title, Ratings.weighted_average_vote AS Rating FROM Movies INNER JOIN Ratings ON Movies.imdb_title_id = Ratings.imdb_title_id ORDER BY Ratings.weighted_average_vote DESC LIMIT 250;

-- actors in movies - input(movieName) - output (all actors)
SELECT Movies.title AS Title, Actors.name AS "Actor Name" FROM Movies INNER JOIN Actors ON Movies.imdb_title_id = Actors.imdb_title_id WHERE Movies.title = '';

-- Longest Movies - input() - output(movie details)
