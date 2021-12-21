-- Drop tables if they exist
DROP TABLE IF EXISTS Movies, Ratings, Names, MovieRoles, Genres;
DROP VIEW IF EXISTS Actors, Directors, Writers;

-- Create table command for the table Movies
CREATE TABLE Movies(imdb_title_id varchar(12), title varchar(100), original_title varchar(100), year_of_release decimal(4,0), date_published datetime, duration int, country varchar(50), language varchar(50), director varchar(200), writer varchar(200), production_company varchar(100), actors varchar(500), description varchar(8000), budget varchar(25), usa_gross_income varchar(25), worlwide_gross_income varchar(25), reviews_from_users int, reviews_from_critics int, PRIMARY KEY (imdb_title_id));

-- Create table command for the table Ratings
CREATE TABLE Ratings(imdb_title_id varchar(12), weighted_average_vote decimal(4,2), total_votes int, mean_vote decimal(4,2), median_vote decimal(4,2), votes_10 int, votes_1 int, males_allages_avg_vote decimal(4,2), males_allages_votes int, females_allages_avg_vote decimal(4,2), females_allages_votes int, top1000_voters_rating decimal(4,2), top1000_voters_votes int, us_voters_rating decimal(4,2), us_voters_votes int, non_us_voters_rating decimal(4,2), non_us_voters_votes int, PRIMARY KEY (imdb_title_id), FOREIGN KEY (imdb_title_id) REFERENCES Movies (imdb_title_id));

-- Create table command for the table Names
CREATE TABLE Names(imdb_name_id varchar(12), name varchar(100), birth_name varchar(100), height int, bio varchar(8000), birth_details varchar(500), date_of_birth datetime, birth_country varchar(50), death_details varchar(500), date_of_death datetime, death_country varchar(50), reason_of_death varchar(300), spouses int, divorces int, spouses_with_children int, children int, PRIMARY KEY (imdb_name_id));

-- Create table command for the table MovieRoles
CREATE TABLE MovieRoles(imdb_title_id varchar(12), imdb_name_id varchar(12), played_role varchar(50), characters varchar(100), PRIMARY KEY (imdb_title_id, imdb_name_id), FOREIGN KEY (imdb_title_id) REFERENCES Movies (imdb_title_id), FOREIGN KEY (imdb_name_id) REFERENCES Names (imdb_name_id));

-- Create view command for the view Actors
GO
CREATE VIEW Actors AS SELECT MovieRoles.imdb_title_id, MovieRoles.imdb_name_id, Names.name FROM MovieRoles INNER JOIN Names ON MovieRoles.imdb_name_id = Names.imdb_name_id WHERE played_role = 'actor' OR played_role = 'actress';

-- Create view command for the view Directors
GO
CREATE VIEW Directors AS SELECT MovieRoles.imdb_title_id, MovieRoles.imdb_name_id, Names.name FROM MovieRoles INNER JOIN Names ON MovieRoles.imdb_name_id = Names.imdb_name_id WHERE played_role = 'director';

-- Create view command for the view Writers
GO
CREATE VIEW Writers AS SELECT MovieRoles.imdb_title_id, MovieRoles.imdb_name_id, Names.name FROM MovieRoles INNER JOIN Names ON MovieRoles.imdb_name_id = Names.imdb_name_id WHERE played_role = 'writer';

-- Create table command for the table Genres
GO
CREATE TABLE Genres(imdb_title_id varchar(12), genre varchar(20), PRIMARY KEY (imdb_title_id, genre), FOREIGN KEY (imdb_title_id) REFERENCES Movies (imdb_title_id));