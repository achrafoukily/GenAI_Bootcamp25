#Daily Challenge : Pagination

import math
class Pagination :
  def __init__(self,items=None,page_size=10):
    self.items = items if items is not None else []
    self.page_size = page_size
    self.current_index = 0
    self.total_pages = math.ceil(len(items)/page_size)
  def get_visible_items(self):
        start = self.current_index
        end = self.current_index + self.page_size
        return self.items[start:end]
  def go_to_page(self, page_number):
    try:
        if 1 <= page_number <= self.total_pages:
            index = page_number - 1
            self.current_index = index * self.page_size
            return self.get_visible_items()
        else:
            return f"Invalid page number. Must be between 1 and {self.total_pages}"
    except Exception as e:
        return f"ValueError: {e}"
    
  def firts_page(self):
    return self.go_to_page(1)
  def last_page(self):
    return self.go_to_page(self.total_pages)
  def next_page(self):
    if self.current_index + self.page_size < len(self.items):
        self.current_index += self.page_size
    return self.get_visible_items()
  def previous_page(self):
    if self.current_index > 0:
        self.current_index -= self.page_size
    return self.get_visible_items()

