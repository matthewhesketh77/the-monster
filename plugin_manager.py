import os
import importlib.util

def register_plugins():
    plugins = []
    plugin_folder = 'plugins'

    for plugin_file in os.listdir(plugin_folder):
        if plugin_file.endswith(".py"):
            plugin_path = os.path.join(plugin_folder, plugin_file)
            module_name = plugin_file[:-3]  # Remove .py extension
            spec = importlib.util.spec_from_file_location(module_name, plugin_path)
            plugin = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin)
            plugins.append(plugin)
            print(f"Registered plugin: {module_name}")

    return plugins

def run_plugins(plugins):
    for plugin in plugins:
        if hasattr(plugin, 'run_plugin'):
            print(f"Running plugin: {plugin.__name__}")
            plugin.run_plugin()
        else:
            print(f"⚠️  Plugin {plugin.__name__} does not have a run_plugin function.")

