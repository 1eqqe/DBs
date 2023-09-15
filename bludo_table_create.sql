-- Table: public.bludo

-- DROP TABLE IF EXISTS public.bludo;

CREATE TABLE IF NOT EXISTS public.bludo
(
    bludo_id integer NOT NULL,
    bludo_type character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    weight_bludo numeric(1000,0) NOT NULL,
    recipe character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    callories numeric(1000,0) NOT NULL,
    "carbs capacity" numeric(1000,0) NOT NULL,
    CONSTRAINT bludo_pkey PRIMARY KEY (bludo_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.bludo
    OWNER to postgres;