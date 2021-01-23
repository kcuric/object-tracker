LAST_ORDER_ID = None

def get_last_order_id():
  return LAST_ORDER_ID

def set_last_order_id(id):
  global LAST_ORDER_ID
  LAST_ORDER_ID = id