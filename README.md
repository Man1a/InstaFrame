InstaFrame
==========

InstaFrame is a Python micro program to add a border to landscape and portrait images in order to make them square-shaped without croping them.

Yes it does batch process a whole directory.

### Launch it

in a terminal, go to the directory that contains InstaFrame.py, and then:
```
./InstaFrame.py -input /yourFoderFullOfImages/
```

I guess you can just whrite
```
./InstaFrame.py -input
```
and then drop a folder from GUI to terminal if you don't want to bother typing the whole address.


By default, the border color is white, but you can change it (here, red)
```
./InstaFrame.py -input /yourFoderFullOfImages/ -color FF0000
```

Then it creates a subdirectory __InstaFramed__ (so /yourFoderFullOfImages/InstaFramed/) containing all the framed images with their real names.

### Dependencies
PIL (Python Image Library) or its fork [Pillow](http://pillow.readthedocs.org/en/latest/installation.html)


### Licence

GPL, read Licence.txt for more info.

Bye.
