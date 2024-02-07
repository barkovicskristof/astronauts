import csv


def beolvas(forras):
    with open(forras, newline='', encoding='utf-8') as dokumentum:
        olvas = csv.DictReader(dokumentum)
        hónapok = [row['Birth Date'].split('/')[0] for row in olvas]
    return hónapok


def count_birth_months(birth_months):
    month_counts = {}
    for month in birth_months:
        month_counts[month] = month_counts.get(month, 0) + 1
    return month_counts


def main():
    file_name = 'astronauts.csv'
    birth_months = beolvas(file_name)
    month_counts = count_birth_months(birth_months)
    sorted_months = sorted(month_counts.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_months[:3]
    total_astronauts = sum(month_counts.values())
    for month, count in top_three:
        percentage = (count / total_astronauts) * 100
        print(f"{month}: {percentage:.1f}%")


main()
