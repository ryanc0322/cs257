-- Find all of earthquakes that had a magnitude between 1 and 3, and quakedepth between 10 and 30.
Query 1: SELECT * FROM earthquakes WHERE mag BETWEEN 1 AND 3 AND quakedepth BETWEEN 10 AND 30;

-- Find all earthquakes where magnitude was greater than 5.
Query 2: SELECT * FROM earthquakes WHERE mag > 5;

-- Find all earthquakes where longitude is between 100 and 200 and quakedepth is between 10 and 20.
Query 3: SELECT * FROM earthquakes WHERE longitude BETWEEN 100 AND 200 AND quakedepth BETWEEN 10 AND 20;

-- Find all earthquakes that happened between 12pm and 8pm with a magnitude greater than 3. 
SELECT * FROM earthquakes WHERE extract(hour from quaketime) BETWEEN 12 AND 20 AND mag>3;
