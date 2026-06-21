clicks = [1000, 1200, 1500, 5000, 5100, 5200, 10000]
sessions = []
gaps = []

current_session = [clicks[0]]

half_hour = 1800


for i in range(1, len(clicks)):
    current_click = clicks[i]
    previous_click = clicks[i-1]

    gap = current_click - previous_click
    gaps.append(gap)

    if gap <= half_hour:
        current_session.append(current_click)
    else:
        sessions.append(current_session)
        current_session = [current_click]
sessions.append(current_session)
print(sessions)
print(gaps)