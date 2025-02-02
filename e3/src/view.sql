
DROP VIEW IF EXISTS sales;
CREATE VIEW sales
AS (

	SELECT ean, category_name, EXTRACT(YEAR FROM instant) AS year, EXTRACT(QUARTER FROM instant) AS quarter, EXTRACT(MONTH FROM instant) AS month, EXTRACT(DAY FROM instant) AS day_month, EXTRACT(DOW FROM instant) AS day_week, location_district, location_county, replenished_units
	FROM (
	SELECT ean, category_name, instant, replenished_units, location_district, location_county
	FROM replenishment_event NATURAL JOIN responsible_for NATURAL JOIN installed_at NATURAL JOIN point_of_retail) AS base_table
);
