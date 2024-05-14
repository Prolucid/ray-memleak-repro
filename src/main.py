import ray
from actors.minimal import MinimalActor


def main():
    ray.init()
    minimal_actor_ref = MinimalActor.remote()

    while True:
        ray.get(minimal_actor_ref.do_work.remote())  # type: ignore


if __name__ == "__main__":
    main()
