WITH RECURSIVE GENERATION_DATA AS (
    SELECT ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT E.ID, EL.GENERATION + 1
    FROM ECOLI_DATA E INNER JOIN GENERATION_DATA EL ON E.PARENT_ID = EL.ID
)
SELECT COUNT(*) AS COUNT, GENERATION
FROM GENERATION_DATA G LEFT JOIN ECOLI_DATA E ON G.ID = E.PARENT_ID
WHERE E.ID IS NULL
GROUP BY GENERATION
ORDER BY GENERATION;