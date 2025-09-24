from typing import List


def mean(numbers: List[float]) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers: List[float]) -> float:

    if not numbers:
        return 0
    nums = sorted(numbers)
    midpoint = len(nums) // 2
    if len(nums) % 2 == 1:
        return nums[midpoint]
    else:
        return (nums[midpoint] + nums[midpoint - 1]) / 2


def mode(numbers: List[float]) -> float:

    if not numbers:
        return 0
    counts = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1

    max_count = max(counts.values())
    for key in counts:
        if counts[key] == max_count:
            return key


def main() -> None:
    sample = [1, 2, 2, 3, 4]
    user = input("Enter numbers separated by spaces or commas (press Enter to use sample): ")
    if not user.strip():
        numbers = sample
        print("Using sample:", numbers)
    else:
        raw = user.replace(',', ' ')
        parts = [p for p in raw.split(' ') if p != '']
        numbers = []
        for p in parts:
            try:
                numbers.append(float(p))
            except ValueError:
                print(f"Warning: '{p}' is not a valid number and will be ignored.")

    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))


if __name__ == "__main__":
    main()
