SELECT
    TO_CHAR(rs.date, 'Month DD, YYYY') AS date,
    ROUND(rs.error_percentage, 2) AS error_percentage
FROM
    (SELECT
        total.date AS date,
            ((error.error_day * 1.0 / total.total_day * 1.0) * 100) AS error_percentage
    FROM
        (SELECT
        date, total_day
    FROM
        (SELECT
        DATE(time) AS date, COUNT(*) AS total_day
    FROM
        log
    GROUP BY date) AS total_day) AS total, (SELECT
        date, error_day
    FROM
        (SELECT
        DATE(time) AS date, COUNT(*) AS error_day
    FROM
        log
    WHERE
        status = '404 NOT FOUND'
    GROUP BY date , status) AS error_day) AS error
    WHERE
        total.date = error.date) rs
WHERE
    rs.error_percentage > 1;
