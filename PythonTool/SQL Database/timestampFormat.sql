-- Author: Juan Luis Flores Garza
-- Date: 7/7/2017

-- After every data import to the DB ejectute the following query to format timestamp
  ALTER TABLE PML
  ALTER COLUMN timestamp smalldatetime;

  ALTER TABLE PND
  ALTER COLUMN timestamp smalldatetime;
