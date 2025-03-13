import lib
import time
import logging




if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)-10s - %(levelname)-6s - %(message)s',
        filename='app.log'
    )
    logger = logging.getLogger(__name__)
    logger.info('Start')
    mon = lib.MonScheduler()

    # mon.module['MonitorHD']._loss = 80
    # mon.module['MonitorSD']._sdrate = 500
    # mon.module['MonitorCPU']._cpu = 91
    for ev in mon.events:
        a = ev
    #     print(a)


    for i in range(3):
    # while True:
        time.sleep(1)
        res = [(test_result,para) for test_result,para in mon.events if test_result==True]

        # print(res)

    mon.stop_threads()
