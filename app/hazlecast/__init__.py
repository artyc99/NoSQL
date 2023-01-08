from hazelcast import HazelcastClient

hz_client = HazelcastClient()

map = None


def create():
    map = hz_client.get_map('books').blocking()


def close():
    hz_client.shutdown()


create()
