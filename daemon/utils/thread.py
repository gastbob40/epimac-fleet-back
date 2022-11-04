import threading


def run_mac_action_async(entities, function):
    threads = []

    for entity in entities:
        th = threading.Thread(target=function, args=(entity,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
