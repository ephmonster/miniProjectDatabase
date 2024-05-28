BEGIN;


CREATE TABLE IF NOT EXISTS public.airplane
(
    serialnumber integer NOT NULL,
    datemanufactored date NOT NULL,
    dateacquired date NOT NULL,
    in_service integer NOT NULL,
    makeandmodel character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airplane_pkey PRIMARY KEY (serialnumber)
);

CREATE TABLE IF NOT EXISTS public.airplanetug
(
    licensenumber character varying COLLATE pg_catalog."default" NOT NULL,
    weightcapacity integer NOT NULL,
    yearsinuse integer NOT NULL,
    manufacturer character varying COLLATE pg_catalog."default" NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airplanetug_pkey PRIMARY KEY (licensenumber)
);

CREATE TABLE IF NOT EXISTS public.airplanetype
(
    makeandmodel character varying COLLATE pg_catalog."default" NOT NULL,
    capacity integer NOT NULL,
    maxspeed integer NOT NULL,
    range integer NOT NULL,
    lifetime integer NOT NULL,
    typeoffuel character varying COLLATE pg_catalog."default" NOT NULL,
    weight integer NOT NULL,
    CONSTRAINT airplanetype_pkey PRIMARY KEY (makeandmodel)
);

CREATE TABLE IF NOT EXISTS public.fuelingtruck
(
    licenseplate character varying COLLATE pg_catalog."default" NOT NULL,
    horsepower integer NOT NULL,
    yearsinuse integer NOT NULL,
    lastmaintained date NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT fuelingtruck_pkey PRIMARY KEY (licenseplate)
);

CREATE TABLE IF NOT EXISTS public.fuelstock
(
    litersinstock integer NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    typeoffuel character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT fuelstock_pkey PRIMARY KEY (location, typeoffuel)
);

CREATE TABLE IF NOT EXISTS public.fueltype
(
    typeoffuel character varying COLLATE pg_catalog."default" NOT NULL,
    price double precision NOT NULL,
    CONSTRAINT fueltype_pkey PRIMARY KEY (typeoffuel)
);

CREATE TABLE IF NOT EXISTS public.gate
(
    gatenumber integer NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT gate_pkey PRIMARY KEY (gatenumber, location)
);

CREATE TABLE IF NOT EXISTS public.jetbridge
(
    serialnumber integer NOT NULL,
    yearsinuse integer NOT NULL,
    weightlimit integer NOT NULL,
    gatenumber integer NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT jetbridge_pkey PRIMARY KEY (serialnumber)
);

CREATE TABLE IF NOT EXISTS public.landingtakingoff
(
    date date NOT NULL,
    lt integer NOT NULL,
    serialnumber integer NOT NULL,
    "number" integer NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    "flightID" integer NOT NULL,
    CONSTRAINT landingtakingoff_pkey PRIMARY KEY ("flightID")
);

CREATE TABLE IF NOT EXISTS public.runway
(
    length integer NOT NULL,
    weightcapacity integer NOT NULL,
    "number" integer NOT NULL,
    orientation character varying COLLATE pg_catalog."default" NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT runway_pkey PRIMARY KEY ("number", location)
);

CREATE TABLE IF NOT EXISTS public.truckload
(
    litersoffuel integer NOT NULL,
    date date NOT NULL,
    licenseplate character varying COLLATE pg_catalog."default" NOT NULL,
    location character varying COLLATE pg_catalog."default" NOT NULL,
    typeoffuel character varying COLLATE pg_catalog."default" NOT NULL,
    "truckloadID" integer NOT NULL,
    CONSTRAINT truckload_pkey PRIMARY KEY ("truckloadID")
);

CREATE TABLE IF NOT EXISTS public.tugs
(
    date date NOT NULL,
    fuelremainingaftertug integer NOT NULL,
    licensenumber character varying COLLATE pg_catalog."default" NOT NULL,
    serialnumber integer NOT NULL,
    tugsnumber integer NOT NULL,
    CONSTRAINT tugs_pkey PRIMARY KEY (tugsnumber)
);

ALTER TABLE IF EXISTS public.airplane
    ADD CONSTRAINT airplane_makeandmodel_fkey FOREIGN KEY (makeandmodel)
    REFERENCES public.airplanetype (makeandmodel) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.airplanetype
    ADD CONSTRAINT fueltype_fkey FOREIGN KEY (typeoffuel)
    REFERENCES public.fueltype (typeoffuel) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.fuelstock
    ADD CONSTRAINT fuelstock_typeoffuel_fkey FOREIGN KEY (typeoffuel)
    REFERENCES public.fueltype (typeoffuel) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.jetbridge
    ADD CONSTRAINT jetbridge_gatenumber_location_fkey FOREIGN KEY (gatenumber, location)
    REFERENCES public.gate (gatenumber, location) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.landingtakingoff
    ADD CONSTRAINT landingtakingoff_serialnumber_fkey FOREIGN KEY (serialnumber)
    REFERENCES public.airplane (serialnumber) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.landingtakingoff
    ADD CONSTRAINT runway_fkey FOREIGN KEY (location, "number")
    REFERENCES public.runway (location, "number") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.truckload
    ADD CONSTRAINT truckload_fk1 FOREIGN KEY (licenseplate)
    REFERENCES public.fuelingtruck (licenseplate) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.truckload
    ADD CONSTRAINT truckload_fk2 FOREIGN KEY (typeoffuel)
    REFERENCES public.fueltype (typeoffuel) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.tugs
    ADD CONSTRAINT tugs_fk1 FOREIGN KEY (licensenumber)
    REFERENCES public.airplanetug (licensenumber) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.tugs
    ADD CONSTRAINT tugs_fk2 FOREIGN KEY (serialnumber)
    REFERENCES public.airplane (serialnumber) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;
