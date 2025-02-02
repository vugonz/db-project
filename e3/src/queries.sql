-- Query 1 - What is the name of the retailer responsible for the most amount of categories?

SELECT retailer_name
FROM responsible_for NATURAL JOIN retailer
GROUP BY retailer_name
HAVING COUNT(DISTINCT category_name) >= ALL (
	SELECT COUNT(DISTINCT category_name)
	FROM responsible_for
	GROUP BY tin
);

-- Query 2 - What is the name of the retailers responsible for all simple categories?
-- Division using EXCEPT and correlated queries

SELECT retailer_name
FROM retailer r
WHERE NOT EXISTS (
	SELECT category_name
	FROM simple_category
	EXCEPT
	SELECT DISTINCT category_name
	FROM responsible_for NATURAL JOIN retailer RR
	WHERE RR.retailer_name = r.retailer_name
);

-- Query 3 - What are the ean of the products that have never been replaced? 

SELECT ean
FROM product
EXCEPT
SELECT DISTINCT ean
FROM replenishment_event;

-- Query 4 - What are the ean of the products that have always been replaced by the same retailer? 

SELECT ean
FROM replenishment_event
GROUP BY ean
HAVING COUNT(DISTINCT tin) = 1;
