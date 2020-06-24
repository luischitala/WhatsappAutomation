from datetime import datetime
from compra import recordatorio
from apscheduler.schedulers.blocking import BlockingScheduler




sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(recordatorio, 'interval', seconds=5)

sched.start()