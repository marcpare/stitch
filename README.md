
Installation
===

Install [Vagrant](http://www.vagrantup.com/downloads)

Then, from the project directory, login to your box:

    vagrant up
    vagrant ssh

`setup.sh` downloads and installs OpenCV:

    cd /vagrant
    chmod +x setup.sh
    ./setup.sh

This takes a while.

Usage
===

To run the [Crichardt panorama stitching](http://richardt.name/teaching/supervisions/vision-2011/practical/) code:

    cd crichardt
    python stitch.py Image1.jpg Image2.jpg

This outputs `correspondences.jpg`, `panorama.jpg`


---

Results:

So many applications of image stitching!

* aligning observations of the sun's position
* brain scan images
* high resolution bio slides
* drones flying over terrain
* panorama photos of landscapes or architecture

And subsequently, quite a variety of techniques.

- Phase correlation with fft
- SIFT, feature detection, homography

Observations

* Got 3 panorama's stitched together
* Walking along the bookshelf confused the algorithm
* autostitch worked great

So many libraries! Didn't play with any (yet)

Cool bugs.

Filled out this exercise:
http://richardt.name/teaching/supervisions/vision-2011/practical/

Wow, as you go, the variety keeps increasing.

* Stitching a panorama from 1 spot, only rotation
* Stitching a panorama moving linearly (trickier, in fact, needs lots of overlap b/c of parallax)
* Stitching a bunch of papers scanned by a scanner (or a microscope...)

A very interesting point: why is it so hard to stitch together the bookcase? Why does moving change everything? (Perspective is everything.)

Think about parallax: an object closer will show more perspective change after translation than an object farther away. Think of two picture, one of an object close, one of an object far. Or, two objects in the same picture, one near and one far. What kind of affine transformation would work for both images? It's not possible; you have to know something about the geometry of the subject.
  
  http://en.wikipedia.org/wiki/Parallax
  
  In a philosophic/geometric sense: An apparent change in the direction of an object, caused by a change in observational position that provides a new line of sight. The apparent displacement, or difference of position, of an object, as seen from two different stations, or points of view. In contemporary writing parallax can also be the same story, or a similar story from approximately the same time line, from one book told from a different perspective in another book. The word and concept feature prominently in James Joyce's 1922 novel, Ulysses. Orson Scott Card also used the term when referring to Ender's Shadow as compared to Ender's Game.

  The metaphor is invoked by Slovenian philosopher Slavoj Žižek in his work The Parallax View. Žižek borrowed the concept of "parallax view" from the Japanese philosopher and literary critic Kojin Karatani. "The philosophical twist to be added (to parallax), of course, is that the observed distance is not simply subjective, since the same object that exists 'out there' is seen from two different stances, or points of view. It is rather that, as Hegel would have put it, subject and object are inherently mediated so that an 'epistemological' shift in the subject's point of view always reflects an ontological shift in the object itself. Or—to put it in Lacanese—the subject's gaze is always-already inscribed into the perceived object itself, in the guise of its 'blind spot,' that which is 'in the object more than object itself', the point from which the object itself returns the gaze. Sure the picture is in my eye, but I am also in the picture."[35]

---

Simplify: align using corresponding features without perspective warp

Show the correspondences bookshelf image


---

sudo apt-get update
sudo apt-get install libopencv-dev
sudo apt-get -y install python-dev python-numpy

trying this...
http://karytech.blogspot.in/2012/05/opencv-24-on-ubuntu-1204.html

This worked, got `import cv2` to work in Python

now...

sudo apt-get install scipy

sudo apt-get install fabric

---

next: do this: 
http://richardt.name/teaching/supervisions/vision-2011/practical/

---

What about scripting Hugin from the command line?
http://wiki.panotools.org/Panorama_scripting_in_a_nutshell#Creating_hugin_projects_on_the_command-line

---

Another OpenCV install, this time to build the examples:

http://mitchtech.net/raspberry-pi-opencv/

---

How to get stitching for work with translation:

./stitching_detailed /vagrant/books/*.JPG --conf_thresh 0.8
./stitching_detailed /vagrant/books/*.JPG --conf_thresh 0.3

---

Panoramas of streets: the pros do it by hand in photoshop. They take lots of overlap in their images. The thought: "1 picture per column of pixels" !!

---

http://wiki.panotools.org/Stitching_a_photo-mosaic

  A photo-mosaic is an image that is stitched together by photographs all taken from different viewpoints. This differs from the panorama where all images are taken from one single viewpoint but with different angles.



