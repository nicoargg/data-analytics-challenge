CREATE TABLE porprovincia AS(
	SELECT provincia, categoria, COUNT(categoria) 
	FROM tabla_completa 
	GROUP BY provincia, categoria ORDER BY provincia
);
