

-- 1341. Movie Rating
-- Solved
-- Medium - 1369
-- Topics
-- premium lock icon
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Movies

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | movie_id      | int     |
-- | title         | varchar |
-- +---------------+---------+
-- movie_id is the primary key (column with unique values) for this table.
-- title is the name of the movie.
-- Each movie has a unique title.
-- Table: Users

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | user_id       | int     |
-- | name          | varchar |
-- +---------------+---------+
-- user_id is the primary key (column with unique values) for this table.
-- The column 'name' has unique values.
-- Table: MovieRating

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | movie_id      | int     |
-- | user_id       | int     |
-- | rating        | int     |
-- | created_at    | date    |
-- +---------------+---------+
-- (movie_id, user_id) is the primary key (column with unique values) for this table.
-- This table contains the rating of a movie by a user in their review.
-- created_at is the user's review date. 
 

-- Write a solution to:

-- Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
-- Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
-- The result format is in the following example.
-- # Write your MySQL query statement below
    (select a.name as results from
    Users as a
    inner join 
    (select user_id ,count(*) as conteo
    from MovieRating 
    group by 
    user_id
    having count(*)= (select max(conteo) 
    from (select user_id,count(*) as conteo from  MovieRating 
    group by 
    user_id) as r 
    )) as b
    on
    a.user_id=b.user_id
    order by 1 limit 1)
    union all
        ( select a.title  from
    Movies  as a
    inner join 
    (select movie_id     ,avg(rating) as conteo
    from MovieRating 
    where created_at like '%2020-02%'
    group by 
    movie_id
    having round(avg(rating),3)= (select round(max(conteo),3) 
    from (select movie_id,avg(rating) as conteo from  MovieRating 
     where created_at like '%2020-02%'
    group by 
    movie_id) as r 
    )) as b
    on
    a.movie_id=b.movie_id
    order by 1 limit 1 )
;


-- select max(conteo) 
--     from (select movie_id,avg(rating) as conteo from  MovieRating 
--      where created_at like '%2020-02%'
--     group by 
--     movie_id)as d
-- | max(conteo) |
-- | ----------- |
-- | 4.6667      |

-- select movie_id     ,avg(rating) as conteo
--     from MovieRating 
--     where created_at like '%2020-02%'
--     group by 
--     movie_id
--     having avg(rating)= (select max(conteo) 
--     from (select movie_id,avg(rating) as conteo from  MovieRating 
--      where created_at like '%2020-02%'
--     group by 
--     movie_id) as r 
--     )

    -- | 8        | 4.6667 |