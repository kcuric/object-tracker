from tracker.services import api

import cv2

class Tracker(object):

  incident_reported = False

  def __init__(self):
    self.camera = cv2.VideoCapture(0)
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
          self.incident_reported = False
        self.draw_box(image, bbox)
      else:
        if(not self.incident_reported):
          api.create_object_missing_report()
          self.incident_reported = True
      
      cv2.imshow('Tracking', image)
      
      if cv2.waitKey(1) and 0xff == ord('q'):
        break