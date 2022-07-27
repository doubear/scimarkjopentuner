'''
#Author:Doubear
#Date:07/07/2022
# This program contains the functionality to tune jvm flags to improve
# given gcbs java program performance
'''
import argparse
import re

import jvmtunerInterface
from jvmtunerInterface import JvmFlagsTunerInterface

argparser = argparse.ArgumentParser(parents=[jvmtunerInterface.argparser])
argparser.add_argument(
  '--jvm_spec_startup', default='java -jar scimark.jar  1 {source} DEFAULT  --jvmArgs "{Opt_flags}"',
  help='command template to JVMSPEC2008 statup program tuning.. ')

argparser.add_argument('--spec_type', help='Select between startup and non_startup', default='startup')
class SpecJvmTuner(JvmFlagsTunerInterface):
    
    def __init__(self, *pargs, **kwargs):
        super(SpecJvmTuner, self).__init__(args, *pargs,
                                        **kwargs)
    
    def execute_program(self):
        temp_metric=0
        for i in range(0,int(args.iterations)):
            print 'running iteration '+str(i)
            if(args.spec_type == 'startup'):
                run_result = self.call_program(args.jvm_spec_startup.format(source=args.source,Opt_flags=self.flags))
                print('run_result '+run_result['stderr'])
            elif(args.spec_type == 'non_startup'):
                run_result = self.call_program(args.jvm_spec_nonstartup.format(source=args.source,Opt_flags=self.flags))
            temp_metric=temp_metric+self.get_ms_per_op_jvm(run_result['stderr'])
        temp_metric=float(temp_metric/int(args.iterations))
        return temp_metric
    
    def get_ms_per_op_jvm(self,result):
        m=re.search('COUNT\|[0-9]*.[0-9]*',result,flags=re.DOTALL)
        ops_m=1
        print("current m:%s" % m)
        if m:
            ops_m=m.group(0)
            ops_m =re.sub('COUNT\|','',ops_m)
            print('current ops_m '+ops_m)
            ops_m = re.sub('|0|lph','',ops_m)
        try:
            ops_m=float(ops_m)/95.93
        except:
            ops_m=1
    
        time_per_op=6000.0/ops_m
        return  time_per_op


if __name__ == '__main__':
    args = argparser.parse_args()
    SpecJvmTuner.main(args)
