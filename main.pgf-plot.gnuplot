set table "main.pgf-plot.table"; set format "%.5f"
set samples 200.0; plot [x=0:2] (1 + x**2 )* 2.7**(-x**2)
