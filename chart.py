def plot(levels):
  from quickchart import QuickChart
  dates = []
  for i in range(len(levels)):
    dates.append(i+1)
  
  qc = QuickChart()
  qc.width = 500
  qc.height = 300
  qc.device_pixel_ratio = 2.0
  qc.config = {
      "type": "line",
      "data": {
          "labels": dates,
          "datasets": [{
              "label": "Mood Levels",
              "data": levels
          }]
      }
  }
  return qc.get_url()
