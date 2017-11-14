class Edge:
    def __init__(self, source, sink, capacity=1, flow=0):
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.flow = flow
        self.reverseEdge = None

    def __repr__(self):
        return "<Edge source:%s sink:%s capacity:%s flow:%s>" % (self.source, self.sink, self.capacity, self.flow)
