SELECT name,
       count(path) AS views
FROM log,
     articles,
     authors
WHERE path LIKE concat('/article/', slug)
  AND author = authors.id
GROUP BY name
ORDER BY views DESC;
