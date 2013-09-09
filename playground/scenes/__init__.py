import inspect
import collections

from .booble import Booble
from .booble_cartesian import BoobleCartesian
from .create_tree import CreateTree
from .binary_search_tree import BinarySearchTree
from .linear_search import LinearSearch


class Pipe:
    def __init__(self, queue):
        self.queue = queue
        self._backlog = collections.OrderedDict()

    def send(self, action_type, key, message):
        message['type'] = action_type #TODO temp workaround
        key = (action_type, ) + key
        self._backlog[repr(key)] = message

    def sync(self):
        #TODO optimize data and stats (send only latest value if entry occurs multiple times)
        #message is sent asynchronously, so we need to make a copy, before clearing
        backlog = list(self._backlog.values())
        self.queue.put(backlog)
        self._backlog.clear()


def register(scene_name, scene_function, Container):
    #TODO
    Container = Container.implementations()[0]

    def _run(queue):
        pipe = Pipe(queue)
        container = Container(pipe)
        return scene_function(container)

    source = inspect.getsource(scene_function)

    scenes.append((scene_name, _run, Container, source))


scenes = []