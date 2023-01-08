from hazelcast import HazelcastClient


class Cash:
    def __init__(self):
        self.hz_client = HazelcastClient(
            cluster_name="dev",
            cluster_members=[
                "localhost:8080"
            ]
        )

    def get(self):
        return self.hz_client.get_map('books').blocking()

    def close(self):
        self.hz_client.shutdown()