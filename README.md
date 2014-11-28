# Livedown

A Sublime plugin for [Livedown](https://github.com/shime/livedown).

![](https://raw.githubusercontent.com/shime/livedown-demos/master/sublime.gif)

## Installation

* Make sure you have [node](http://nodejs.org/) with [npm](https://www.npmjs.org/) installed. 
* ``` npm install -g livedown```
* Open your Sublime Text and click on `Preferences > Browse Packages`.
* Go to the parent folder and find `Installed Packages` directory in it.
* Download [the zipped package](https://raw.githubusercontent.com/shime/sublime-livedown/master/build/Livedown.sublime-package) and place it in that directory.
* Restart Sublime Text.

You will now have `Livedown: Preview` command available from your command pallete (`Ctrl+Shift+P`).

For bonus points, map it to the keyboard shortcut like `Alt+m` by going to 
`Preferences > Key Bindings - User` and adding

    { "keys": ["alt+m"], "command": "livedown_preview"}

## Configuration

There are several configuration options available. You can check them by opening your Sublime Editor and going to `Preferences > Package Settings > Livedown > Settings`.

## License

MIT
