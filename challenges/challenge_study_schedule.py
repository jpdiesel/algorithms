def study_schedule(permanence_period, target_time):
    try:
        student = int()
        for In, Out in permanence_period:
            if In <= target_time <= Out:
                student += 1
        return student
    except (TypeError, ValueError):
        return None
