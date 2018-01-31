f(x,y)=(sin(x)*sin(y)/(x*y))**2

set xrange [-15:15]
set yrange [-15:15]
set pm3d map
set size square
set palette gray positive
set isosample 1000,1000
splot f(x,y)
