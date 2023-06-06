#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from queue import Queue
from threading import Lock, Thread


def manager(lock, q):
    with lock:
        tasks = []
        while not q.empty():
            task = q.get()
            worker = random.choice(workers)
            print(f"Менеджер передал задачу '{task}' работнику {worker}")
            tasks.append({
                "Задача": task,
                "Работник": worker
            })

    for task in tasks:
        if task["Работник"] is None:
            print(f"Задача '{task['Задача']}' ожидает выполнения")


def worker(lock, q, worker_id):
    with lock:
        while not q.empty():
            task = q.get()
            print(f"Работник {worker_id} выполняет задачу: '{task}'")


if __name__ == "__main__":
    tasks = ["Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5"]
    workers = ["Работник A", "Работник B", "Работник C"]
    lock = Lock()
    q = Queue()

    for task in tasks:
        q.put(task)

    for worker_id in workers:
        Thread(target=worker, args=(lock, q, worker_id)).start()

    Thread(target=manager, args=(lock, q)).start()
