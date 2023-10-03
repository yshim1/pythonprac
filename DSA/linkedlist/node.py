class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
#At end of node path, link to next node is null because there are no more nodes left. In python this means it will be set to None
  def get_value(self):
    return self.value
  def get_link_node(self):
    return self.link_node
def set_link_node(self, link_node):
    self.link_node = link_node