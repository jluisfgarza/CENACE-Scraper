-- Author: Juan Luis Flores Garza
-- Date: 7/7/2017

CREATE Database PreciosEnergia

USE PreciosEnergia

-- Create Tables
CREATE TABLE PML (
  [Hora] int NOT NULL,
  [Nodo] varchar(20) NOT NULL,
  [Precio] decimal(10,2) NOT NULL,
  [Energia] decimal(10,2) NOT NULL,
  [Perdidas] decimal(10,2) NOT NULL,
  [Congestion] varchar(10) NOT NULL,
  [Fecha] smalldatetime,
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
  [Fecha] smalldatetime,
  [Tipo] varchar(3) NOT NULL,
  [Sistema] varchar(3) NOT NULL
);
