CREATE TABLE IF NOT EXISTS public.units(
    uid UUID DEFAULT gen_random_uuid(),
    xml_id INTEGER,
    name VARCHAR(200),
    quantity INTEGER,
    price NUMERIC(10,2),
    category VARCHAR(100),
    sales_date DATE
);
