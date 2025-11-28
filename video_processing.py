
import cv2
import numpy as np

def apply_distortion(frame, distortion_type, intensity):
    if distortion_type == "temporal":
        return temporal_distortion(frame, intensity)
    elif distortion_type == "spatial":
        return spatial_distortion(frame, intensity)
    elif distortion_type == "glitch":
        return glitch_distortion(frame, intensity)
    else:
        raise ValueError("Unknown distortion type")

def temporal_distortion(frame, intensity):
    alpha = np.clip(intensity, 0.1, 3.0)
    return cv2.addWeighted(frame, alpha, frame, 0, 0)

def spatial_distortion(frame, intensity):
    h, w, _ = frame.shape
    distorted = cv2.resize(frame, (int(w * intensity), h))
    return cv2.resize(distorted, (w, h))

def glitch_distortion(frame, intensity):
    frame_copy = frame.copy()
    for _ in range(int(intensity * 10)):
        y1, y2 = np.random.randint(0, frame.shape[0], 2)
        frame_copy[y1:y2] = np.roll(frame_copy[y1:y2], np.random.randint(1, 50), axis=1)
    return frame_copy
    