-- Author: Juan Luis Flores Garza
-- Date: 6/16/2017

CREATE Database PreciosEnergia

USE PreciosEnergia

-- 1. Create Tables
CREATE TABLE PML (
  [Hora] int NOT NULL,
  [Nodo] varchar(20) NOT NULL,
  [Precio] decimal(10,2) NOT NULL,
  [Energia] decimal(10,2) NOT NULL,
  [Perdidas] decimal(10,2) NOT NULL,
  [Congestion] varchar(10) NOT NULL,
  [timestamp] varchar(30) NOT NULL,
  [Tipo] varchar(3) NOT NULL,
  [Sistema] varchar(3) NOT NULL
);

CREATE TABLE PND (
  [Hora] int NOT NULL,
  [Zona de Carga] varchar(30) NOT NULL,
  [Precio Zonal] decimal(10,2) NOT NULL,
  [Energia] decimal(10,2) NOT NULL,
  [Perdidas] decimal(10,2) NOT NULL,
  [Congestion] decimal(10,2) NOT NULL,
  [timestamp] varchar(30) NOT NULL,
  [Tipo] varchar(3) NOT NULL,
  [Sistema] varchar(3) NOT NULL
);

-- 2. Python script to import csv files
  --  Implementar script para automatizar la importación de los datos en
  --  automáico a la base de datos.

-- 3. Count Reg to verify data import integrity of display full data info
  -- PML
SELECT COUNT(*) as [Number of Reg PML]
FROM [PreciosEnergia].[dbo].[PML]
  -- PND
SELECT COUNT(*) as [Number of Reg PND]
FROM [PreciosEnergia].[dbo].[PND]
  -- Display full PML and PND info
EXEC sp_spaceused 'PML'
EXEC sp_spaceused 'PND'

-- 4. Space used by tables
  -- PML full info 2016
CREATE TABLE PMLTEMP(
  [Hora] int NOT NULL,
  [Nodo] varchar(20) NOT NULL,
  [Precio] decimal(10,2) NOT NULL,
  [Energia] decimal(10,2) NOT NULL,
  [Perdidas] decimal(10,2) NOT NULL,
  [Congestion] varchar(10) NOT NULL,
  [timestamp] varchar(30) NOT NULL,
  [Tipo] varchar(3) NOT NULL,
  [Sistema] varchar(3) NOT NULL
);

INSERT INTO PMLTEMP ([Hora], [Nodo], [Precio], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema])
SELECT [Hora], [Nodo], [Precio], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema]
FROM PML
Where [timestamp] like '%2016%'

EXEC sp_spaceused 'PMLTEMP'
DROP TABLE PMLTEMP

  -- PND full info 2017
CREATE TABLE PNDTEMP(
  [Hora] int NOT NULL,
  [Zona de Carga] varchar(30) NOT NULL,
  [Precio Zonal] decimal(10,2) NOT NULL,
  [Energia] decimal(10,2) NOT NULL,
  [Perdidas] decimal(10,2) NOT NULL,
  [Congestion] decimal(10,2) NOT NULL,
  [timestamp] varchar(30) NOT NULL,
  [Tipo] varchar(3) NOT NULL,
  [Sistema] varchar(3) NOT NULL
);

INSERT INTO PNDTEMP ([Hora], [Zona de Carga], [Precio Zonal], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema])
SELECT [Hora], [Zona de Carga], [Precio Zonal], [Energia], [Perdidas], [Congestion], [timestamp], [Tipo], [Sistema]
FROM PND
Where [timestamp] like '%2016%'

EXEC sp_spaceused 'PMLTEMP'
DROP TABLE PNDTEMP
