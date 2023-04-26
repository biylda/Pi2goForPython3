if [ ! -d ~/pi2go2 ]; then
  mkdir ~/pi2go2
fi
if [ ! -d ~/.config/autostart ]; then
  mkdir ~/.config/autostart
fi
# cd ~/.config/autostart
echo Creating IP Display autostart
cp ipd.desktop ~/.config/autostart
# cd ~/pi2go2
cp ipd03.py ~/pi2go2
echo Copying Pi2Go Library Module
cp pi2go2.py ~/pi2go2
echo Copying Test Files
cp adc.py ~/pi2go2
cp sonarTest.py ~/pi2go2
cp avoider.py ~/pi2go2
cp ledTest.py ~/pi2go2
cp motorTest.py ~/pi2go2
cp stepTest.py ~/pi2go2
cp lineTest.py ~/pi2go2
cp lineFollower.py ~/pi2go2
cp rainbow.py ~/pi2go2

echo Pi2Go Mk2 Files Copied to ~/pi2go2



