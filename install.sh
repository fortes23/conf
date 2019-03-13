#!/bin/bash

DIR_REL=$(dirname $0)
DIR=$(readlink -f $DIR_REL)

if [ -f ~/.gitconfig ] || [ -f ~/.subversion/config ] || [ -f ~/.vimrc ]; then
	while [ "$ANSWER" != "y" ] && [ "$ANSWER" != "n" ]
	do
		echo -n "File ~/.gitconfig or ~/.subversion/config or ~/.vimrc already exist, do you want to remove it?(y/n)"
		read -n 1 ANSWER
	done
	if [ "$ANSWER" != "y" ]; then
		exit 1
	fi
fi

ln -sf $DIR/git/gitconfig ~/.gitconfig
ln -sf $DIR/svn/svnconfig ~/.subversion/config
ln -sf $DIR/vim/vimrc ~/.vimrc
