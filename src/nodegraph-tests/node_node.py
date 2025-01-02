from node_graphics_node import QDMGraphicsNode


class Node():
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene
        self.title = title
        self.gr_node = QDMGraphicsNode(self, self.title)
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.gr_node)

        # self.gr_node.title = "new title"
        
        self.inputs = []
        self.outputs = []
