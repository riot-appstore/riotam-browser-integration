# Browser integration for RAPstore

## Requirements
1. **sudo apt-get install git python make openocd**
2. navigate with a terminal in to the directory where you want the extension to be stored at \*, then run:
   <br>**git clone https://github.com/riot-appstore/rapstore-browser-integration**

**IMPORTANT:** Don't remove this directory while using the extension, otherwise it won't work anymore

\* Notice: the path must not contain spaces

## Install

### Complete (extension and native messaging host)
1. run **python install.py <your_browser>** from the cloned repo's src/ directory
2. for further information look at the instructions below

### Install the extension

#### Google Chrome and Chromium
1. open a terminal
2. run **python install.py --component extension <your_browser>** from the cloned repo's src/ directory
3. you need to restart chrome/ chromium
4. extension should be installed now

#### Firefox
1. open a terminal
2. run **python install.py --component extension firefox** from the cloned repo's src/ directory
3. Firefox will open and ask for a confirmation
4. click on **Add**

### Install the Native Messaging Host
1. open a terminal
2. run **python install.py --component host <your_browser>** from the cloned repo's src/ directory

## More Information
Please ignore upcoming warnings, they are caused by a shared codebase for firefox and chrome

Graphics are editable with [yEd](http://www.yworks.com/products/yed "http://www.yworks.com/products/yed")

## LICENSE
* The project is licensed under the GNU Lesser General Public License
  (LGPL) version 2.1 as published by the Free Software Foundation.

All code files contain licensing information.
