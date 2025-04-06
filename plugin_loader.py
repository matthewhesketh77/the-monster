import os
import importlib.util

PLUGIN_DIR = "plugins"

def list_plugins():
    return [f.replace(".py", "") for f in os.listdir(PLUGIN_DIR) if f.endswith(".py")]

def load_plugin(plugin_name):
    try:
        plugin_path = os.path.join(PLUGIN_DIR, f"{plugin_name}.py")
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error loading plugin {plugin_name}: {e}")
        return None

def run_plugin(plugin_name, **kwargs):
    plugin = load_plugin(plugin_name)
    if plugin and hasattr(plugin, "run"):
        return plugin.run(**kwargs)
    return f"Plugin {plugin_name} failed or has no run() function"

