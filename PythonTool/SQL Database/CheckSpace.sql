-- Author: Juan Luis Flores Garza
-- Date: 7/7/2017

-- Space used by tables
  -- PML full info by year
CREATE TABLE PMLTEMP(
  [Hora] int NOT NULL,
  [Nodo] varchar(20) NOT NULL,
  [Precio] decimal(10,2) NOT NULL,
  [Energia] decimal(10,2) NOT NULL,
  [Perdidas] decimal(10,2) NOT NULL,
  [Congestion] varchar(10) NOT NULL,
  [timestamp] smalldatetime,
  [Tipo] varchar(3) NOT NULL,
  [Sistema] varchar(3) NOT NULL
);

INSERT INTO PMLTEMP ([Hora], [Nodo], [Precio], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema])
SELECT [Hora], [Nodo], [Precio], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema]
FROM PML
Where [timestamp] like '%2016%' -- Change year or erase line to check full table size

EXEC sp_spaceused 'PMLTEMP'
DROP TABLE PMLTEMP

  -- PND full info by year
CREATE TABLE PNDTEMP(
  [Hora] int NOT NULL,
  [Zona de Carga] varchar(30) NOT NULL,
  [Precio Zonal] decimal(10,2) NOT NULL,
  [Energia] decimal(10,2) NOT NULL,
  [Perdidas] decimal(10,2) NOT NULL,
  [Congestion] decimal(10,2) NOT NULL,
  [timestamp] smalldatetime,
  [Tipo] varchar(3) NOT NULL,
  [Sistema] varchar(3) NOT NULL
);

INSERT INTO PNDTEMP ([Hora], [Zona de Carga], [Precio Zonal], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema])
SELECT [Hora], [Zona de Carga], [Precio Zonal], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema]
FROM PND
Where [timestamp] like '%2016%' -- Change year or erase line to check full table size

EXEC sp_spaceused 'PMLTEMP'
DROP TABLE PNDTEMP
