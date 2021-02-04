import os
import sys
import argparse

env_path = os.path.join(os.path.dirname(__file__), '..')
if env_path not in sys.path:
    sys.path.append(env_path)

from pytracking.evaluation import Tracker


def run_images(tracker_name, tracker_param, imagefile, debug=None, save_results=False):
    """Run the tracker on your webcam.
    args:
        tracker_name: Name of tracking method.
        tracker_param: Name of parameter file.
        debug: Debug level.
    """
    tracker = Tracker(tracker_name, tracker_param)
    tracker.run_images(imagefilepath=imagefile, debug=debug, save_results=save_results)

def main():
    parser = argparse.ArgumentParser(description='Run the tracker on your webcam.')
    parser.add_argument('tracker_name', type=str, help='Name of tracking method.')
    parser.add_argument('tracker_param', type=str, help='Name of parameter file.')
    parser.add_argument('imagefile', type=str, help='path to a image file.')
    parser.add_argument('--debug', type=int, default=0, help='Debug level.')
    parser.add_argument('--save_result', dest='save_result', action='store_true', help='Save bounding boxes')
    parser.set_defaults(save_result=False)

    args = parser.parse_args()

    run_images(args.tracker_name, args.tracker_param, args.imagefile , args.debug, args.save_result)


if __name__ == '__main__':
    main()
