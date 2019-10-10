def is_degenerated(coorditantes):
  if coorditantes[0]==coorditantes[1]:
    return True
  return False

def is_vertical(coorditantes):
  if coorditantes[0][0]==coorditantes[1][0]:
    return True
  return False

def is_horizontal(coorditantes):
  if coorditantes[0][1]==coorditantes[1][1]:
    return True
  return False

def is_inclined(coorditantes):
  if coorditantes[0][1]!=coorditantes[1][1] and coorditantes[0][0]==coorditantes[1][0]:
    return True
  return False

def type_of_line(coordinates):
  if is_degenerated(coordinates):
    return "Point"
  if is_vertical(coordinates):
    return "Vertical"
  if is_horizontal(coordinates):
    return "Horizontal"
  if is_inclined(coordinates):
    return "Inclined"
