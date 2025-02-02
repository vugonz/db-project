--1ª consulta OLAP:
SELECT ean, category_name, year, quarter, month,day_month, day_week, SUM(replenished_units) AS units, location_county FROM sales
WHERE day_month BETWEEN 1 AND 29
GROUP BY ROLLUP(day_week, location_county);


--2ª consulta OLAP:
SELECT ean, category_name, year, quarter, month,day_month, day_week, SUM(replenished_units) AS units, location_county, location_district FROM sales
WHERE location_district = 'LISBOA'
GROUP BY ROLLUP(location_county, day_week, category_name);