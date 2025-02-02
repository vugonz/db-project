DROP TRIGGER IF EXISTS super_category_child ON has_other;
DROP TRIGGER IF EXISTS planogram_limit_units ON replenishment_event;
DROP TRIGGER IF EXISTS shelf_category ON replenishment_event;

-- IC-1, a category cannot contain itself

CREATE OR REPLACE FUNCTION chk_super_category_child()
RETURNS TRIGGER AS
$$
BEGIN
	IF NEW.super_category = NEW.category THEN
		RAISE EXCEPTION 'Category "%" cannot contain itself.', NEW.super_category;
	END IF;
	
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER super_category_child
BEFORE UPDATE OR INSERT ON has_other
FOR EACH ROW EXECUTE PROCEDURE chk_super_category_child();

-- IC-2, the number of unites in a replenishment event cannot exceed the amount of units stated in the planogram

CREATE OR REPLACE FUNCTION chk_planogram_units_limit()
RETURNS TRIGGER AS
$$
DECLARE limit_units INT;

BEGIN

	SELECT units INTO limit_units
	FROM planogram p 
	WHERE p.ean = NEW.ean AND p.shelf_number = NEW.shelf_number AND p.serial_number = NEW.serial_number AND p.manufacturer = NEW.manufacturer; 

	IF NEW.replenished_units > limit_units THEN
		RAISE EXCEPTION 'Replenished units, "%", exceed the max limit of units, "%", specified in the planogram.', NEW.replenished_units, limit_units;
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER planogram_limit_units
BEFORE INSERT ON replenishment_event
FOR EACH ROW EXECUTE PROCEDURE chk_planogram_units_limit();
	
-- IC-3, a product can only be replenished in a shelf that is destined for at least one of its categories

CREATE OR REPLACE FUNCTION chk_shelf_category()
RETURNS TRIGGER AS
$$
DECLARE shelf_category VARCHAR(80);

BEGIN
	SELECT category_name INTO shelf_category
	FROM shelf s
	WHERE s.shelf_number = NEW.shelf_number AND s.serial_number = NEW.serial_number AND s.manufacturer = NEW.manufacturer;

	IF shelf_category NOT IN (
		SELECT category_name
		FROM has_category p
		WHERE p.ean = NEW.ean) THEN
		RAISE EXCEPTION 'Shelf is not destined for the categories of product with ean "%".', NEW.ean;
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER shelf_category
BEFORE INSERT ON replenishment_event
FOR EACH ROW EXECUTE PROCEDURE chk_shelf_category();
