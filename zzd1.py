import collections
import asyncio
import csv

def listmaker():
    """создаст лист из айдишников
    на основе файла с кучей айдишников и их месейджей"""
    all_id = []
    with open("table.csv") as f:
        reader = csv.reader(f)
        new_list = list(reader)
        pop_exp = new_list.pop(0)
    for row in new_list:
        message = row[0]
        id = row[1]
        all_id.append(id)
    return all_id

async def find_duplicates(lst):
    """на вход принимает лист из наших идишников.
    На выход отдаст только те айдишники  которые повторялись в списке 3 раза.
    асинхронна."""
    counter = collections.Counter(lst)
    duplicates = [id for id in counter if counter[id] == 3]
    return duplicates

my_list = listmaker()

async def main():
    duplicates = await find_duplicates(my_list)
    print("полный список уникальных айдишников которые повторялись только 3 раза: ", duplicates)

if __name__ == '__main__':
    asyncio.run(main())
