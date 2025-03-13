from lib.base import doc, MonitorBase


class MonitorHD(MonitorBase):
    def init(self):
        self._capa = 10
        self._loss = 10

    def check(self):
        ...
        # print('HD Check')

    @doc(log='硬盘容量超过90%',notice='当前硬盘容量使用90%，当使用容量超过95%，将会删除旧数据，如有需要，请及时备份')
    def event_hd_over_capacity(self):
        if self._capa > 90:
            return True
        else:
            return False

    @doc(log='系统启动后，检测不到硬盘存在',notice='系统未检测到硬盘，请检查')
    def event_hd_drive_loss(self):
        if self._loss > 90:
            return True
        else:
            return False



if __name__ == "__main__":

    mon = MonitorSD()