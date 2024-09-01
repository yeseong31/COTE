SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK A JOIN BOOK_SALES B ON A.BOOK_ID = B.BOOK_ID
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') ='2022-01'
GROUP BY CATEGORY
ORDER BY CATEGORY