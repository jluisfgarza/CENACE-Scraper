-- Author: Juan Luis Flores Garza
-- Date: 7/7/2017

-- TESTING

/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (10) [Hora]
      ,[Nodo]
      ,[Precio]
      ,[Energia]
      ,[Perdidas]
      ,[Congestion]
      ,[Fecha]
      ,[Tipo]
      ,[Sistema]
  FROM [PreciosEnergia].[dbo].[PML]

-- PML
SELECT COUNT(*) as [Number of Reg PML]
FROM [PreciosEnergia].[dbo].[PML]

  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (100) [Hora]
      ,[Zona de Carga]
      ,[Precio Zonal]
      ,[Energia]
      ,[Perdidas]
      ,[Congestion]
      ,[Fecha]
      ,[Tipo]
      ,[Sistema]
  FROM [PreciosEnergia].[dbo].[PND]

  -- PND
SELECT COUNT(*) as [Number of Reg PND]
FROM [PreciosEnergia].[dbo].[PND]
