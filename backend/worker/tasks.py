from worker.celery_task import celery


@celery.task
def memory_calculation_task(model):
    return {'model_size': '28gb'}
