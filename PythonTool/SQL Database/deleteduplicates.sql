-- Delete Duplicates
-- PML
WITH CTE_Dup AS(
  SELECT [Nodo], [Hora], [Precio], [Energia], [Perdidas], [Congestion], [Fecha], [Tipo], [Sistema],
  ROW_NUMBER()OVER(PARTITION BY Nodo, Fecha, Hora, Tipo, Sistema ORDER BY Sistema) as RN
  FROM [PreciosEnergia].[dbo].[PML]
) DELETE FROM CTE_Dup WHERE RN <> 1;

WITH CTE_Dup AS(
  SELECT [Zona de Carga], [Hora], [Precio Zonal], [Energia], [Perdidas], [Congestion], [Fecha], [Tipo], [Sistema],
  ROW_NUMBER()OVER(PARTITION BY [Zona de Carga], Fecha, Hora, Tipo, Sistema ORDER BY Sistema) as RN
  FROM [PreciosEnergia].[dbo].[PND]
) DELETE FROM CTE_Dup WHERE RN <> 1;
