-- Table: public.needs

-- DROP TABLE IF EXISTS public.needs;

CREATE TABLE IF NOT EXISTS public.needs
(
    bludo_id integer NOT NULL,
    product_id integer NOT NULL,
    product_volume character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT needs_pkey PRIMARY KEY (product_volume),
    CONSTRAINT bludo_id FOREIGN KEY (bludo_id)
        REFERENCES public.bludo (bludo_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT product_id FOREIGN KEY (product_id)
        REFERENCES public.product (product_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.needs
    OWNER to postgres;