# MoonWatch
Mac OS menu/status bar app that displays the phase of the moon.

![example](https://raw.githubusercontent.com/WBrandes/MoonWatch/main/example.png "example")

</br>

### Installation

To install, simply download the repo and then run the `MoonWatch` app in the `dist` folder. Or, download just the app from that folder in the repo.

</br>

### Usage

* When running, the app will show the current phase of the moon in your menu bar.
* If you click on it, you can see the phase in text, and a dropdown option displays to Quit the app.
* To make the app run on startup, open `System Preferences` and navigate to the `Users & Groups` section. Then select `Login Items` at the top of the window, and hit the `+` icon to add the app.
* Alt-click on the icon to drag it around your menu bar.
* The app updates every 4 hours, and depends on your system's internal time. To force it to update, quit and re-open the app.

</br>

### Editing Code

If you want to edit the code yourself, it may be helpful to know that it's built on the `rumps` Python library you can find here: [rumps](https://pypi.org/project/rumps/).

Once you're done making changes, or if you just want to compile the app yourself, run:

`python3 setup.py py2app`

From the project folder in a Terminal window. This will create a `build` folder and `dist` folder, with the runnable app in the `dist` folder.
