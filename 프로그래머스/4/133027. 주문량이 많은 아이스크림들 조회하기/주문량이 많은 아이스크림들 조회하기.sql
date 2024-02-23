SELECT F.FLAVOR
FROM JULY J RIGHT OUTER JOIN FIRST_HALF F ON J.FLAVOR = F.FLAVOR
GROUP BY F.FLAVOR
ORDER BY (F.TOTAL_ORDER + SUM(J.TOTAL_ORDER)) DESC
LIMIT 3