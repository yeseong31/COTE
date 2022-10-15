SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO A, (
    SELECT FOOD_TYPE FT, MAX(FAVORITES) MF
    FROM REST_INFO
    GROUP BY FOOD_TYPE
) M
WHERE A.FOOD_TYPE = M.FT AND A.FAVORITES = M.MF
ORDER BY FOOD_TYPE DESC
