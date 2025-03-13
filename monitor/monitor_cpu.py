from lib.base import doc, MonitorBase, shell_cmd
import logging


class MonitorCPU(MonitorBase):
    def init(self):
        ...
        self._cpu = 0
        self._gpu = 0

    def check(self):
        try:
            # 执行sar命令获取CPU利用率
            cpu_load = shell_cmd('sar 1 1') 
            # 解析输出
            for line in cpu_load.splitlines():
                if "Average" in line:
                    parts = line.split()
                    # 假设输出格式为：Average:       %user     %nice   %system   %iowait    %steal     %idle
                    user = float(parts[2])
                    system = float(parts[4])
                    idle = float(parts[7])
                    
                    # 计算总负载率 (非空闲时间占比)
                    total_load = 100.0 - idle
                    self._cpu = round(total_load, 3)
                    logging.INFO(F"Current CPU load: {self._cpu}%")
                    return self._cpu
                
        except FileNotFoundError:
            print("The 'sar' command is not found. Please ensure sysstat package is installed.")
            return None
        

    @doc(log='cpu负载超过90%',notice='当前cpu使用90%，当使用容量超过95%，将会删除旧数据，如有需要，请及时备份')
    def event_cpu_load(self):
        if self._cpu > 90:
            return True
        else:
            logging.info(f"current cpu load: {self._cpu}%")
            return False

    @doc(log='gpu负载超过90%',notice='当前cpu使用90%，当使用容量超过95%，将会删除旧数据，如有需要，请及时备份')
    def event_gpu_load(self):
        if self._gpu > 90:
            return True
        else:
            return False



if __name__ == "__main__":

    mon = MonitorCPU()
    mon.check()
