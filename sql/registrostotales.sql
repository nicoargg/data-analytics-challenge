CREATE TABLE registrostotales AS(
    select categoria, count(categoria) 
    from tabla_completa group by categoria
);
