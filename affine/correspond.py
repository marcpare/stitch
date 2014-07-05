import cv2, numpy as np
import math

DEBUG = False

def extract_features(image, surfThreshold=1000, algorithm='SIFT'):
    image_gs = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    detector = cv2.FeatureDetector_create(algorithm)
    descriptor = cv2.DescriptorExtractor_create(algorithm)
    kp = detector.detect(image_gs)
    return descriptor.compute(image_gs,kp)

def find_correspondences(keypoints1, descriptors1, keypoints2, descriptors2):
    match = match_flann(descriptors1, descriptors2)
    points1 = np.array([keypoints1[i].pt for (i, j) in match], np.float32)
    points2 = np.array([keypoints2[j].pt for (i, j) in match], np.float32)
    return (points1, points2)  

def match_flann(desc1, desc2, r_threshold = 0.12):
    """ Finds strong corresponding features in the two given vectors. """
    ## Adapted from <http://stackoverflow.com/a/8311498/72470>.

    ## Build a kd-tree from the second feature vector.
    FLANN_INDEX_KDTREE = 1  # bug: flann enums are missing
    flann = cv2.flann_Index(desc2, {'algorithm': FLANN_INDEX_KDTREE, 'trees': 4})

    ## For each feature in desc1, find the two closest ones in desc2.
    (idx2, dist) = flann.knnSearch(desc1, 2, params={}) # bug: need empty {}

    ## Create a mask that indicates if the first-found item is sufficiently
    ## closer than the second-found, to check if the match is robust.
    mask = dist[:,0] / dist[:,1] < r_threshold

    ## Only return robust feature pairs.
    idx1  = np.arange(len(desc1))
    pairs = np.int32(zip(idx1, idx2[:,0]))
    return pairs[mask]
  
def draw_correspondences(image1, image2, points1, points2):
    """ Connects corresponding features in the two images with colored lines. """

    ## Put images side-by-side into 'image'.
    (h1, w1) = image1.shape[:2]
    (h2, w2) = image2.shape[:2]
    image = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
    image[:h1, :w1] = image1
    image[:h2, w1:w1+w2] = image2

    ## Draw lines connecting corresponding features.
    for (x1, y1), (x2, y2) in zip(np.int32(points1), np.int32(points2)):
     cv2.line(image, (x1, y1), (x2+w1, y2), (255, 0, 255), lineType=cv2.CV_AA)

    return image

def correspond(fn1, fn2, algorithm='SIFT'):
    image1 = cv2.imread(fn1)
    image2 = cv2.imread(fn2)
    
    ## Detect features and compute descriptors.
    (keypoints1, descriptors1) = extract_features(image1, algorithm=algorithm)
    (keypoints2, descriptors2) = extract_features(image2, algorithm=algorithm)

    if DEBUG:
        print len(keypoints1), "features detected in image1"
        print len(keypoints2), "features detected in image2"
    
    ## Find corresponding features.
    (points1, points2) = find_correspondences(keypoints1, descriptors1, keypoints2, descriptors2)
    
    if DEBUG:
        print len(points1), "features matched"
        correspondences = draw_correspondences(image1, image2, points1, points2)
        cv2.imwrite("correspondences.jpg", correspondences)
        print "Drew correspondences.jpg"
    
    return (points1, points2)
    
if __name__ == "__main__":
    print "Going to try to print a list of correspondances"
    print correspond('books/01.JPG', 'books/02.JPG')