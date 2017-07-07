-- Author: Juan Luis Flores Garza
-- Date: 7/7/2017

-- Count Reg to verify data import integrity of display full data info

  -- PML
SELECT COUNT(*) as [Number of Reg PML]
FROM [PreciosEnergia].[dbo].[PML]

  -- PND
SELECT COUNT(*) as [Number of Reg PND]
FROM [PreciosEnergia].[dbo].[PND]

  -- Display full PML and PND info
EXEC sp_spaceused 'PML'
EXEC sp_spaceused 'PND'
