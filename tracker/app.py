from tracker.tracker.tracker import Tracker

def run():
  try:
    tracker = Tracker()
    tracker.run()
  except Exception as ex:
    print(ex)
  
