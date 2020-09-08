#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Fri Dec  4 15:09:22 2009

import sys

import wx
import esky
from wx.lib.softwareupdate import SoftwareUpdate

from MainWindow import MainWindow
import argparse

import config

class App(wx.App, SoftwareUpdate):
    def OnInit(self):
        # # Parse command line arguments
        parser = argparse.ArgumentParser(description='Wuggy - A Multilingual Pseudoword Generator')
        parser.add_argument('--data', help='specify a non-default data directory')
        parser.add_argument('--plugin', help='specify a non-default plugin directory')
        try:
            clargs = parser.parse_args()
            config.cl_plugin_path=vars(clargs)['plugin']
            config.cl_data_path=vars(clargs)['data']
        except:
            "Exception parsing command line arguments"
        # Check for Updates
        BASEURL = "http://crr.ugent.be"
        self.InitUpdates(updatesURL=BASEURL+"/Wuggy/downloads/", 
                         changelogURL=BASEURL+"/Wuggy/changelog.txt")
        self.SetAppDisplayName('Wuggy')
        # Initialize the application
        # wx.InitAllImageHandlers()
        mainwindow = MainWindow(None, -1, "")
        self.SetTopWindow(mainwindow)
        mainwindow.Show()
        self.CheckForUpdate()
        return 1

# end of class App

if __name__ == "__main__":
    Wuggy = App()
    Wuggy.MainLoop()
    
