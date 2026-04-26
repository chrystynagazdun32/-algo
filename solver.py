def find_minimum_beers(n, b, preferences_string):
    raw_prefs = preferences_string.split()
    worker_preferences = []

    for pref in raw_prefs:
        likes = {i for i, char in enumerate(pref) if char == "Y"}
        worker_preferences.append(likes)

    min_beers = b

    def solve(index, current_count, covered_workers):
        nonlocal min_beers

        if len(covered_workers) == n:
            min_beers = min(min_beers, current_count)
            return

        if current_count >= min_beers or index == b:
            return

        new_covered = covered_workers.copy()
        for i in range(n):
            if index in worker_preferences[i]:
                new_covered.add(i)

        if not (new_covered <= covered_workers):
            solve(index + 1, current_count + 1, new_covered)

        solve(index + 1, current_count, covered_workers)

    solve(0, 0, set())
    return min_beers