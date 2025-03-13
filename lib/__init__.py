import logging
import time


from monitor.monitor_hd import MonitorHD
from monitor.monitor_sd import MonitorSD
from monitor.monitor_cpu import MonitorCPU
from monitor.monitor_net import MonitorNET
from lib.base import MonSchedulerBase


class MonScheduler(MonSchedulerBase):
    def init(self):
        # self.module['MonitorHD'] = MonitorHD()
        # self.module['MonitorSD'] = MonitorSD()
        self.module['MonitorCPU'] = MonitorCPU()
        self.module['MonitorNET'] = MonitorNET()
        # self.create_thread(period=0.1,modules=['MonitorHD'])
        # self.create_thread(period=1,modules=['MonitorSD'])
        self.create_thread(period=1,modules=['MonitorCPU'])
        self.create_thread(period=1,modules=['MonitorNET'])

if __name__ == "__main__":
    ...