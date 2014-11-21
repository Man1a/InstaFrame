InstaFrame
==========

InstaFrame is a Python micro program to add a border to landscape and portrait images in order to make them square-shaped without croping them.

Yes it does batch process a whole directory.

### Launch it

in a terminal, go to the directory that contains InstaFrame.py, and then:
```
./InstaFrame.py -input /yourFoderFullOfImages/
```

I guess you can just write
```
./InstaFrame.py -input
```
and then drop a folder from GUI to terminal if you don't want to bother typing the whole address.


By default, the border color is white, but you can change it (here, red):
```
./InstaFrame.py -input /yourFoderFullOfImages/ -color FF0000
```

And by default, the output size is the biggest (width or height) of each image, but you can tune it (here 1000):
```
./InstaFrame.py -input /yourFoderFullOfImages/ -size 1000
```

Note: the jpeg quality of output images is hard coded at 90%. It seemed pretty useless to make an parameter for that.

Then it creates a subdirectory __InstaFramed__ (so /yourFoderFullOfImages/InstaFramed/) containing all the framed images with their real names.

### Dependencies
PIL (Python Image Library) or its fork [Pillow](http://pillow.readthedocs.org/en/latest/installation.html)


### Licence

GPL, read Licence.txt for more info.

Bye.
