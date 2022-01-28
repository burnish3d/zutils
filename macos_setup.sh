#!/bin/bash
# install homebrew, vscode, git
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew doctor

brew update

#was advised to run xcode-select --install "just in case", probably only necessary if xcode some how does not get installed

brew install --cask visual-studio-code

brew install git

