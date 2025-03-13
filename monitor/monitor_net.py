# import sys
# sys.path.append('/root/duuboo/calmvergemon')
# print(sys.path)
from lib.base import doc, MonitorBase, shell_cmd
import logging


class MonitorNET(MonitorBase):
    def init(self):
        self._net = 0
        self.lines = []

    def check(self):
        try:
            # 执行sar命令获取CPU利用率
            net_load = shell_cmd('sar -n DEV 1 1') 
            # print(net_load)
            # 解析输出
            for line in net_load.splitlines():
                self.lines.append(line)
            if "Average" in self.lines[-1]:
                parts = self.lines[-1].split()
                # 假设输出格式为：Average:    rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s   %ifutil
                net_load = parts[9]
                
                self._net = float(net_load)
                return self._net
                
        except FileNotFoundError:
            print("The 'sar' command is not found. Please ensure sysstat package is installed.")
            return None
        

    @doc(log='网络负载超过90%',notice='当前网络带宽使用90%，当使用容量超过95%，将会删除旧数据，如有需要，请及时备份')
    def event_net_load(self):
        if self._net > 90:
            return True
        else:
            logging.info(f"current net load: {self._net}%")
            return False



if __name__ == "__main__":

    mon = MonitorNET()
    mon.check()
