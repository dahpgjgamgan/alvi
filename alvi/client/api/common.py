def create_marker(pipe, id, name, node_id):
    pipe.send('create_marker', (id,), dict(
        id=id,
        name=name,
        node_id=node_id,
    ))


def move_marker(pipe, id, node_id):
    pipe.send('move_marker', (id,), dict(
        id=id,
        node_id=node_id,
    ))


def remove_marker(pipe, id):
    pipe.send('remove_marker', (id,), dict(
        id=id,
    ))


def update_stats(pipe, name, value):
    pipe.send("update_stats", (name, ), dict(
        name=name,
        value=value
    ))


def create_multi_marker(pipe, id, name, **kwargs):
    pipe.send('create_multi_marker', (id,), dict(
        id=id,
        name=name,
        **kwargs
    ))


def multi_marker_append(pipe, id, node_id):
    pipe.send('multi_marker_append', (id, node_id), dict(
        id=id,
        node_id=node_id,
    ))


def multi_marker_remove(pipe, id, node_id):
    pipe.send('multi_marker_remove', (id, node_id), dict(
        id=id,
        node_id=node_id,
    ))