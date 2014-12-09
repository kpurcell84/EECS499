set title "Traceroute ICMP CDF (74,051 hosts reached)"
set terminal postscript color
set term postscript enhanced eps color font "Helvetica,20"
set output "output.ps"
set datafile commentschars "#%"
set datafile separator ","
set xlabel "Hops to host"
set ylabel "CDF of Hosts"
set style data points
set autoscale fix
set xtics nomirror rotate by -45 font ",20"
set ytics nomirror  font ",20"
set key font ",20"
set xlabel font ",20" offset 0,-2,0
set ylabel font ",20"
set grid

set key bottom right
	
set style line 1 linecolor rgb '#925476' linetype 1 linewidth 3 
set style line 2 linecolor rgb '#005789' linetype 1 linewidth 3 
set style line 3 linecolor rgb '#6c8338' linetype 1 linewidth 3 
set style line 4 linecolor rgb '#ca7700' linetype 1 linewidth 3 
set style line 5 linecolor rgb '#675331' linetype 1 linewidth 3 
set style line 6 linecolor rgb '#813050' linetype 1 linewidth 3 
set style line 7 linecolor rgb '#a73c32' linetype 1 linewidth 3 
set style line 8 linecolor rgb '#456638' linetype 1 linewidth 3 
set style line 9 linecolor rgb '#358500' linetype 1 linewidth 3 
set style line 10 linecolor rgb '#3d87aa' linetype 1 linewidth 1.5 
set style line 11 linecolor rgb '#c85d28' linetype 1 linewidth 1.5 
set style line 12 linecolor rgb '#979281' linetype 1 linewidth 1.5 
set style line 13 linecolor rgb '#d55258' linetype 1 linewidth 1.5 

set xrange [0:60]

plot filename using 1:2 title "Hosts Reached" with lines ls 4;
