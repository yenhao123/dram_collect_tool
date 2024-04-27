perf mem record -a sleep 3600
perf script -F comm,time,event,addr > out/trace.out
awk '{print $1 "," $2 "," $3 "," $4}' out/trace.out > out/trace.csv
