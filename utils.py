import cv2
import random
import numpy as np

def build_lst_record(img_path, w, h, bboxes, cids, idx):
    """ Build a standard record file
    :param img_path: path to image relative to the location of .lst file
    :param w: image image width in pixels
    :param h: image image height in pixels
    :param bboxes: list of bounding box coordinates in pixels (xmin, ymin, xmax, ymax)
    :param ids: list of class ids for each box
    :param idx: index of the record
    :return:
    """

    # If bboxes are not given then we are packing for classification which uses only a single header value
    if bboxes is not None:
        # Record header must have at least 2 elements but we also store image width and height so 4
        A = 4  # Header length
        B = 5  # Bbox label length is 5 for boundary boxes
        C = w  # Image width
        D = h  # Image height
        header = [str(x) for x in [A, B, C, D]]

        # Normailise bounding boxes
        bboxes = np.array(bboxes).astype(float)
        bboxes[:, (0, 2)] /= w
        bboxes[:, (1,3)] /= h
        bboxes = np.clip(bboxes, 0., 1.)

        # Concat ids and bboxes
        labels = np.hstack((np.array(cids).reshape(-1, 1), bboxes)).astype('float')
        # labels = np.hstack((np.array(cids).reshape(-1, 1), np.array(norm_boxes))).astype('float')

    else:
        labels = np.array(cids).astype('float')
        header = []  # No header here

    labels = labels.flatten().tolist()
    line = '\t'.join([str(idx)] + header + [str(x) for x in labels] + [img_path])
    return line
        
def draw_bbox(image, bbox, label=None, color=None):

    if color is None:
        color = [random.randint(0, 255) for _ in range(3)]
    x1, y1, x2, y2 = bbox
    cv2.rectangle(image, (x1, y1), (x2, y2), color=color, thickness=5)

    # Assure label is visible
    if label is not None:
        # Assure label is visible
        h, w = image.shape[:2]
        thickness = 2 if w < 1000 else 3 if w < 2000 else 6
        font_scale = 0.8 if w < 1000 else 2 if w < 2000 else 3
        lbl_h = 20 if h < 1000 else 70 if h < 2000 else 150
        lbl_y1 = y1 - lbl_h
        lbl_y2 = y1
        if lbl_y1 < 0:
            lbl_y1, lbl_y2 = y2, y2 + lbl_h
        elif lbl_y2 > h:
            lbl_y1, lbl_y2 = y2 - lbl_h, y2
        cv2.rectangle(image, (x1, lbl_y1), (x2, lbl_y2), color=color, thickness=cv2.FILLED)
        cv2.putText(image, label, (x1 + 5, lbl_y2 - 2), cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale,
                    color=(255, 255, 255), thickness=thickness, lineType=1)


def denormalise_box(box, image):
    x1, y1, x2, y2 = box
    h, w = image.shape[:2]
    x1 = clip(int(float(x1) * w), 0, w)
    y1 = clip(int(float(y1) * h), 0, h)
    x2 = clip(int(float(x2) * w), 0, w)
    y2 = clip(int(float(y2) * h), 0, h)

    return x1, y1, x2, y2


def clip(val, min_val, max_val):
    if val < min_val:
        return min_val
    elif val > max_val:
        return max_val
    else:
        return val
