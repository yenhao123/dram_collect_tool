#!/bin/bash

if [ -z "$1" ]; then
	echo "未更改 benchmark"
	exit 1
fi

benchmark_app -m ../benchmark/openvino/intel/text-to-speech-en-0001/text-to-speech-en-0001-duration-prediction/FP32/text-to-speech-en-0001-duration-prediction.xml -t 4000

