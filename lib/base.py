import logging
import threading
import time
import subprocess


def doc(**kwargs):
    def wrap_func(func):
        def inner(self):
            # tmp = [line.strip() for line in func.__doc__.strip().split('\n')]
            res = func(self)
            if res:
                logging.info(kwargs.get('log',''))
            return res,kwargs

        return inner
    return wrap_func

def shell_cmd(cmd):
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode('utf8', errors="ignore")
    return output

class MonitorBase:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.init()
    
    def init(self):
        ...

    @property
    def events(self):
        for event_name in dir(self):
            if 'event_' == event_name[:6]:
                # self.logger.info(f'Event name: {event_name}')
                bar = getattr(self, event_name)
                yield bar()

class ThreadCls:
    def __init__(self,**kw):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.period = kw.get('period',1)
        self.funcs = kw.get('funcs',[])


        self.run_flag = False
        self.main_loop_thread = threading.Thread(target=self.main_loop)


    def start(self):
        self.run_flag = True
        self.main_loop_thread.setDaemon(True)
        self.main_loop_thread.start()

    def stop(self):
        self.run_flag = False
        self.main_loop_thread.join()
        print("Thread has stopped.")
    def main_loop(self):
        while self.run_flag:
            try:
                for func in self.funcs:
                    func()

                time.sleep(self.period)
            except:
                break
        # print("Thread has stopped.")



class MonSchedulerBase:
    def __init__(self):
        self.module = {}
        self.threads = []
        self.init()
        self.start_threads()

    def start_threads(self):
        for th in self.threads:
            th.start()
    def stop_threads(self):
        for th in self.threads:
            th.stop()
    @property
    def events(self):
        for mod in self.module:
            for ev in self.module[mod].events:
                yield ev
    def create_thread(self,period,modules):
        funcs = [self.module[el].check for el in modules]
        self.threads.append(ThreadCls(period=period,funcs=funcs))








if __name__ == "__main__":

    mon = MonScheduler()
    mon.module['MonitorHD']._loss = 91
    for ev in mon.events:
        a = ev

    mon.init_threads()
    mon.start_threads()
    # t = ThreadCls(period=0.1,funcs=[mon.module['MonitorHD'].check])
    # t.start()
    #
    for i in range(3):
        time.sleep(1)

    mon.stop_threads()

    # m = MonitorHD()
    # m._loss = 91
    # # doc_string = m.event_hd_drive_loss()
    # # print(doc_string)
    # for ev in m.events:
    #     a = ev