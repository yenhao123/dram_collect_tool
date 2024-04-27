if [ -z $1 ]; then
	echo "缺目錄參數"
	exit 1
fi
if [ -d "/tmp2/mem_trace/$1/" ]; then
    sudo cp perf.data perf.data.old trace.csv trace.out "/tmp2/mem_trace/$1/"
    echo "文件已複製到目錄 /tmp2/mem_trace/$1/"
else
    echo "錯誤：目錄 /tmp2/mem_trace/$1/ 不存在。退出。"
    exit 1
fi
