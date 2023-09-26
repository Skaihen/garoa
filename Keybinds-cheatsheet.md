
Tip: You can open any file by its name when you type Ctrl+P (Quick Open).

The Explorer is great for navigating between files when you are exploring a project. However, when you are working on a task, you will find yourself quickly jumping between the same set of files. VS Code provides two powerful commands to navigate in and across files with easy-to-use key bindings.

Hold Ctrl and press Tab to view a list of all files open in an editor group. To open one of these files, use Tab again to pick the file you want to navigate to, then release Ctrl to open it.

Quick Navigation

Alternatively, you can use Alt+Left and Alt+Right to navigate between files and edit locations. If you are jumping around between different lines of the same file, these shortcuts allow you to navigate between those locations easily.



To interact with breadcrumbs, use the Focus Breadcrumbs command or press Ctrl+Shift+.. It will select that last element and open a dropdown that allows you to navigate to a sibling file or symbol. Use the Left and Right keyboard shortcuts to go to elements before or after the current element. When the dropdown appears, start typing - all matching elements will be highlighted and the best match will be selected for quick navigation.

You can also interact with breadcrumbs without the dropdown. Press Ctrl+Shift+; to focus the last element, use Left and Right to navigate, and use Space to reveal the element in the editor.

Go to Definition
If a language supports it, you can go to the definition of a symbol by pressing F12.

If you press Ctrl and hover over a symbol, a preview of the declaration will appear:

Ctrl Hover

Tip: You can jump to the definition with Ctrl+Click or open the definition to the side with Ctrl+Alt+Click.


Go to Implementation
Languages can also support jumping to the implementation of a symbol by pressing Ctrl+F12. For an interface, this shows all the implementors of that interface and for abstract methods, this shows all concrete implementations of that method.

Go to Symbol
You can navigate symbols inside a file with Ctrl+Shift+O. By typing : the symbols will be grouped by category. Press Up or Down and navigate to the place you want.

Go to Symbol

Open symbol by name
Some languages support jumping to a symbol across files with Ctrl+T. Type the first letter of a type you want to navigate to, regardless of which file contains it, and press Enter.

Open symbol by name

Peek
We think there's nothing worse than a big context switch when all you want is to quickly check something. That's why we support peeked editors. When you execute a Go to References search (via Shift+F12), or a Peek Definition (via Alt+F12), we embed the result inline:

Peek References

You can navigate between different references in the peeked editor and make quick edits right there. Clicking on the peeked editor filename or double-clicking in the result list will open the reference in the outer editor.

Tip: Additionally, the peek window is closed if you press Escape or double-click in the peek editor region. You can disable this behavior with the editor.stablePeek setting.

Bracket matching
Matching brackets will be highlighted as soon as the cursor is near one of them.

Bracket Matching

Tip: You can jump to the matching bracket with Ctrl+Shift+\



Errors & warnings
Warnings or Errors can be generated either via configured tasks, by rich language services, or by linters, that constantly analyze your code in the background. Since we love bug-free code, warnings and errors show up in multiple places:

In the Status Bar, there is a summary of all errors and warnings counts.
You can click on the summary or press Ctrl+Shift+M to display the PROBLEMS panel with a list of all current errors.
If you open a file that has errors or warnings, they will be rendered inline with the text and in the overview ruler.
errors in problems panel

Tip: To loop through errors or warnings in the current file, you can press F8 or Shift+F8 which will show an inline zone detailing the problem and possible Code Actions (if available):



Tip: A Secondary Side Bar is also available to display views opposite the Primary Side Bar. You can show it with Ctrl+Alt+B.

Tip: Type Ctrl+P (Quick Open) to quickly search and open a file by its name.

You can filter the currently visible files in the File Explorer. With the focus on the File Explorer, press Ctrl/Cmd+F to open the tree Find control and type part of the file name you want to match. You will see a Find control in the top-right of the File Explorer showing what you have typed and matching file names will be highlighted. Pressing the Filter button will toggle between the two modes: highlighting and filtering. Pressing DownArrow will let you focus the first matched element and jump between matching elements.


ctrl+h toggle replace


Side by side editing
You can open as many editors as you like side by side vertically and horizontally. If you already have one editor open, there are multiple ways of opening another editor to the side of the existing one:

Alt click on a file in the Explorer.
Ctrl+\ to split the active editor into two.
Open to the Side (Ctrl+Enter) from the Explorer context menu on a file.
Click the Split Editor button in the upper right of an editor.
Drag and drop a file to any side of the editor region.
Ctrl+Enter (macOS: Cmd+Enter) in the Quick Open (Ctrl+P) file list.



Command Palette
VS Code is equally accessible from the keyboard. The most important key combination to know is Ctrl+Shift+P, which brings up the Command Palette. From here, you have access to all of the functionality of VS Code, including keyboard shortcuts for the most common operations.


The Command Palette provides access to many commands. You can execute editor commands, open files, search for symbols, and see a quick outline of a file, all using the same interactive window. Here are a few tips:

Ctrl+P will let you navigate to any file or symbol by typing its name
Ctrl+Tab will cycle you through the last set of files opened
Ctrl+Shift+P will bring you directly to the editor commands
Ctrl+Shift+O will let you navigate to a specific symbol in a file
Ctrl+G will let you navigate to a specific line in a file

Type ? into the input field to get a list of available commands you can execute from here:


You can hide the Menu Bar on Windows and Linux by changing the setting window.menuBarVisibility from classic to toggle. A setting of toggle means that a single press of the Alt key will show the Menu Bar again.


Open a folder.
File > Open Folder (Ctrl+K Ctrl+O)
Use File Explorer to view the folder's files and subfolders.
View > Explorer (Ctrl+Shift+E)
Install the Node.js runtime to execute JavaScript code.
Find Node.js for your platform at https://nodejs.org
Check your Node.js installation.
From a terminal or command prompt, type node --version
Create new file.
File > New File (Ctrl+N)
Create a simple "Hello world" console application called app.js.
IntelliSense provides suggestions as you type.
Automatically format the source code.
Format Document command (Shift+Alt+F)
Turn on Auto Save.
File > Auto Save
Display the Integrated Terminal.
View > Terminal (Ctrl+`)
Split the terminal.
Split Terminal (Ctrl+Shift+5)
Create new terminal.
Create New Terminal (Ctrl+Shift+`)
Run the application.
From the Integrated Terminal, type node app.js



Settings
Most editor configurations are kept in settings which can be modified directly. You can set options globally through user settings or per project/folder through workspace settings. Settings values are kept in a settings.json file.

Select File > Preferences > Settings (or press Ctrl+,) to edit the user settings.json file.
To edit workspace settings, select the WORKSPACE SETTINGS tab to edit the workspace settings.json file.

Zen Mode
Zen Mode lets you focus on your code by hiding all UI except the editor (no Activity Bar, Status Bar, Side Bar and Panel), going to full screen and centering the editor layout. Zen mode can be toggled using View menu, Command Palette or by the shortcut Ctrl+K Z. Double Esc exits Zen Mode. The






Keyboard shortcuts
Here are some handy keyboard shortcuts to quickly navigate between editors and editor groups.

If you'd like to modify the default keyboard shortcuts, see Key Bindings for details.

Ctrl+PageDown go to the right editor.
Ctrl+PageUp go to the left editor.
Ctrl+Tab open the previous editor in the editor group MRU list.
Ctrl+1 go to the leftmost editor group.
Ctrl+2 go to the center editor group.
Ctrl+3 go to the rightmost editor group.
Ctrl+W close the active editor.
Ctrl+K W close all editors in the editor group.
Ctrl+K Ctrl+W close all editors.


Ctrl+Tab to navigate in entire editor history
You can change keybindings for Ctrl+Tab to show you a list of all opened editors from the history independent from the active editor group.






-----------------------------------------------------------------------------------------------------------------------------------------------




First of all, Metago is a tool made for myself, it comes from the voice in my heart💖as a programmer. Metago tries its best to be the coolest😎 keyboard(mouseless) focused navigation tool in vscode. Metago tries to make your keyboard⌨ to you as meaningful as a kitchen knife to a master chef👩‍🍳.


Metago as a free tool, currently is maintained and developed by me in my spare time🌙⏳, if you think has ever saved you time, boosted your efficiency, or even indispensable like some of our users, please support me 😊
Give me a github⭐, or even sponsor me at github🍻

quotes from users:

Wicked fast cursor movement/selection for a focus on keyboard usage. This changed how I use VS Code forever. Seriously.

This boosts my performance so much since It’s a trouble for me to use VIM (I’m leftie :( )

probably the best tool for keyboard driven navigation bar none (better than vim), includes bookmarks

MetaGo is a way to move your cursor to a position quickly and without using your mouse/trackpad.

Oh, man.. I have a feeling that after that I'm going to feel crippled without it. This is fantastic.

This takes a bit to get used to but so much worth it! I really think this should be mainstream and every modern editor should support this.

and MORE from you...

Features Summary
MetaGo provides fast cursor movement/selection/delete for keyboard focused users:

MetaJump

features highlight
go to any character on screen with 3(most cases) or 4 times key press
select to any character in the active editor
add multiple cursors to the active editor
change active selection in multiple selections
delete to any character
MetaSelection

lines selection
alternate Selection's active with anchor
surrounding-pair selection
surrounding-pair selection of common tag
surrounding-pair selection of html tag
surrounding-pair changing demo
Navigate between files using bookmarks

MetaWord

Other features

scroll the active line to the screen top, middle and bottom
moving/select up/down between blank lines
jump to bracket
metaJump
metaJump is one part of the tool set MetaGo, with the goal to do cursor moving/selecting/deleting by showing decorators on possible target-locations. (detail document of MetaJump) MetaGo.MetaJump

metaSelection
lines selection
vsCode's default select current line command(Ctrl+l) selects current line and puts the cursor at the next line's start position. we create our own to extend/shrink the selection of the current line:

Ctrl+l to select current line if no selection at cursor, or extend/shrink selections by one line below if there is selection before/after the cursor.
Ctrl+o to extend/shrink selection by one line above if there is selection after/before the cursor.
extend/shrink selections work at the selection's active end(where cursor flashing), if you want to extend/shrink at the selection's anchor end, use Alt+a to alternate selection's anchor with active at first.

note: Ctrl+o triggers open file by default, and it triggers extend line selection above only when there is selection in active editor.

if you want to select line up, you should press Ctrl+l to select current line and then press Ctrl+o to extend line selection above.

by default selectLineUp command is configured as:

{
    "command": "metaGo.selectLineUp",
    "key": "ctrl+o",
    "when": "editorTextFocus && editorHasSelection"
}

you could assign a shortcut key not collision with default vscode ones, just remove the editorHasSelection condition, so it works even with no selection in editor.

alternate Selection's active with anchor
Alt+a to alternate the selection's active(cursor flashing) with the anchor.
➭Feature Summary⮵

lineSelection demo
we use ctrl+l to select current line, then ctrl+l again to extend current selection below, then ctrl+o to shrink current selection above, then alt+a to alternate the current selection's active end with anchor end, then ctrl+o to extend current selection above, then ctrl+alt+/ to add another cursor, and ctrl+l to select current line, ctrl+l again to extend selection below, then alt+a to alternate selection's active with anchor, then ctrl+o to extend selection above.

With the two selections, you could then delete or copy... MetaGo.LineSelection

➭Feature Summary⮵

surrounding-pair selection
commands to select content inside a pair of separators: '(',')'; '[',']'; '{','}';'<','>'; '>', '<'; or any char pair: ''', '"'... html tag pair is supported via regexp. (i.e. to select content between two html tag pairs: alt+shift+p t, t means tag).

Alt+p to chang surrounding pairs.
Alt+Shift+p to select content between surrounding pairs.
Alt+Ctrl+p to select both the content and the pairs.
Alt+Shift+p: I want to select content between a pair of chars.
type the start character of the pair. i.e. '(', '[', '{', '"'... or the specific regex key(i.e. 't' for html/xml tag)
Note: Alt+Ctrl+p to selection both the content and the pair of separators.

it supports multiple cursors/selections

➭Feature Summary⮵

surroundPairs config
below is the default surrounding-pairs config, it support regex:

"metaGo.surroundPairs": {
    "type": "object",
    "default":[["{","}"],["(",")"],["[","]"],["<",">"],["/<(?!/)(?!!)(?!br[\\s>])(?!area[\\s>])(?!base[\\s>])(?!col[\\s>])(?!command[\\s>])(?!embed[\\s>])(?!hr[\\s>])(?!img[\\s>])(?!input[\\s>])(?!keygen[\\s>])(?!link[\\s>])(?!meta[\\s>])(?!param[\\s>])(?!source[\\s>])(?!track[\\s>])(?!wbr[\\s>])((?:.(?!/>))+?)(?<!/)>/ms", "/<\/(.+?)>/", "t"]]
},

the last one is and regex, it is used for html tag: this array has 3 items: start html tag regex, end html tag regex, trigger key. the default trigger key is the start pair, if start pair is only one char. regex is the content inside '/' and '/', is defined by javascript regex grammar you could config your own regex pairs the regex pairs support all regex flags, which means it support multiline tag.

html elements is defined in https://www.w3.org/TR/2011/WD-html-markup-20110405/syntax.html#syntax-elements

➭Feature Summary⮵

surrounding-pair-selection demo
we use alt+shift+p ( to select content inside the '(' and ')', then alt+shift+p { to extend selection, then alt+shift+p { to extend further, then alt+ctrl+p { to include then pair('{'and '}') in the selection, then alt+ctrl+p to extend the selection further with the pair('{' and '}') included.

metago.surrounding-pair-selection

note: the hotkey in gif has been changed

➭Feature Summary⮵

surrounding-pair-selection demo: html tag pairs
we use alt+shift+p t to select content inside html tag, alt+ctrl+p to select both the content and the tag pairs. if the cursor is in the start or end tag, alt+shift+p t would select both the tag and the content.

metago.surrounding-pair-selection-html-tag

note: hotkeys in gif have been changed

➭Feature Summary⮵

surrounding-pair changing demo
in this demo, we alt+p ' " to change a pair of ' to ", and then goto another place use alt+p [ ( to change a pair to '[]' to '()'. Then we switch to another html file, where we alt+p t to change a surrounding pair of 'h1' to 'h2', and go to another place, to use alt+p t to change another pair of tag from 'h3' to 'h1', note: here is a multi-line start-tag, we use alt+shift+// to shrink the selection first and then modify the pair of tag.



➭Feature Summary⮵

navigate between files using bookmarks
Alt+ ' to toggle a bookmark at the cursor location.
Alt+ [ goto previous bookmark.
Alt+ ] goto next bookmark.
Alt+\ to list the bookmarks with management menu:
press cc then enter to clear all the bookmarks
press c then enter to clear all the bookmarks in current document.
press n then enter to go to the next bookmark.
press p then enter to go to the previous bookmark.
MetaGo.Center

➭Feature Summary⮵

Other features
scroll the active line to the screen top, middle and bottom
Alt+t is the default shortcut to scroll current line to screen top.
Alt+m is the default shortcut to scroll current line to screen middle.
Alt+b is the default shortcut to scroll current line to screen bottom.
MetaGo.Center

move/select up/down between blank lines
Alt+Home to move cursor to the blank line above.
Alt+End to move cursor to the blank line below.
Alt+Shift+Home to select from the cursor to the blank line above.
Alt+Shift+End to select from the cursor to the blank line below. MetaGo.blankLine
➭Feature Summary⮵

jump to bracket
default command always put cursor before the bracket, we want it after start bracket and before end bracket.

default command always search down for the end bracket if the cursor is not at bracket, we want it search up.

ctrl+shift+\: jump to the begin bracket that contains the cursor. Press the shortcut again jump to the end bracket.
➭Feature Summary⮵

to invoke command from command panel
it's very easy to trigger metago command: type F1, xx.... xx` is a prefix for search metago commands

➭Feature Summary⮵

Other resources that help you understand MetaGo
Use MetaGo to Quickly Move Around Your Code in VS Code

➭Feature Summary⮵

Default Shortcut Settings
To configure the keybinding, press ctrl+k ctrl+s, or via menu: File -> Preferences -> Keyboard Shortcuts:

default shortcuts refer: keybindings section in package.json

➭Feature Summary⮵

Extension Settings
To modify the settings, press ctrl+,, and search metago...

default setting refer: configuration section in package.json

➭Feature Summary⮵

Credits
Contributors:
Thank you to all the people who have already contributed to MetaGo!🤞

➭Feature Summary⮵

Notes
if you like this tool, and using Windows, you may also be interested in my other tool: metaTool. (release soon) 😉 with metaTool running with it's metaKeyboard plugin, you just using the 61 keys main keyboard area to type any key you want.

i.e. to jump next blank line in the document, currently the default trigger is Alt+End, now you could useLAlt+;, because LAlt+; is expanded to Alt+end


Hacer keymap tocho
con cheatsheet