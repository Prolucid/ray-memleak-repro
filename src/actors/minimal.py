import ray


@ray.remote
class MinimalActor:
    def __init__(self):
        self._counter = 0

    def do_work(self) -> None:
        self._counter += 1
