CREATE OR REPLACE FUNCTION add_numbers()
RETURNS INT
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN 10 + 20;
END;
$$;
select * from add_numbers();

CREATE OR REPLACE FUNCTION salary_audit_function()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO salary_audit
    VALUES (
        OLD.employee_id,
        OLD.salary,
        NEW.salary
    );
    RETURN NEW;
END;
$$;
CREATE TRIGGER salary_update_trigger
AFTER UPDATE OF salary
ON employees
FOR EACH ROW
EXECUTE FUNCTION salary_audit_function();


Syntax: create index idx_index_name on tablename(column_name)

CREATE INDEX idx_appointment_patient ON appointments(patient_id);




1. Create Index
2. Multiple Column Index
3. Unique Index
4. Drop Index


CREATE INDEX idx_appointment_patient
ON appointments(patient_id);


CREATE INDEX idx_customer_name_city
ON customers(customer_name, city);

CREATE UNIQUE INDEX idx_customer_email
ON customers(email);

DROP INDEX idx_customer_email;

