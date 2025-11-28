# Welcome to Pythonista

Thank you for downloading Pythonista! You now have everything you need to build and run Python scripts directly on your iPhone or iPad.

To give you an idea of what you can do with the app, various sample scripts are included in the [Examples][examples] folder (just tap the link to open it). Feel free to use them as starting points for your own experiments. To share your creations, get help with coding problems, or just to meet fellow Pythonistas, please visit our [community forum][forum]

## Getting Started + Tips

If you're new to Pythonista, here are some tips to help you get up and running:

* To create a **new script**, first tap `≡` to reveal the library, then `+` (at the bottom). You can also use left and right swipe gestures to switch between the file browser, editor, and console panels.

* The editor supports multiple **tabs** – tap the button in the top-righthand corner to add a new one. You can also create new files from an empty tab.

* The **settings** ("gear" button in the file browser) contain useful options to customize the editor font, color theme, indentation type (tabs/spaces), and much more.

* Swipe left to show the **console** (REPL) panel. This is where text output appears, and you can use the prompt at the bottom to evaluate individual lines of Python code directly.

* You'll also find the included **documentation** in the console panel; simply tap the `(?)` button to open it in a separate tab. Reference documentation is also available while you're editing code -- simply select a word (e.g. a function name), and choose *Help…* from the menu.

* For easier navigation in long scripts, tap the file name at the top to show an **outline**/list of classes and functions. This is also where you can **rename** the current file.

* If you have a hardware (e.g. Bluetooth) keyboard attached to your iPad or iPhone, you can navigate almost all of Pythonista using **keyboard shortcuts**. Press and hold the Cmd (⌘) key to show keyboard shortcuts that are currently available.

* The **"wrench" menu** contains various options for checking your coding style and formatting your scripts. You can also pass arguments (`sys.argv`) to a script, using the "Run Options" menu, and you can add your own script shortcuts to this menu to extend Pythonista's functionality. (Have a look at the `editor` module if you're interested in automating Pythonista itself.)

* A lot of keys on Pythonista's extra keyboard row have multiple mappings. For example, you can tap and hold the tab key to get an unindent option.

* Tap with two fingers in the editor to select an entire line of code.

* The "**Shortcuts**" option in the "wrench" menu allows you to integrate Pythonista scripts with various parts of iOS, like the share sheet, the on-screen keyboard, and apps that support opening custom URL schemes. You can also generate QR codes from script URLs there.

* Swipe right on a file in the script library for more options, e.g. to open files in new tabs. Swipe left to delete files.

*If you enjoy coding in Pythonista, please consider leaving a rating or [review in the App Store][review]. Thank you!*
💚

## What's New in 3.3

For full release notes, and to see what was added in previous releases, please refer to the "What's New in Pythonista" page in the documentation. You can also open the release notes from an empty tab.

* Support for dark mode on iOS 13 – you can now select separate themes for light/dark mode, and Pythonista will switch automatically between them. Switching between themes is also a bit faster now.

* New *PyKeys* custom keyboard for running scripts in any app with text input. Have a look at the examples in the [Keyboard][kb_examples] folder for some ideas and more information.

* Significantly improved support for external keyboards (more shortcuts, arrow-key navigation almost everywhere).

* The outline (list of functions) in the editor can now be filtered -- just start typing if the keyboard is already active, or drag down the list to reveal the filter text field. The filter supports fuzzy matching.

* Unified UI for creating script shortcuts in various places of iOS ("Shortcuts" option in the "wrench" menu).

* New URL generator for improved inter-app automation (you can also use this with the Shortcuts app, but full Shortcuts support will come later).

* Support for opening external folders using the system's file picker.

* Revamped `notifications` module with custom action buttons, support for attachments and location triggers, and more – see the new [Quiz.py][quiz] for an example of what you can do with this. The module also works in the share sheet extension now.

* New "on device" option for speech recognition in the `speech` module.

* New `location.render_map_snapshot()` function to generate an image from a location (see new [Satellite Image][satellite] example).

* Console history is now persistent (you can clear it by tapping and holding the `^` button).

* Added a couple of new sample scripts (see [Examples/Overview.md][overview.md]).

* Various bugfixes for iOS 13 and new screen sizes.

[overview.md]: pythonista3://Examples/Overview.md?action=open
[kb_examples]: pythonista3://Examples/Keyboard/?action=open
[quiz]: pythonista3://Examples/Misc/Quiz.py?action=open
[satellite]: pythonista3://Examples/Misc/Satellite%20Image.py?action=open

## Feedback

I hope you enjoy coding in Pythonista. If you have any feedback, please send an email to <pythonista@omz-software.com>, or visit the [community forum][forum] to share code and get help with your programming questions. You can also find me on Twitter:[@olemoritz][twitter].

---

[forum]: https://forum.omz-software.com
[twitter]: http://twitter.com/olemoritz
[review]: itms-apps://itunes.apple.com/app/id1085978097?action=write-review
[examples]: pythonista3://Examples/?action=open
