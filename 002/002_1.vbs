i = 0
Set player = CreateObject("WMPlayer.OCX")
Set shell = Wscript.CreateObject("WScript.Shell")
player.URL = "rickroll.mp3"

While i < 1:
  WScript.Sleep 1000 * 60 * 10
  player.controls.play()
  While player.playState <> 1
    ' increase volume while mp3 is playing
    shell.sendKeys(chr(&hAF))
    WScript.Sleep 10
  Wend

  player.close()
Wend
