import os, sys

apps = {}
sys_apps = {}

current_app_class = ''

def register_apps():
    global apps, current_app_class
    sys.path.insert(0, './apps')
    file_contents = os.listdir('apps')
    for app in file_contents:
        if app.startswith('__') or 'main_class' in app:
            continue
        app_name = app.split('.')[0]
        app_address = str(app_name)
        exec(f'import {app_address}')
        exec(f'global current_app_class; current_app_class = {app_name}.app')
        apps[current_app_class.local_name] = current_app_class
    return apps

def register_sys_apps():
    global sys_apps, current_app_class
    sys.path.insert(0, './sys_apps')
    file_contents = os.listdir('sys_apps')
    for app in file_contents:
        if app.startswith('__') or 'main_class' in app:
            continue
        app_name = app.split('.')[0]
        app_address = str(app_name)
        exec(f'import {app_address}')
        exec(f'global current_app_class; current_app_class = {app_name}.app')
        sys_apps[current_app_class.local_name] = current_app_class
    return sys_apps