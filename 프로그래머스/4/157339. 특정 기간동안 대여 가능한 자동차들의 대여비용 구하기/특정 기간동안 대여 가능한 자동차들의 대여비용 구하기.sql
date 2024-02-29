SELECT CAR_ID, CAR_TYPE, FLOOR(DAILY_FEE * (1 - DISCOUNT_RATE / 100) * 30) AS FEE
FROM CAR_RENTAL_COMPANY_CAR
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN USING(CAR_TYPE)
WHERE CAR_TYPE IN ('세단', 'SUV') 
    AND DURATION_TYPE = '30일 이상'
    AND CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01'
    )
HAVING FEE BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC