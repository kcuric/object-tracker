from tracker.services import api
from tracker.data import state

import cv2

class Tracker(object):

  incident_reported = False

  def __init__(self):
    self.camera = cv2.VideoCapture(1)
    self.tracker = cv2.TrackerKCF_create()
    success, initial_image = self.camera.read()
    if(success):
      bbox = cv2.selectROI('Tracking', initial_image, False)
      self.tracker.init(initial_image, bbox)
    else:
      raise Exception('Tracker initialization failed.')

  def draw_box(self, image, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(image, (x,y), ((x+w), (y+h)), (0,255,0), 3, 1)
  
  def run(self):
    while True:
      success, image = self.camera.read()
      success, bbox = self.tracker.update(image)

      if(success):
        if(self.incident_reported):
          try:
            id = state.get_last_order_id()
            api.mark_order_as_completed(id)
            self.incident_reported = False
          except Exception:
            print('Cannot contact the server.')
        self.draw_box(image, bbox)
      else:
        if(not self.incident_reported):
          try:
            id = api.create_product_missing_report()
            state.set_last_order_id(id)
            self.incident_reported = True
          except Exception:
            print('Cannot contact the server.')
      
      cv2.imshow('Tracking', image)
      
      if cv2.waitKey(1) and 0xff == ord('q'):
        break