-- PML
WITH CTE AS(
  SELECT [Nodo], [Hora], [Precio], [Energia], [Perdidas], [Congestion], [Fecha], [Tipo], [Sistema],
  RN = ROW_NUMBER()OVER(PARTITION BY Nodo, Fecha, Hora, Tipo, Sistema ORDER BY Sistema)
  FROM dbo.PML
)
DELETE FROM CTE WHERE RN > 1;

WITH CTE AS(
  SELECT [Zona de Carga], [Hora], [Precio Zonal], [Energia], [Perdidas], [Congestion], [Fecha], [Tipo], [Sistema],
  RN = ROW_NUMBER()OVER(PARTITION BY [Zona de Carga], Fecha, Hora, Tipo, Sistema ORDER BY Sistema)
  FROM dbo.PND
)
DELETE FROM CTE WHERE RN > 1;
