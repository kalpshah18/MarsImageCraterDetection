# Detecting Craters on Mars using Computer Vision
Kalp Shah
Advisor: Prof. Shanmuganathan Raman
EE299 Project Course

## About
This Repository Implements a Edge Detection Paper^[1]  for detecting Craters on Lunar Surfaces but we use Mars Surface Images instead by converting images to grayscale and normalization.

## Pipeline
The paper defines a **two–stage system**:

1.  **Crater Detection**
    
    -   Multi-scale adaptive Gaussian filtering
        
    -   Adaptive Canny edge detection using Gradient Magnitude Histogram
        
    -   Edge selection using lighting direction
        
    -   Edge pairing (light–shadow rim pairing)
        
    -   Ellipse fitting (Direct Least Squares)
        
2.  **Crater Matching**
    
    -   Conic-pair affine invariants
        
    -   Voting matrix matching
        
    -   Area-ratio correction for false matches

## Citations

[1] J. He, H. Cui, and J. Feng, “Edge information based crater detection and matching for lunar exploration,” in Proc. International Conference on Intelligent Control and Information Processing, Dalian, China, Aug. 13–15, 2010, pp. 302–307