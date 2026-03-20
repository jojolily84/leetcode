# Write your MySQL query statement below
SELECT
    firstName,
    lastName,
    city,
    state
FROM Person AS p
LEFT JOIN Address As a
    ON p.personID = a.personID