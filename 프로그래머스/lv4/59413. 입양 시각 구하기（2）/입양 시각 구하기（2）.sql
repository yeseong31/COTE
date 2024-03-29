WITH RECURSIVE HOUR_TABLE(HOUR) AS (
    SELECT 0 AS HOUR
    UNION
    SELECT HOUR + 1 FROM HOUR_TABLE WHERE HOUR < 23
)
SELECT HOUR_TABLE.HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM HOUR_TABLE
LEFT OUTER JOIN ANIMAL_OUTS
ON HOUR_TABLE.HOUR = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR