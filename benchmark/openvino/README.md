## 透過 DNN benchmark 評估硬體的效能
>教學
>https://blog.openvino.ai/blog-posts/build-cpp-benchmark-linux

install openvino + building environment
https://docs.openvino.ai/2023.3/openvino_docs_install_guides_installing_openvino_apt.html

download model
>from pre_trained model or yours
>>pretrained https://docs.openvino.ai/archive/2023.1/omz_models_group_intel.html
>
>指令: omz_downloader 
```
omz_downloader --name [model_name/model_path]
```

評估模型
>指令: benchmark_app
>https://docs.openvino.ai/archive/2023.1/omz_models_group_public.html
>https://docs.openvino.ai/archive/2023.1/omz_models_group_intel.html
```
benchmark_app -m [model_path] -hint [throughput/latency]

# parameter
-hint: 更仔細的統計
-d: device
-t: time(s)
```
>FPS: frame per seconds 每秒鐘可以 inference 幾次

