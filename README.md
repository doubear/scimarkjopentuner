# scimarkjopentuner
Automated testing of SCIMarKJ

1、执行install_dou.sh 安装脚本所需py debs
出现pandas/opentuner error 需要修改源手动下载安装
python -3 -m pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple/
python -3 -m pip install opentuner -i https://pypi.tuna.tsinghua.edu.cn/simple/

2、进入测试目录，比如specjvm2008.jar所在目录执行：
python /home/XXX/Hotspot_JVM_Tuner/src/specjvmTuner.py  --iterations=1  --configfile=specjvm_results --source=startup.scimark.fft --no-dups --flags=zxauto
输出结果位于TunedConfiguration/specjvm_results 文件中

使用高版本sqlalchemy会导致opentuner报错 configuration.id 因此需要降低版本 ，建议使用1.2以下版本
pip install  sqlalchemy==1.2
