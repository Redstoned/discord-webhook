import os

def lookup(key, prefix="INPUT"):
  val = os.getenv(key, f"{prefix}_{key.upper()}")
  tested_val = val.lower()

  if tested_val == "":
    return None
  elif tested_val in ("yes", "true"):
    return True
  elif tested_val in ("no", "false"):
    return False

  try:
    return int(tested_val)
  except:
    pass

  return val
