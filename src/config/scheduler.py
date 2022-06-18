from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

executors = {
    'default': ThreadPoolExecutor(20)
}
scheduler = BackgroundScheduler(executors=executors, timezone="america/sao_paulo")
