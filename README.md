#zxopentuner-specjvm2008自动化测试
1、执行install_dou.sh 安装脚本所需py debs
出现pandas/opentuner error 需要修改源手动下载安装
python -3 -m pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple/
python -3 -m pip install opentuner -i https://pypi.tuna.tsinghua.edu.cn/simple/

2、配置flags
进入src/Flags 默认支持多种类型flags 可手动进行添加需要测试的flag在ZXauto/zxauto.csv中
个别jvm参数未添加到global文件中，需要手动将参数添加至src/Configurations/flags.csv flags.txt jvm_bool_flags.csv jvm_param_flags.csv中 ，再添加至自定义测试zxauto.csv中

3、执行
进入测试目录，比如specjvm2008.jar所在目录执行：
python /home/XXX/Hotspot_JVM_Tuner/src/specjvmTuner.py  --iterations=1  --configfile=specjvm_results --source=startup.scimark.fft --no-dups --flags=zxauto
输出结果位于TunedConfiguration/specjvm_results 文件中

note：
1、参数描述可参考Flags/jdk8参数描述.xlsx，默认支持jdk8及以下参数，对于jdk8以上，需要手动添加。
2、可以支持java code tuner
3、使用高版本sqlalchemy会导致opentuner报错 configuration.id 因此需要降低版本 ，建议使用1.2以下版本
pip install  sqlalchemy==1.2
