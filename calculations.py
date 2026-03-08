import numpy as np

def calculate_wrist_velocity(prev_wrist, curr_wrist, time_delta, w, h):
    if time_delta == 0:
        return 0, 0
    
    # Convert from normalized to pixel coordinates
    prev_x = prev_wrist.x * w
    prev_y = prev_wrist.y * h
    curr_x = curr_wrist.x * w
    curr_y = curr_wrist.y * h

    # Velocity in each direction (can be negative)
    vx = (curr_x - prev_x) / time_delta  # positive = moving right
    vy = (curr_y - prev_y) / time_delta  # positive = moving down, negative = moving up

    return vx, vy

def calculate_angle(a, b, c):
    """
    Calculate angle at point b, between lines ba and bc.
    a, b, c are landmarks e.g. shoulder, elbow, wrist
    """
    a = np.array([a.x, a.y])
    b = np.array([b.x, b.y])
    c = np.array([c.x, c.y])

    # Vectors from b to a and b to c
    ba = a - b
    bc = c - b

    # Dot product formula
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))

    return angle

