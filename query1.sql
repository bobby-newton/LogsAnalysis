SELECT title,
       count(path) AS views
FROM log,
     articles
WHERE path LIKE concat('/article/', slug)
GROUP BY title
ORDER BY views DESC
LIMIT 3;
