import PySimpleGUI as sg

layout=[[
    sg.OK(),
    sg.Ok(),
    sg.Submit(),
    sg.Cancel(),
    sg.Yes(),
    sg.No(),
    sg.Exit(),
    sg.Quit(),
    sg.Open(),
    sg.Save(),
    sg.SaveAs(),
    sg.Help()
]]

sg.Window('Window Short', layout).read()