# Livedown
#
# Version: 1.0.1
# Author: Hrvoje Simic <shime.ferovac@gmail.com>
# License: MIT

import sublime
import sublime_plugin
import os
import re
import subprocess

class Settings(object):
    @classmethod
    def _settings(self):
        return sublime.load_settings('Livedown.sublime-settings')

    @classmethod
    def open_arg(self):
        return '--open' if self._settings().get('open') else ''

    @classmethod
    def port_arg(self):
        return ['--port', self.port()]

    @classmethod
    def port(self):
        return str(self._settings().get('port'))

    @classmethod
    def autostart(self):
        return self._settings().get('autostart')

class Helper(object):
    @classmethod
    def is_markdown(self, view):
        if view.is_scratch() or not view.file_name:
            return False

        syntax = view.settings().get('syntax')
        return re.search(r'markdown', syntax, re.IGNORECASE)

    @classmethod
    def execute(self, args):
        subprocess.Popen(args)

    @classmethod
    def monitor_path(self):
        return os.path.join(sublime.packages_path(), "Livedown",  'monitor.py')

class LivedownPreviewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not Helper.is_markdown(self.view):
            return

        Helper.execute(['livedown', 'start', self.view.file_name(), Settings.open_arg()]
                + Settings.port_arg())

class LivedownListener(sublime_plugin.EventListener):
    def on_load(self, view):
        if Settings.autostart():
            view.run_command('livedown_preview')

        Helper.execute(['python', Helper.monitor_path(), str(os.getpid()), Settings.port()])
