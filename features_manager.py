try:
  from features.joke import tell_joke
  from features.weather import tell_weather
  from features.near_locations import tell_location
  from features.network import tell_network
  from features.videoweb import tell_videoweb
  from features.shutdown_system import tell_shutdown
  from features.search import tell_search
except Exception as e:
  from .features.joke import tell_joke
  from .features.weather import tell_weather
  from .features.near_locations import tell_location
  from .features.network import tell_network
  from .features.videoweb import tell_videoweb
  from .features.shutdown_system import tell_shutdown
  from .features.search import tell_search

features_map = {
  'joke': tell_joke,
  'weather': tell_weather,
  'locations': tell_location,
  'network': tell_network,
  'videoweb': tell_videoweb,
  'shutdown': tell_shutdown,
  'search': tell_search
}

def get_action(action_name):
  return features_map.get(action_name)