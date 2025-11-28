
import cv2
from video_processing import apply_distortion
import argparse

def process_video(input_path, output_path, distortion_type, intensity):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply the selected distortion
        distorted_frame = apply_distortion(frame, distortion_type, intensity)

        if out is None:
            h, w, _ = distorted_frame.shape
            out = cv2.VideoWriter(output_path, fourcc, 30, (w, h))

        out.write(distorted_frame)
        cv2.imshow('Distorted Video', distorted_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reality Distortion Field Project")
    parser.add_argument("--input", required=True, help="Path to input video or '0' for webcam")
    parser.add_argument("--output", required=True, help="Path to save the output video")
    parser.add_argument("--type", required=True, help="Distortion type: temporal, spatial, or glitch")
    parser.add_argument("--intensity", type=float, default=1.0, help="Distortion intensity (0.1 to 3.0)")

    args = parser.parse_args()

    input_path = 0 if args.input == "0" else args.input
    process_video(input_path, args.output, args.type, args.intensity)
    