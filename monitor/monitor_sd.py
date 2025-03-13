from lib.base import doc, MonitorBase


class MonitorSD(MonitorBase):
    def init(self):
        self._capa = 10
        self._loss = 10
        self._sdrate = 500

    def check(self):
        ...
        # print('SD Check')
        # cmd = "dd if=/dev/zero bs=1M count=50 of=/home/nvidia/vbox/bin/recorder_sd/test1.img oflag=direct 2>sd.txt"
        # #os.system(cmd)
        # self._sdrate = 100

    @doc(log='SD写入速率过慢',notice='SD写入速率过慢')
    def event_sd_write_rate_slow(self):
        if self._sdrate < 200:
            return True
        else:
            return False

    @doc(log='SD容量超过90%',notice='当前SD容量使用90%，当使用容量超过95%，将会删除旧数据，如有需要，请及时备份')
    def event_sd_over_capacity(self):
        if self._capa > 90:
            return True
        else:
            return False

    @doc(log='系统启动后，检测不到SD存在',notice='系统未检测SD，请检查')
    def event_sd_drive_loss(self):
        if self._loss > 90:
            return True
        else:
            return False



if __name__ == "__main__":

    mon = MonitorSD()

    print(mon.event_sd_over_capacity())
    mon._capa = 95
    test_result, meta = mon.event_sd_over_capacity()
    if test_result:
        print(meta)
    # for ev in mon.events:
    #     print(ev)