-- Table: public.product

-- DROP TABLE IF EXISTS public.product;

CREATE TABLE IF NOT EXISTS public.product
(
    product_id integer NOT NULL,
    product_name character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    measure numeric(1000,0) NOT NULL,
    CONSTRAINT product_pkey PRIMARY KEY (product_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.product
    OWNER to postgres;