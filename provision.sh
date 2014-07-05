sudo apt-get update

sudo apt-get -y install build-essential checkinstall cmake pkg-config yasm
sudo apt-get -y install libtiff4-dev libjpeg-dev libjasper-dev
sudo apt-get -y install python-dev python-numpy

wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.0/OpenCV-2.4.0.tar.bz2
tar -xvf OpenCV-2.4.0.tar.bz2
cd OpenCV-2.4.0/
mkdir build
cd build
cmake -D WITH_QT=ON -D WITH_XINE=ON -D WITH_OPENGL=ON -D WITH_TBB=ON -D BUILD_EXAMPLES=ON ..
make
sudo make install